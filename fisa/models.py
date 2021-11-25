from django.db import models
from animal.models import Animal
from inventariu.models import Consumabile

class Fisa(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, null=True)
    data = models.DateField(null=True)
    #examinarea aparatului digestiv
    apetit = models.CharField(max_length=30, null=True, blank=True)
    consumulvoluntardeapa = models.CharField(max_length=15, null=True, blank=True, verbose_name="Consumul voluntar de apa")
    prehensiunea = models.CharField(max_length=30, null=True, blank=True)
    masticatia = models.CharField(max_length=30, null=True, blank=True)
    deglutitia = models.CharField(max_length=30, null=True, blank=True)
    voma = models.CharField(max_length=30, null=True, blank=True)
    defecarea = models.CharField(max_length=30, null=True, blank=True)
    examenulcavitatiiorale = models.CharField(max_length=30, null=True, blank=True, verbose_name="Examenul cavitatii orale")
    examenulcavitatiioraleother = models.TextField(max_length=100, null=True, blank=True)
    examenulfaringului = models.CharField(max_length=30, null=True, blank=True)
    examenulfaringuluiother = models.TextField(max_length=100, null=True, blank=True)
    examenulesofagului = models.CharField(max_length=30, null=True, blank=True)
    examenulesofaguluiother = models.TextField(max_length=100, null=True, blank=True)
    examenulabdomenului = models.CharField(max_length=30, null=True, blank=True)
    examenulabdomenuluiother = models.TextField(max_length=100, null=True, blank=True)
    examenulstomacului = models.CharField(max_length=30, null=True, blank=True)
    examenulstomaculuiother = models.TextField(max_length=100, null=True, blank=True)
    examenulintestinelor = models.CharField(max_length=30, null=True, blank=True)
    examenulintestinelorother = models.TextField(max_length=100, null=True, blank=True)
    examenulanusului = models.CharField(max_length=30, null=True, blank=True)
    examenulanusuluiother = models.TextField(max_length=100, null=True, blank=True)
    examenulfecalelor = models.CharField(max_length=30, null=True, blank=True)
    examenulfecalelorother = models.TextField(max_length=100, null=True, blank=True)
    eaxmenulglanexe = models.CharField(max_length=30, null=True, blank=True)
    eaxmenulglanexeother = models.TextField(max_length=100, null=True, blank=True)
    examenulglsalivare = models.CharField(max_length=30, null=True, blank=True)
    examenulglsalivareother = models.TextField(max_length=100, null=True, blank=True)
    ariahepatica = models.CharField(max_length=30, null=True, blank=True)
    ariapancreatica = models.CharField(max_length=30, null=True, blank=True)
    #examinarea aparatului respirator
    tuse = models.CharField(max_length=30, null=True, blank=True)
    jetaj = models.CharField(max_length=30, null=True, blank=True)
    mirosulaparatuluiexpirat = models.CharField(max_length=30, null=True, blank=True)
    mirosulaparatuluiexpiratother = models.TextField(max_length=100, null=True, blank=True)
    cornaj = models.CharField(max_length=30, null=True, blank=True)
    examenulnasului = models.CharField(max_length=30, null=True, blank=True)
    examenulnasuluiother = models.TextField(max_length=100, null=True, blank=True)
    examenulsinusului = models.CharField(max_length=30, null=True, blank=True)
    examenulsinusuluiother = models.TextField(max_length=100, null=True, blank=True)
    examenullaringelui = models.CharField(max_length=30, null=True, blank=True)
    examenullaringeluiother = models.TextField(max_length=100, null=True, blank=True)
    examenultraheei = models.CharField(max_length=30, null=True, blank=True)
    examenultraheeiother = models.TextField(max_length=100, null=True, blank=True)
    #examenul toraco-respirator
    tipulrespiraor = models.CharField(max_length=30, null=True, blank=True)
    dispnee = models.CharField(max_length=30, null=True, blank=True)
    murmurvezicular = models.CharField(max_length=30, null=True, blank=True)
    raluriuscate = models.CharField(max_length=30, null=True, blank=True)
    raluriumede = models.CharField(max_length=30, null=True, blank=True)
    sufluri = models.TextField(max_length=150, null=True, blank=True)
    sunetpercutie = models.CharField(max_length=30, null=True, blank=True)
    sunetpercutieother = models.TextField(max_length=150, null=True, blank=True)
    altemodificaritoraco2 = models.TextField(max_length=150, null=True, blank=True)
    #examenul aparatului cardio-vascular
    dispneecardio = models.CharField(max_length=30, null=True, blank=True)
    dispneecardioother = models.TextField(max_length=150, null=True, blank=True)
    zgomotulcardiac = models.CharField(max_length=30, null=True, blank=True)
    zgomotulcardiacother = models.TextField(max_length=150, blank=True, null=True)
    altemodificaricardio = models.TextField(max_length=150, blank=True, null=True)
    pulsul = models.CharField(max_length=30, null=True, blank=True)
    #examenul aparatului urinar
    mictiunea = models.CharField(max_length=30, null=True, blank=True)
    #examenul rinichilor
    sensibilitatea = models.CharField(max_length=30, null=True, blank=True)
    marime = models.CharField(max_length=30, null=True, blank=True)
    #examenul vezicii urinare
    sensibilitateavezicii = models.CharField(max_length=30, null=True, blank=True)
    graddeplentitudine = models.CharField(max_length=30, null=True, blank=True)
    altemodificariurinar = models.TextField(max_length=150, null=True, blank=True)
    #examenul aparatului locomotor
    schiopatura = models.CharField(max_length=30, null=True, blank=True)
    schiopaturaother = models.TextField(max_length=150, null=True, blank=True)
    aplomburi = models.CharField(max_length=30, null=True, blank=True)
    tumefacatiiarticulare = models.CharField(max_length=30, null=True, blank=True)
    mobilitatearticulara = models.CharField(max_length=30, null=True, blank=True)
    durerearticulara = models.CharField(max_length=30, null=True, blank=True)
    durerediafizara = models.CharField(max_length=30, null=True, blank=True)
    deficitpropioceptiv = models.CharField(max_length=30, null=True, blank=True)
    masamusculara = models.CharField(max_length=30, null=True, blank=True)
    tonusmuscular = models.CharField(max_length=30, null=True, blank=True)
    #examenul complementar
    examenulcomplementarfield = models.TextField(max_length=500, null=True, blank=True)
    diagnostic = models.TextField(max_length=500, null=True, blank=True)
    tratament = models.TextField(max_length=500, null=True, blank=True)
    consumabilefolosite = models.ManyToManyField(Consumabile, through='ConsumabileFisa', blank=True, null=True)
    #send_notification = models.IntegerField(max_length=1, null=True, blank=True, default=0)

    class Meta:
        verbose_name_plural = "Fise"
    def __str__(self):
        return "Fisa" + " " + str(self.animal)

class ConsumabileFisa(models.Model):
    events = models.ForeignKey(Fisa, on_delete=models.CASCADE, null=True, blank=True)
    consumabile = models.ForeignKey(Consumabile, on_delete=models.CASCADE, null=True, blank=True)
    cantitate = models.IntegerField(null=True, blank=True)
    class Meta:
        verbose_name = 'Consumabile'
        verbose_name_plural = 'Consumabile'

    def reset(self):
        print("blabla")
        super(ConsumabileFisa, self).save()

    def save(self):
        Consumabile.objects.filter(nume=str(self.consumabile.nume)).update(cantitate=self.consumabile.cantitate - self.cantitate)
        super(ConsumabileFisa, self).save()

    def __str__(self):
        return self.consumabile.nume
