from django.contrib import admin
from .models import Fisa
from .forms import FisaForm
from docxtpl import DocxTemplate
from django.utils.html import format_html
from .models import ConsumabileFisa

class ConsumabileInline(admin.TabularInline):
    model = ConsumabileFisa

class FisaAdmin(admin.ModelAdmin):
    def show_url(self, obj):
        return format_html(
            "<a href='/media/fise/{url}.docx'><img src='https://cdn1.iconfinder.com/data/icons/hawcons/32/698873-icon-136-document-edit-512.png' width='20' height='20'></img></a>",
            url=obj.animal)

    '''
    def request_modification(self, obj):
        return format_html('<a class="button" href="{}">Solicitare modificare</a>', reverse('request_modification_view', args=[obj.id]))'''

    show_url.short_description = "Document trimitere"
    form = FisaForm
    change_form_template = 'admin/fise/change_form.html'
    change_list_template = 'admin/fise/change_list.html'
    list_display = ['animal', 'show_url']
    search_fields = ['animal__microcip', 'animal__nume']
    inlines = (ConsumabileInline,)
    fieldsets = (
        ('Identificare animal', {
            'fields': ('animal', ),
        }),
      ('Examenul aparatului digestiv', {
          'fields': ('apetit',
                    "consumulvoluntardeapa",
                    "prehensiunea",
                    "masticatia",
                    "deglutitia",
                    "voma",
                    "defecarea",
                    "examenulcavitatiiorale",
                    "examenulcavitatiioraleother",
                    "examenulfaringului",
                    "examenulfaringuluiother",
                    "examenulesofagului",
                    "examenulesofaguluiother",
                    "examenulabdomenului",
                    "examenulabdomenuluiother",
                    "examenulstomacului",
                    "examenulstomaculuiother",
                    "examenulintestinelor",
                    "examenulintestinelorother",
                    "examenulanusului",
                    "examenulanusuluiother",
                    "examenulfecalelor",
                    "examenulfecalelorother",
                    "eaxmenulglanexe",
                    "eaxmenulglanexeother",
                    "examenulglsalivare",
                    "examenulglsalivareother",
                    "ariahepatica",
                    "ariapancreatica")
      }),
        ('Examenul aparatului respirator', {
            'fields': ("tuse",
                        "jetaj",
                        "mirosulaparatuluiexpirat",
                        "mirosulaparatuluiexpiratother",
                        "cornaj",
                        "examenulnasului",
                       "examenulnasuluiother",
                       "examenulsinusului",
                       "examenulsinusuluiother",
                       "examenullaringelui",
                       "examenullaringeluiother",
                       "examenultraheei",
                       "examenultraheeiother")
        }),
        ('Examenul toraco-pulmonar', {
            'fields': ("tipulrespiraor",
                        "dispnee",
                        "murmurvezicular",
                        "raluriuscate",
                        "raluriumede",
                        "sufluri",
                        "sunetpercutie",
                        "altemodificaritoraco2",)
        }),
        ('Examenul aparatului cardio-vascular', {
            'fields': ("dispneecardio",
                        "zgomotulcardiac",
                        "zgomotulcardiacother",
                        "pulsul",
                        "altemodificaricardio",)
        }),
        ('Examenul aparatului urinar', {
            'fields': ("mictiunea",)
        }),
        ('Examenul rinichilor', {
            'fields': ("sensibilitatea",
                       "marime",)
        }),
        ('Examenul vezicii urinare', {
            'fields': ("sensibilitateavezicii",
                       "graddeplentitudine",
                       "altemodificariurinar",)
        }),
        ('Examenul aparatului locomotor', {
            'fields': ("schiopatura",
                        "schiopaturaother",
                        "aplomburi",
                        "tumefacatiiarticulare",
                        "mobilitatearticulara",
                        "durerearticulara",
                        "durerediafizara",
                        "deficitpropioceptiv",
                        "masamusculara",
                        "tonusmuscular",)
        }),
        ('Examenul complementar', {
            'fields': ("examenulcomplementarfield",
                        "diagnostic",
                        "tratament",)
        }),
   )

    '''
    def get_form(self, request, obj=None, **kwargs):
        form = super(FisaAdmin, self).get_form(request, obj, **kwargs)
        if obj:
            if obj.permission == True:
                for field in form.base_fields:
                    form.base_fields[field].disabled = False
            else:
                for field in form.base_fields:
                    form.base_fields[field].disabled = True
        else:
            for field in form.base_fields:
                form.base_fields[field].disabled = False
        return form
        '''
    '''
    def get_inline_formsets(self, request, formsets, inline_instances, obj=None):
        inline_admin_formsets = []
        for inline, formset in zip(inline_instances, formsets):
            fieldsets = list(inline.get_fieldsets(request, obj))
            readonly = list(inline.get_readonly_fields(request, obj))
            prepopulated = dict(inline.get_prepopulated_fields(request, obj))
            inline_admin_formset = helpers.InlineAdminFormSet(
                inline, formset, fieldsets, prepopulated, readonly,
                model_admin=self,
            )

            if isinstance(inline, ConsumabileInline):
                if obj:
                    if obj.permission == True:
                        for form in inline_admin_formset.forms:
                            for field in form.fields:
                                form.fields[field].disabled = False
                    else:
                        for form in inline_admin_formset.forms:
                            for field in form.fields:
                                form.fields[field].disabled = True
                else:
                    for form in inline_admin_formset.forms:
                        for field in form.fields:
                            form.fields[field].disabled = False

            inline_admin_formsets.append(inline_admin_formset)
        return inline_admin_formsets'''

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['title'] = "Identificare fișă"
        return super(FisaAdmin, self).changelist_view(request, extra_context)

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        otherchoices = ["examenulcavitatiiorale",
                        "examenulfaringului",
                        "examenulesofagului",
                        "examenulabdomenului",
                        "examenulstomacului",
                        "examenulintestinelor",
                        "examenulanusului",
                        "examenulfecalelor",
                        "eaxmenulglanexe",
                        "examenulglsalivare",
                        "mirosulaparatuluiexpirat",
                        "examenulnasului",
                        "examenulsinusului",
                        "examenultraheei",
                        "examenullaringelui",
                        "sunetpercutie",
                        "dispneecardio",
                        "zgomotulcardiac",
                        ]

        otherotherChoices = ["examenulcavitatiioraleother",
                        "examenulfaringuluiother",
                        "examenulesofaguluiother",
                        "examenulabdomenuluiother",
                        "examenulstomaculuiother",
                        "examenulintestinelorother",
                        "examenulanusuluiother",
                        "examenulfecalelorother",
                        "eaxmenulglanexeother",
                        "examenulglsalivareother",
                        "mirosulaparatuluiexpiratother",
                        "examenulnasuluiother",
                        "examenulsinusuluiother",
                        "examenultraheeiother",
                        "examenullaringeluiother",
                        "sunetpercutieother",
                        "dispneecardioother",
                        "zgomotulcardiacother",
                        "schiopaturaother",
                        ]
        extra_context['title'] = "Adăugare fișă"
        extra_context['otherChoice'] = otherchoices
        extra_context['otherotherChoice'] = otherotherChoices

        return super().changeform_view(request, object_id, form_url, extra_context)

    def save_model(self, request, obj, form, change):
        if request.method == 'POST':
            form = FisaForm(request.POST)
            if form.is_valid():
                doc = DocxTemplate("FISADEOBSERVATIE.docx")
                context = {'proprietar_nume': obj.animal.proprietar.nume if obj.animal.proprietar.nume != None else " ",
                           'proprietar_adresa': obj.animal.proprietar.adresa if obj.animal.proprietar.adresa != None else " ",
                           'proprietar_telefon': obj.animal.proprietar.telefon if obj.animal.proprietar.telefon != None else " ",
                           'specia': obj.animal.specia if obj.animal.specia != None else " ",
                           'rasa': obj.animal.rasa if obj.animal.rasa != None else " ",
                           'varstaani': str(obj.animal.varstaani) + " ani " if obj.animal.varstaani != None else " ",
                           'varstaluni': str(obj.animal.varstaluni) + " luni" if obj.animal.varstaluni != None else " ",
                           'sex': obj.animal.gender,
                           'greutate': str(obj.animal.greutate) + " kg" if obj.animal.greutate != None else " ",
                           'culoare': obj.animal.culoare if obj.animal.culoare != None else " ",
                           'nume': obj.animal.nume,
                           'vaccinari': obj.animal.vaccinarideparazitari,
                           'castrat': obj.animal.castrat,
                           'mediudeviata': obj.animal.mediudeviata,
                           'anamneza': obj.animal.anamneza,
                           'antecedente': obj.animal.antecedente,
                           'alimentatia': obj.animal.alimentatie,
                           'conformatie': obj.animal.conformatie,
                           'temperament': obj.animal.temperament,
                           'constitutie': obj.animal.constitutie,
                           'atitudine': obj.animal.atitudine,
                           'scorclinic': obj.animal.scorclinic,
                           'pielea': obj.animal.pielea,
                           'altemodificari': obj.animal.altemodificari,
                           'parul': obj.animal.parul,
                           'parulmodificat': obj.animal.parulmodificat,
                           'limfonoduriexplorabile': obj.animal.limfonoduriexplorabile,
                           'limfonoduriexplorabileother': obj.animal.limfonoduriexplorabiletextarea,
                           'mucoaseaferente': obj.animal.mucoaseaferente,
                           'temperatura': str(obj.animal.temperatura) + "°C",
                           'trc': obj.animal.trc if obj.animal.trc != None else " ",
                           'frecventarespiratorie': obj.animal.frecventarespiratorie if obj.animal.frecventarespiratorie != None else " ",
                           'frecventapulsului': obj.animal.frecventapulsului if obj.animal.frecventapulsului != None else " ",
                           'apetit': obj.apetit,
                            'consumapa': obj.consumulvoluntardeapa,
                           'prehensiunea': obj.prehensiunea,
                            "masticatia": obj.masticatia,
                           "deglutitia": obj.deglutitia,
                            "voma": obj.voma,
                           "defecarea": obj.defecarea,
                            'cavitateorala': obj.examenulcavitatiiorale,
                           'cavitateoralaother': obj.examenulcavitatiioraleother,
                           'faringe': obj.examenulfaringului,
                           'faringeother': obj.examenulfaringuluiother,
                           'esofag': obj.examenulesofagului,
                           'esofagother': obj.examenulesofaguluiother,
                           'abdomen': obj.examenulabdomenului,
                           'abdomenother': obj.examenulabdomenuluiother,
                           'stomac': obj.examenulstomacului,
                           'stomacother': obj.examenulstomaculuiother,
                           'intestine': obj.examenulintestinelor,
                           'intestineother': obj.examenulintestinelorother,
                           'anus': obj.examenulanusului,
                           'anusother': obj.examenulanusuluiother,
                           'fecale': obj.examenulfecalelor,
                           'fecaleother': obj.examenulfecalelorother,
                           'glandeanexe': obj.eaxmenulglanexe,
                           'glandeanexeother': obj.eaxmenulglanexeother,
                           'glandesalivare': obj.examenulglsalivare,
                           'glandesalivareother': obj.examenulglsalivareother,
                           'ariahepatica': obj.ariahepatica,
                           'ariapancreatica': obj.ariapancreatica,
                           'tuse': obj.tuse,
                           'jetaj': obj.jetaj,
                            'mirosulaeruluiexpirat': obj.mirosulaparatuluiexpirat,
                           'mirosulaeruluiexpiratother': obj.mirosulaparatuluiexpiratother,
                           'cornaj': obj.cornaj,
                           'nas': obj.examenulnasului,
                           'nasother': obj.examenulnasuluiother,
                           'sinusuri': obj.examenulsinusului,
                           'sinusuriother': obj.examenulsinusuluiother,
                           'laringe': obj.examenullaringelui,
                           'laringeother': obj.examenullaringeluiother,
                           'trahee': obj.examenultraheei,
                           'traheeother': obj.examenultraheeiother,
                           'tipulrespirator':obj.tipulrespiraor,
                            'dispnee':obj.dispnee,
                           'altemodificaritoraco':obj.altemodificaritoraco2,
                            'murmurvezicular':obj.murmurvezicular,
                           'raluriuscate':obj.raluriuscate,
                            'raluriumede':obj.raluriumede,
                           'sufluri':obj.sufluri,
                            'sunetpercutie':obj.sunetpercutie if obj.sunetpercutie != None else " ",
                           'sunetpercutieother':obj.sunetpercutieother if obj.sunetpercutieother != None else " ",
                           'dispneecardio':obj.dispneecardio if obj.dispneecardio != None else " ",
                            'dispneecardioother':obj.dispneecardioother if obj.dispneecardioother != None else " ",
                           'zgomotulcardiac':obj.zgomotulcardiac,
                            'zgomotulcardiacother':obj.zgomotulcardiacother,
                           'pulsul':obj.pulsul,
                            'altemodificaricardio': obj.altemodificaricardio,
                           'mictiunea':obj.mictiunea,
                            'sensibilitatea':obj.sensibilitatea,
                           'marime':obj.marime,
                            'sensibilitateavezicii':obj.sensibilitateavezicii,
                           'graddeplentitudine':obj.graddeplentitudine,
                            'altemodificarivezicii':obj.altemodificariurinar,
                           'schiopatura':obj.schiopatura,
                           'schipaturaother': obj.schiopaturaother,
                            'aplomburi':obj.aplomburi,
                           'tumefactiiarticulare':obj.tumefacatiiarticulare,
                            'mobilitatearticulara':obj.mobilitatearticulara,
                           'durerearticulara':obj.durerearticulara,
                            'durerediafizara':obj.durerediafizara,
                           'deficitpropioceptiv':obj.deficitpropioceptiv,
                            'masamusculara':obj.masamusculara,
                           'tonusmuscular':obj.tonusmuscular,

                           }
                doc.render(context)
                doc.save("media/fise/" + str(obj.animal) + ".docx")
        super().save_model(request, obj, form, change)

admin.site.register(Fisa, FisaAdmin)
