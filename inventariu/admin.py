from django.contrib import admin
from .models import Consumabile
from .forms import ConsumabileForm
from django.contrib.admin.models import LogEntry


class ConsumabileAdmin(admin.ModelAdmin):
    form = ConsumabileForm
    change_list_template = 'change_list.html'

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['title'] = "Identificare consumabile"
        return super(ConsumabileAdmin, self).changelist_view(request, extra_context)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['title'] = "Adăugare consumabil"
        return super(ConsumabileAdmin, self).changeform_view(request, object_id, form_url, extra_context)

class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user', 'action_time']

admin.site.register(Consumabile, ConsumabileAdmin)
admin.site.register(LogEntry, LogEntryAdmin)

