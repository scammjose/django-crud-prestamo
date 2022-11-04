from django import forms
from .models import Laboratorios

class LaboratoriosForm(forms.ModelForm):
    class Meta:
        model=Laboratorios
        fields=('imagen','nombre','status')
        # widgets={'duracion_sancion': forms.DateTimeInput(attrs={'type':'datetime-local'})}
        