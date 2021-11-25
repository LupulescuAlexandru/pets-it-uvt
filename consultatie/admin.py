from django.contrib import admin
from django.forms import ModelForm
from django.http import HttpResponseBadRequest
from django.utils.html import format_html
from animal.models import Animal
from .models import consultatie
from bootstrap_datepicker_plus import TimePickerInput, DatePickerInput


class ConsultatieForm(ModelForm):
    class Meta:
        model = consultatie
        fields = ['animal', 'dataconsultatie', 'oraconsultatie', 'tratamente']
        widgets = {
            'dataconsultatie': DatePickerInput(),
            'oraconsultatie': TimePickerInput(),
        }

@admin.register(consultatie)
class ConsultatieAdmin(admin.ModelAdmin):
    list_display = ['dataoraconsultatie', 'tratamente']
    search_fields = ['animal__name']
    form = ConsultatieForm
    change_list_template = 'consultatie/change_list.html'
    change_form_template = 'consultatie/change_form.html'

    def rezumat(self, obj):
        return format_html('<b>Tratamente:<b><br>{}'.format(obj.tratamente))

    def dataoraconsultatie(self, obj):
        return format_html('<a href="/consultatie/consultatie/{}/change/?_changelist_filters=animal__id__exact={}">{} - {}</a>'
                           .format(obj.id, obj.animal.id, obj.dataconsultatie.strftime("%d %b %Y"), obj.oraconsultatie.strftime("%H:%M")))

    dataoraconsultatie.short_description = "Dată consultație"

    def show_object_title(self, request):
        animal_id = request.GET['animal__id__exact']
        if int(animal_id):
            animal = Animal.objects.get(id=animal_id)
            return animal

    def changelist_view(self, request, extra_context=None):
        animal_id = request.GET['animal__id__exact']
        extra_context = {'title': str(self.show_object_title(request).nume) + ", proprietar " +str(self.show_object_title(request).proprietar) + " - consultatii",
                         'addBtnAnimal': animal_id}
        return super(ConsultatieAdmin, self).changelist_view(request, extra_context)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        animal_id = request.GET['_changelist_filters'].split('=')[1]
        try:
            extra_context = {'title': 'Add consultatie',
                'addBtnAnimal': int(animal_id)}
        except ValueError:
            return HttpResponseBadRequest()
        return super(ConsultatieAdmin, self).changeform_view(request, object_id, form_url, extra_context)
