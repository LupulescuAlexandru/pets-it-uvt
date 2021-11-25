from django.db import models

class Proprietar(models.Model):
    nume = models.CharField(max_length=40, null=True)
    adresa = models.CharField(max_length=50, null=True)
    telefon = models.CharField(max_length=15, null=True)
    class Meta:
        verbose_name_plural = "Proprietari"
    def __str__(self):
        return self.nume

class Animal(models.Model):
    nume = models.CharField(max_length=50, null=True)
    microcip = models.CharField(max_length=30, null=True, verbose_name="Cod microcip")
    proprietar = models.ForeignKey(Proprietar, on_delete=models.CASCADE)
    specia = models.CharField(max_length=50, null=True)
    rasa = models.CharField(max_length=50, null=True)
    varstaluni = models.IntegerField(null=True, verbose_name="Varsta (luni)")
    varstaani = models.IntegerField(null=True, verbose_name="Varsta (ani)")
    gender = models.CharField(max_length=10, verbose_name="Sex")
    greutate = models.FloatField(null=True)
    culoare = models.CharField(max_length=20, null=True)
    vaccinarideparazitari = models.CharField(max_length=30, null=True, verbose_name="Vaccinari si deparazitari")
    castrat = models.CharField(max_length=3, null=True)
    mediudeviata = models.CharField(max_length=30, null=True, verbose_name="Mediu de viata")
    anamneza = models.TextField(max_length=500, null=True, verbose_name="Anamneză")
    antecedente = models.TextField(max_length=300, null=True, verbose_name="Antecedente")
    alimentatie = models.CharField(max_length=30, null=True)
    conformatie = models.CharField(max_length=30, null=True)
    constitutie = models.CharField(max_length=30, null=True)
    temperament = models.CharField(max_length=30, null=True)
    atitudine = models.CharField(max_length=30, null=True)
    scorclinic = models.CharField(max_length=30, null=True)
    pielea = models.CharField(max_length=30, null=True)
    altemodificari = models.TextField(max_length=150, null=True)
    parul = models.CharField(max_length=30, null=True)
    parulmodificat = models.CharField(max_length=20, null=True, blank=True)
    limfonoduriexplorabile = models.CharField(max_length=30, null=True)
    limfonoduriexplorabiletextarea = models.TextField(max_length=100, null=True, blank=True)
    mucoaseaferente = models.CharField(max_length=20, null=True)
    temperatura = models.FloatField(null=True, blank=True)
    trc = models.FloatField(blank=True, null=True, verbose_name="TRC")
    frecventarespiratorie = models.FloatField(null=True, blank=True)
    frecventapulsului = models.FloatField(null=True, blank=True)
    class Meta:
        verbose_name_plural = "Animale"
    def __str__(self):
        return self.nume
