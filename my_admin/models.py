'''
from django.db import models
from fisa.models import Fisa

class modificare_req(models.Model):
    requestfisa = models.ForeignKey(Fisa, on_delete=models.CASCADE, verbose_name="Denumire fisa")
    class Meta:
        verbose_name = "Solicitare"
        verbose_name_plural = "Solicitari"
'''
