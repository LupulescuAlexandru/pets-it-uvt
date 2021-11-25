from django.contrib import admin
from django.utils.html import format_html
from .models import Proprietar, Animal
from .forms import AnimalForm

class ProprietarAdmin(admin.ModelAdmin):
    list_display = ['nume', 'telefon']
    change_list_template = 'admin/proprietar/change_list.html'
    change_form_template = 'admin/proprietar/change_form.html'

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['title'] = "Identificare proprietar"
        return super(ProprietarAdmin, self).changelist_view(request, extra_context)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['title'] = "Adăugare proprietar"
        return super(ProprietarAdmin,self).changeform_view(request, object_id, form_url, extra_context)

class AnimalAdmin(admin.ModelAdmin):
    change_form_template = 'admin/animal/change_form.html'
    change_list_template = 'admin/animal/change_list.html'
    list_display = ['nume', 'proprietar', 'view_consultation']
    form = AnimalForm
    search_fields = ['nume', 'microcip']

    def view_consultation(self, obj):
        return format_html('<a href="/consultatie/consultatie/?animal__id__exact={0}"class="button" style="background-color:#3ab44a;color: white; font-size: 13px; cursor:pointer;">Consultatii</a>'.format(obj.id))
    view_consultation.short_description = "Consultații"

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['title'] = "Identificare animal"
        return super(AnimalAdmin, self).changelist_view(request, extra_context)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        otherchoices = ['parulmodificat', 'limfonoduriexplorabiletextarea', 'greutate', 'temperatura', 'varstaani']
        extra_context['otherChoice'] = otherchoices
        extra_context['title'] = "Adăugare animal"
        return super(AnimalAdmin, self).changeform_view(request, object_id, form_url, extra_context)

admin.site.register(Proprietar, ProprietarAdmin)
admin.site.register(Animal, AnimalAdmin)
