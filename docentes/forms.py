from tkinter import Widget
from django import forms
from pkg_resources import require
from .models import Docentes

class DocentesForm(forms.ModelForm):
    class Meta:
        model=Docentes
        fields=('matricula','nombre','apellido','correo','imagen','status')
        # widgets={'duracion_sancion': forms.DateTimeInput(attrs={'type':'datetime-local'})}
        widgets={'status':forms.TextInput(attrs={'min':'0','max':'2','type': 'number'})}