from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistroForm(UserCreationForm):
    email=forms.EmailField(label='Email')
    username=forms.CharField(min_length=4, max_length=10,label='Usuario')
    first_name=forms.CharField(min_length=2,max_length=100,label='Nombre')
    last_name=forms.CharField(min_length=2,max_length=100,label='Apellido')
    password1= forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2= forms.CharField(label='Confirmar Contraseña',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']
        help_text={k:"" for k in fields}
