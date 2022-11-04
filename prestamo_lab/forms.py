from django import forms

from laboratorio.models import Laboratorios
from .models import PrestamoLab

class PrestamoForm(forms.ModelForm):
    class Meta:
        model=PrestamoLab
        fields=('matricula','lab_id')
        # widgets={'equipo_id':forms.TextInput(attrs={'type': 'text'})}