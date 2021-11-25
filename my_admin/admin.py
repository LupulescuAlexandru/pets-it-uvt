from django.contrib import admin, messages
from django.contrib.admin.options import IS_POPUP_VAR
from django.contrib.admin.utils import unquote
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.admin import sensitive_post_parameters_m
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.utils.html import escape
from django.utils.translation import gettext
from django.urls import reverse, path
from django.contrib.auth.models import User
from .forms import AdminPasswordChangeForm, UserChangeForm

class UserAdmin(admin.ModelAdmin):
    change_list_template = 'admin/auth/user/change_list.html'
    add_form_template = 'admin/auth/user/add_form.html'
    change_user_password_template = 'admin/auth/user/change_password.html'
    form = UserChangeForm
    change_password_form = AdminPasswordChangeForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Informații personale'), {'fields': ['email',]}),
        (('Permisiuni'), {
            'fields': ('is_staff', 'groups'),
        }),
        (('Activitate cont'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)

    def get_urls(self):
        return [
                   path(
                       '<id>/password/',
                       self.admin_site.admin_view(self.user_change_password),
                       name='auth_user_password_change',
                   ),
               ] + super().get_urls()

    @sensitive_post_parameters_m
    def user_change_password(self, request, id, form_url=''):
        user = self.get_object(request, unquote(id))
        if not self.has_change_permission(request, user) or (str(request.user.id) != id):
            raise PermissionDenied
        if user is None:
            raise Http404(('%(name)s object with primary key %(key)r does not exist.') % {
                'name': self.model._meta.verbose_name,
                'key': escape(id),
            })
        if request.method == 'POST':
            form = self.change_password_form(user, request.POST)
            if form.is_valid():
                form.save()
                change_message = self.construct_change_message(request, form, None)
                self.log_change(request, user, change_message)
                msg = gettext('Password changed successfully.')
                messages.success(request, msg)
                update_session_auth_hash(request, form.user)
                return HttpResponseRedirect(
                    reverse(
                        '%s:%s_%s_change' % (
                            self.admin_site.name,
                            user._meta.app_label,
                            user._meta.model_name,
                        ),
                        args=(user.pk,),
                    )
                )
        else:
            form = self.change_password_form(user)

        fieldsets = [(None, {'fields': list(form.base_fields)})]
        adminForm = admin.helpers.AdminForm(form, fieldsets, {})

        context = {
            'title': ('Change password: %s') % escape(user.get_username()),
            'adminForm': adminForm,
            'form_url': form_url,
            'form': form,
            'is_popup': (IS_POPUP_VAR in request.POST or
                         IS_POPUP_VAR in request.GET),
            'add': True,
            'change': False,
            'has_delete_permission': False,
            'has_change_permission': True,
            'has_absolute_url': False,
            'opts': self.model._meta,
            'original': user,
            'save_as': False,
            'show_save': True,
            **self.admin_site.each_context(request),
        }

        request.current_app = self.admin_site.name

        return TemplateResponse(
            request,
            self.change_user_password_template or
            'admin/auth/user/change_password.html',
            context,
        )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super(UserAdmin, self).get_form(request, obj, change, **kwargs)
        if(obj.id != request.user.id):
            for field in form.base_fields:
                form.base_fields[field].widget.attrs['disabled'] = True
        else:
            for field in form.base_fields:
                form.base_fields[field].widget.attrs['disabled'] = False
        return form

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['title'] = 'Identificare utilizatori'
        return super(UserAdmin, self).changelist_view(request, extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['title'] = 'Vizualizare utilizator'
        return super(UserAdmin, self).change_view(request, object_id, form_url, extra_context)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

