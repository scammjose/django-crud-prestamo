from django import forms
from .models import Equipos

class EquiposForm(forms.ModelForm):
    class Meta:
        model=Equipos
        fields=('imagen','nombre','codigo','status','categoria')
        # widgets={'duracion_sancion': forms.DateTimeInput(attrs={'type':'datetime-local'})}
        
