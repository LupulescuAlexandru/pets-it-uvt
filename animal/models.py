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

    class Meta:
        verbose_name_plural = "Animale"
    def __str__(self):
        return self.nume



