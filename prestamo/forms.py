from dataclasses import fields
from django import forms

from equipos.models import Equipos
from .models import Prestamo

class PrestamoForm(forms.ModelForm):
    class Meta:
        model=Prestamo
        fields=('matricula','equipo_id')
        # widgets={'equipo_id':forms.TextInput(attrs={'type': 'text'})}