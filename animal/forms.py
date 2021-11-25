from dal import autocomplete
from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AnimalForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False
        self.fields['nume'].required = True
        self.fields['proprietar'].required = True
    GENDER_CHOICES = [('Mascul', 'Mascul'),
                      ('Femelă', 'Femelă')]
    VACCINARI = [('nevaccinat', 'nevaccinat'),
                 ('vaccinat conform protocolului', 'vaccinat conform protocolului'),
                 ('parțial', 'parțial'),
                 ('deparazitat', 'deparazitat'),
                 ('nedeparazitat', 'nedeparazitat'),
                 ]
    MEDIUDEVIATA = [('apartament', 'apartament'),
                    ('casacurte', 'casă+curte'),
                    ('curte', 'curte'),
                    ('canisa', 'canisă'),
                    ('altele', 'altele')
                    ]
    CASTRAT = [('da', 'da'),
               ('nu', 'nu')]
    ALIMENTATIE = [('rație menajeră', 'rație menajeră'),
                   ('preparat comercial uscat', 'preparat comercial uscat'),
                   ('preparat comercial umed', 'preparat comercial umed'),]
    CONFORMATIE = [('bună', 'bună'),
                   ('rea', 'rea')]
    CONSTITUTIE = [('fină', 'fină'),
                    ('robustă', 'robustă'),
                   ('debfla', 'debfla'),
                   ('grosolană', 'grosolană')]
    TEMPERAMENT = [('vioi', 'vioi'),
                   ('limfatic', 'limfatic')]
    ATITUDINE = [('nemodificată', 'nemodificată'),
                 ('forțată în stațiune', 'forțată in stațiune'),
                 ('forțată în mers', 'forțată în mers'),
                 ('forțată în decubit', 'forțată în decubit')]
    SCORCLINIC = [('1 (foarte slab)', '1 (foarte slab)'),
                  ('2 (subponderal)', '2 (subponderal)'),
                  ('3 (greutate ideală)', '3 (greutate ideală)'),
                  ('4 (supraponderal)', '4 (supraponderal)'),
                  ('5 (obez)', '5 (obez)')]
    PIELEA = [("hidratare normală", "hidratare normală"),
              ("deshidratare ușoară", "deshidratare ușoară"),
              ("deshidratare medie", "deshidratare medie"),
              ("deshidratare gravă", "deshidratare gravă")]
    PARUL = [("nemodificat", "nemodificat"),
             ("modificat:", "modificat:")]
    LIMFONODURIEXPLORABILE = [("normale", "normale"),
                            ("modificate:", "modificate:")]
    MUCOASEAFERENTE = [("normale", "normale"),
                      ("congestionate", "congestionate"),
                      ('icterice', 'icterice'),
                       ('palide', 'palide'),
                       ('cianotice', 'cianotice')]
    varstaani = forms.IntegerField(widget=forms.NumberInput(attrs={'style': 'width: 50px'}), label='Vârsta')
    greutate = forms.FloatField(widget=forms.NumberInput(attrs={'style': 'width: 50px'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect, label="Sex")
    vaccinarideparazitari = forms.ChoiceField(choices=VACCINARI, widget=forms.RadioSelect, label="Vaccinări și deparazitări")
    castrat = forms.ChoiceField(choices=CASTRAT, widget=forms.RadioSelect, label="Castrat")
    mediudeviata = forms.ChoiceField(choices=MEDIUDEVIATA, widget=forms.RadioSelect, label="Mediu de viață")
    alimentatie = forms.ChoiceField(choices=ALIMENTATIE, widget=forms.RadioSelect, label="Alimentație")
    conformatie = forms.ChoiceField(choices=CONFORMATIE, widget=forms.RadioSelect, label="Conformație")
    constitutie = forms.ChoiceField(choices=CONSTITUTIE, widget=forms.RadioSelect, label="Constituție")
    temperament = forms.ChoiceField(choices=TEMPERAMENT, widget=forms.RadioSelect, label="Temperament")
    atitudine = forms.ChoiceField(choices=ATITUDINE, widget=forms.RadioSelect, label="Atitudine")
    scorclinic = forms.ChoiceField(choices=SCORCLINIC, widget=forms.RadioSelect, label="Stare de întreținere (scor clinic)")
    pielea = forms.ChoiceField(choices=PIELEA, widget=forms.RadioSelect, label="Examenul pielii")
    parul = forms.ChoiceField(choices=PARUL, widget=forms.RadioSelect, label="Părul")
    parulmodificat = forms.CharField(max_length=30)
    altemodificari = forms.CharField(label="Alte modificări", help_text="", widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    limfonoduriexplorabile = forms.ChoiceField(choices=LIMFONODURIEXPLORABILE, widget=forms.RadioSelect, label="Limfonoduri explorabile")
    limfonoduriexplorabiletextarea = forms.CharField(label="Limfonoduri explorabile", help_text="", required=False, widget=forms.Textarea(attrs={'rows': 1, 'cols': 40}))
    mucoaseaferente = forms.ChoiceField(choices=MUCOASEAFERENTE, widget=forms.RadioSelect, label="Mucoase aferente")
    temperatura = forms.FloatField(widget=forms.NumberInput(attrs={'style': 'width: 50px'}))
    trc = forms.FloatField(widget=forms.NumberInput(attrs={'style': 'width: 50px'}), label="TRC")
    frecventarespiratorie = forms.FloatField(label="Frecvența respiratorie", widget=forms.NumberInput(attrs={'style': 'width: 50px'}))
    frecventapulsului = forms.FloatField(label="Frecvența pulsului", widget=forms.NumberInput(attrs={'style': 'width: 50px'}))

    class Meta:
        model = Animal
        fields = '__all__'

        widgets = {
            'proprietar': autocomplete.ModelSelect2(url='proprietar-autocomplete')
        }


