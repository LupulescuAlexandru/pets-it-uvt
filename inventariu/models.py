from django.db import models


class Consumabile(models.Model):
    id = models.AutoField(primary_key=True)
    nume = models.CharField(max_length=50)
    cantitate = models.IntegerField()
    class Meta:
        verbose_name="Consumabil"
        verbose_name_plural="Consumabile"
        ordering = ('nume',)
    def __str__(self):
        return self.nume
