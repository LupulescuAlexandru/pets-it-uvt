from django import forms
from .models import Consumabile

class ConsumabileForm(forms.ModelForm):
    model = Consumabile