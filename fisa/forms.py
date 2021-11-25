from dal import autocomplete
from django import forms
from animal.models import Animal
from .models import Fisa

class FisaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FisaForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False
        self.fields["animal"].required = True

    # animal = forms.ModelChoiceField(
    #     widget=autocomplete.ModelSelect2(url='animal-autocomplete'),
    # )
    APETIT = [("normal", "normal"),
              ("scăzut", "scăzut"),
              ("selectiv", "selectiv"),
              ("anorexic", "anorexic"),
              ("bulimie", "bulimie")]
    CONSUMULVOLUNTARDEAPA = [("normal", "normal"),
                            ("scăzut", "scăzut"),
                            ("crescut", "crescut")]
    PREHENSIUNEA = [("normală", "normală"),
              ("dificilă", "dificilă"),
              ("absentă", "absentă")]
    MASTICATIA = [("normală", "normală"),
              ("dificilă", "dificilă"),
              ("absentă", "absentă")]
    DEGLUTITIA = [("normală", "normală"),
              ("disfagie ord. I", "disfagie ord. I"),
              ("disfagie ord. II", "disfagie ord. II"),
              ("disfagie ord. III", "disfagie ord. III")]
    VOMA = [("alimentară", "alimentară"),
              ("spumoasă", "spumoasă"),
              ("gleroasă", "gleroasă"),
              ("biloasă", "biloasă"),
              ("fecaleidă", "fecaleidă"),
            ("hemoragică", "hemoragică"),
            ("anică", "anică"),
            ("repetată", "repetată"),
            ("incoercibiă", "incoercibilă")]
    DEFECAREA = [("normală", "normală"),
                 ("absentă", "absentă"),
                 ("frecventă, în cantități mici", "frecventă, în cantități mici"),
                 ("cu tenesme", "cu tenesme")]
    EXAMENULCAVITATIIORALE = [("fără modificări", "fără modificări"),
                              ("modificări:", "modificări:")]
    EXAMENULFARINGULUI = [("fără modificări", "fără modificări"),
       ("modificări: ", "modificări: ")]
    EXAMENULESOFAGULUI = [("fără modificări", "fără modificări"),
       ("modificări: ", "modificări: ")]
    EXAMENULABDOMENULUI = [("fără modificări", "fără modificări"),
       ("modificări: ", "modificări: ")]
    EXAMENULSTOMACULUI = [("fără modificări", "fără modificări"),
       ("modificări: ", "modificări: ")]
    EXAMENULINTESTINELOR = [("fără modificări", "fără modificări"),
       ("modificări: ", "modificări: ")]
    EXAMENULANUSULUI = [("fără modificări", "fără modificări"),
       ("modificări: ", "modificări: ")]
    EXAMENULFECALELOR = [("fără modificări", "fără modificări"),
       ("modificări: ", "modificări: ")]
    EXAMENULGLANEXE = [("fără modificări", "fără modificări"),
       ("modificări: ", "modificări: ")]
    EXAMENULGLSALIVARE = [("fără modificări", "fără modificări"),
       ("modificări: ", "modificări: ")]
    ARIAHEPATICA = [("normală", "normală"),
                    ("marită", "marită"),
                    ("sensibilă", "sensibilă")]
    ARIAPANCREATICA = [("normală", "normală"),
                       ("sensibilă", "sensibilă")]
    # examenul aparatului respirator
    TUSE = [("seacă", "seacă"),
            ("umedă", "umedă"),
            ("unică", "unică"),
            ("rară", "rară"),
            ("repetată", "repetată"),
            ("frecventă", "frecventă"),
            ("nocturnă", "nocturnă")]
    JETAJ = [("absent", "absent"),
            ("seros", "seros"),
            ("mucos", "mucos"),
            ("purulent", "purulent"),
            ("hemoragic", "hemoragic"),
            ("alimentar", "alimentar")]
    MIROSULAPARATULUIRESPIRAT = [("fad", "fad"),
                                 ("modificat", "modificat")]
    CORNAJ = [("absent", "absent"), #not sure
            ("seros", "seros"), #not sure
            ("traheal", "mucos"),
            ("bronșic", "bronșic"),]
    EXAMENULNASULUI = [("fără modificări", "fără modificări"),
       ("modificări: ", "modificări: ")]
    EXAMENULSINUSULUI = [("fără modificări", "fără modificări"),
       ("modificări: ", "modificări: ")]
    EXAMENULLARINGELUI = [("fără modificări", "fără modificări"),
       ("modificări: ", "modificări: ")]
    EXAMENULTRAHEEI = [("fără modificări", "fără modificări"),
       ("modificări: ", "modificări: ")]
    #examenul toraco-pulmonar
    TIPULRESPIRATOR = [("toracal", "toracal"),
                       ("toraco-abdominal", "toraco-abdominal"),
                       ("abdominal", "abdominal")]
    DISPNEE = [("absentă", "absentă"),
               ("inspiratorie", "inspiratorie"),
               ("expiratorie", "expiratorie"),
               ("la efort intens", "la efort intens"),
               ("la efort mediu", "la efort mediu"),
               ("repaus", "repaus")] #not sure
    MURMURVEZICULAR = [("nemodificat", "nemodificat"),
                       ("diminuat", "diminuat"),
                       ("inasprit", "inasprit"),
                       ("abolit", "abolit")]
    SUNETPERCUTIE = [("normal", "normal"),
                     ("modificat:", "modificat:")]
    DISPNEECARDIO = [("absentă", "absentă"),
                     ("prezentă", "prezentă")]
    ZGOMOTULCARDIAC = [("normal", "normal"),
                       ("modificat", "modificat")]
    PULSUL = [("normal", "normal"),
              ("modificat", "modificat")]
    #examenul aparatului digestiv
    MICTIUNEA = [("normală", "normală"),
                 ("poliurie", "poliurie"),
                 ('oligurie', 'oligurie'),
                 ('anurie', 'anurie'),
                 ('strangurie', 'strangurie'),
                 ('tenesme urinare', 'tenesme urinare'),
                 ('incontinenţă Urinară', 'incontinenţă urinară')]
    SENSIBILITATEA = [("normală", "normală"),
                      ("crescută", "crescută")]
    MARIME = [("normală", "normală"),
              ("micsorați", "micsorați"),
              ("mariți", "mariți")]
    GRADDEPLENTITUDINE = [("normal", "normal"),
                          ("redusă", "redusă"),
                          ("tensionată", "tensionată"),
                          ("bloc vezical", "bloc vezical")]
    #examenul aparatului locomotor
    SCHIOPATURA = [("absentă", "absentă"),
                   ("intermitentă", "intermitentă"),
                   ("permanentă", "permanentă"),
                   ("altele:", "altele:")]
    APLOMBURI = [("corecte", "corecte"),
                 ("defectuoase", "defectuoase")]
    TUMEFACATIIARTICULARE = [("absente", "absente"),
                             ("simetrice", "simterice"),
                             ("asimetrice", "asimetrice"),
                             ("reci", "reci"),
                             ("calde", "calde")]
    MOBILITATEARTICULARA = [("normală", "normală"),
                            ("redusă", "redusă"),
                            ("crescută", "crescută")]
    DUREREARTICULARADIAFIZARA = [("absentă", "absentă"),
                        ("ușoară", "ușoară"),
                        ("moderată", "moderată"),
                        ("severă", "severă")]
    DEFICITPROPIOCEPTIV = [("da", "da"),
                           ("nu", "nu")]
    MASAMUSCULARA = [("normal dezvoltată", "normal dezvoltată"),
                     ("subdezvoltată", "subdezvoltată"),
                     ("amiotrofie", "amiotrofie")]
    TONUSMUSCULAR = [("normal", "normal"),
                     ("hipotonie", "hipotonie"),
                     ("hipertonie", "hipertonie")]
    apetit = forms.ChoiceField(choices=APETIT, widget=forms.RadioSelect)
    consumulvoluntardeapa = forms.ChoiceField(choices=CONSUMULVOLUNTARDEAPA, widget=forms.RadioSelect, label="Consum apă")
    prehensiunea = forms.ChoiceField(choices=PREHENSIUNEA, widget=forms.RadioSelect)
    masticatia = forms.ChoiceField(choices=MASTICATIA, widget=forms.RadioSelect, label="Masticația")
    deglutitia = forms.ChoiceField(choices=DEGLUTITIA, widget=forms.RadioSelect, label="Deglutiția")
    voma = forms.ChoiceField(choices=VOMA, widget=forms.RadioSelect)
    defecarea = forms.ChoiceField(choices=DEFECAREA, widget=forms.RadioSelect)
    examenulcavitatiiorale = forms.ChoiceField(choices=EXAMENULCAVITATIIORALE, widget=forms.RadioSelect, label="Cavitate orală")
    examenulfaringului = forms.ChoiceField(choices=EXAMENULFARINGULUI, widget=forms.RadioSelect, label="Faringe")
    examenulesofagului = forms.ChoiceField(choices=EXAMENULESOFAGULUI, widget=forms.RadioSelect, label="Esofag")
    examenulabdomenului = forms.ChoiceField(choices=EXAMENULABDOMENULUI, widget=forms.RadioSelect, label="Abdomenului")
    examenulstomacului = forms.ChoiceField(choices=EXAMENULSTOMACULUI, widget=forms.RadioSelect, label="Stomac")
    examenulintestinelor = forms.ChoiceField(choices=EXAMENULINTESTINELOR, widget=forms.RadioSelect, label="Intestine")
    examenulanusului = forms.ChoiceField(choices=EXAMENULANUSULUI, widget=forms.RadioSelect, label="Anus")
    examenulfecalelor = forms.ChoiceField(choices=EXAMENULFECALELOR, widget=forms.RadioSelect, label="Fecale")
    eaxmenulglanexe = forms.ChoiceField(choices=EXAMENULGLANEXE, widget=forms.RadioSelect, label="Glande anexe")
    examenulglsalivare = forms.ChoiceField(choices=EXAMENULGLSALIVARE, widget=forms.RadioSelect, label="Glande salivare")
    ariahepatica = forms.ChoiceField(choices=ARIAHEPATICA, widget=forms.RadioSelect, label="Aria hepatică")
    ariapancreatica = forms.ChoiceField(choices=ARIAPANCREATICA, widget=forms.RadioSelect, label="Aria pancreatică")
    examenulcavitatiioraleother = forms.CharField(label="Limfonoduri explorabile", help_text="", required=False, widget=forms.Textarea(attrs={'rows': 1, 'cols': 40}))
    examenulfaringuluiother= forms.CharField(label="Limfonoduri explorabile", help_text="", required=False, widget=forms.Textarea(attrs={'rows': 1, 'cols': 40}))
    examenulesofaguluiother= forms.CharField(label="Limfonoduri explorabile", help_text="", required=False, widget=forms.Textarea(attrs={'rows': 1, 'cols': 40}))
    examenulabdomenuluiother= forms.CharField(label="Limfonoduri explorabile", help_text="", required=False, widget=forms.Textarea(attrs={'rows': 1, 'cols': 40}))
    examenulstomaculuiother= forms.CharField(label="Limfonoduri explorabile", help_text="", required=False, widget=forms.Textarea(attrs={'rows': 1, 'cols': 40}))
    examenulintestinelorother= forms.CharField(label="Limfonoduri explorabile", help_text="", required=False, widget=forms.Textarea(attrs={'rows': 1, 'cols': 40}))
    examenulanusuluiother= forms.CharField(label="Limfonoduri explorabile", help_text="", required=False, widget=forms.Textarea(attrs={'rows': 1, 'cols': 40}))
    examenulfecalelorother= forms.CharField(label="Limfonoduri explorabile", help_text="", required=False, widget=forms.Textarea(attrs={'rows': 1, 'cols': 40}))
    eaxmenulglanexeother= forms.CharField(max_length=30)
    examenulglsalivareother= forms.CharField(label="Limfonoduri explorabile", help_text="", required=False, widget=forms.Textarea(attrs={'rows': 1, 'cols': 40}))
    # examenul aparatului respirator
    tuse = forms.ChoiceField(choices=TUSE, widget=forms.RadioSelect)
    jetaj = forms.ChoiceField(choices=JETAJ, widget=forms.RadioSelect)
    mirosulaparatuluiexpirat = forms.ChoiceField(choices=MIROSULAPARATULUIRESPIRAT, widget=forms.RadioSelect, label="Mirosul aerului expirat")
    mirosulaparatuluiexpiratother = forms.CharField(label="Limfonoduri explorabile", help_text="", required=False, widget=forms.Textarea(attrs={'rows': 1, 'cols': 40}))
    cornaj = forms.ChoiceField(choices=CORNAJ, widget=forms.RadioSelect)
    examenulnasului = forms.ChoiceField(choices=EXAMENULNASULUI, widget=forms.RadioSelect, label="Nas")
    examenulnasuluiother = forms.CharField(label="Limfonoduri explorabile", help_text="", required=False, widget=forms.Textarea(attrs={'rows': 1, 'cols': 40}))
    examenulsinusului = forms.ChoiceField(choices=EXAMENULSINUSULUI, widget=forms.RadioSelect, label="Sinusuri")
    examenulsinusuluiother = forms.CharField(label="Limfonoduri explorabile", help_text="", required=False, widget=forms.Textarea(attrs={'rows': 1, 'cols': 40}))
    examenullaringelui = forms.ChoiceField(choices=EXAMENULLARINGELUI, widget=forms.RadioSelect, label="Laringe")
    examenullaringeluiother = forms.CharField(label="Limfonoduri explorabile", help_text="", required=False, widget=forms.Textarea(attrs={'rows': 1, 'cols': 40}))
    examenultraheei = forms.ChoiceField(choices=EXAMENULTRAHEEI, widget=forms.RadioSelect, label="Trahee")
    examenultraheeiother = forms.CharField(label="Traheei", help_text="", required=False, widget=forms.Textarea(attrs={'rows': 1, 'cols': 40}))
    #exaemnul toraco-pulmonar
    tipulrespiraor = forms.ChoiceField(choices=TIPULRESPIRATOR, widget=forms.RadioSelect, label="Tipul respirator")
    dispnee = forms.ChoiceField(choices=DISPNEE, widget=forms.RadioSelect)
    murmurvezicular = forms.ChoiceField(choices=MURMURVEZICULAR, widget=forms.RadioSelect, label="Murmur vezicular")
    raluriuscate = forms.ChoiceField(choices=TIPULRESPIRATOR, widget=forms.RadioSelect, label="Raluri uscate")
    raluriumede = forms.ChoiceField(choices=TIPULRESPIRATOR, widget=forms.RadioSelect, label="Raluri umede")
    sufluri = forms.CharField(widget=forms.Textarea(attrs={'rows': 1, 'cols': 40}), label="Sufluri")
    sunetpercutie = forms.ChoiceField(choices=SUNETPERCUTIE, widget=forms.RadioSelect, label="Sunet percuție")
    sunetpercutieother = forms.CharField(label="Limfonoduri explorabile", help_text="", required=False, widget=forms.Textarea(attrs={'rows': 1, 'cols': 40}))
    altemodificaritoraco2 = forms.CharField(widget=forms.Textarea, label="Alte modificări")
    #examenul cardio-vascular
    dispneecardio = forms.ChoiceField(choices=DISPNEECARDIO, widget=forms.RadioSelect, label="Dispnee")
    dispneecardioother = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 1, 'cols': 40}))
    zgomotulcardiac = forms.ChoiceField(choices=ZGOMOTULCARDIAC, widget=forms.RadioSelect, label="Zgomotul cardiac")
    zgomotulcardiacother = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 1, 'cols': 40}))
    pulsul = forms.ChoiceField(choices=PULSUL, widget=forms.RadioSelect)
    altemodificaricardio = forms.CharField(widget=forms.Textarea, label="Alte modificări")
    #examenul aparatului urinar
    mictiunea = forms.ChoiceField(choices=MICTIUNEA, widget=forms.RadioSelect, label="Micțiunea")
    sensibilitatea = forms.ChoiceField(choices=SENSIBILITATEA, widget=forms.RadioSelect)
    marime = forms.ChoiceField(choices=MARIME, widget=forms.RadioSelect)
    sensibilitateavezicii = forms.ChoiceField(choices=SENSIBILITATEA, widget=forms.RadioSelect, label="Sensibilitatea vezicii")
    graddeplentitudine = forms.ChoiceField(choices=GRADDEPLENTITUDINE, widget=forms.RadioSelect, label="Grad de plentitudine")
    altemodificariurinar = forms.CharField(widget=forms.Textarea, label="Alte modificări")
    #examenul aparatului locomotor
    schiopatura = forms.ChoiceField(choices=SCHIOPATURA, widget=forms.RadioSelect)
    schiopaturaother = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 1, 'cols': 40}))
    aplomburi = forms.ChoiceField(choices=APLOMBURI, widget=forms.RadioSelect)
    tumefacatiiarticulare = forms.ChoiceField(choices=TUMEFACATIIARTICULARE, widget=forms.RadioSelect, label="Tumefacții articulare")
    mobilitatearticulara = forms.ChoiceField(choices=MOBILITATEARTICULARA, widget=forms.RadioSelect, label="Mobilitate articulara")
    durerearticulara = forms.ChoiceField(choices=DUREREARTICULARADIAFIZARA, widget=forms.RadioSelect, label="Durere articulara")
    durerediafizara = forms.ChoiceField(choices=DUREREARTICULARADIAFIZARA, widget=forms.RadioSelect, label="Durere diafizara")
    deficitpropioceptiv = forms.ChoiceField(choices=DEFICITPROPIOCEPTIV, widget=forms.RadioSelect, label="Deficit propioceptiv")
    masamusculara = forms.ChoiceField(choices=MASAMUSCULARA, widget=forms.RadioSelect, label="Masa musculara")
    tonusmuscular = forms.ChoiceField(choices=TONUSMUSCULAR, widget=forms.RadioSelect, label="Tonus muscular")
    #eaxmenul complementar
    examenulcomplementarfield = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 80}), label="Examenul complementar")
    diagnostic = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 80}))
    tratament = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 80}))
    class Meta:
        model = Fisa
        fields = '__all__'
        widgets = {
            'animal': autocomplete.ModelSelect2(url='animal-autocomplete')
        }
