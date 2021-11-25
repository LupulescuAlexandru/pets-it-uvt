from django.db import models
from animal.models import Animal

class consultatie(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    dataconsultatie = models.DateField(null=True, verbose_name="Dată consultație")
    oraconsultatie = models.TimeField(null=True, verbose_name="Oră consultație")
    tratamente = models.TextField(max_length=1000, null=True)
    def __str__(self):
        return "Consultatie" + str(self.animal)
    class Meta:
        verbose_name = "Consultație"
        verbose_name_plural = "Consultații"
