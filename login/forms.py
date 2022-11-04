from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegistroForm(UserCreationForm):
    email=forms.EmailField(
        label='Email', 
        widget=(forms.EmailInput(attrs={'class':'form-control'}))
    )

    username=forms.CharField(
        min_length=4, 
        max_length=10,
        label='Usuario', 
        widget=(forms.TextInput(attrs={'class':'form-control'}))
    )

    first_name=forms.CharField(
        min_length=2,
        max_length=100,
        label='Nombre', 
        widget=(forms.TextInput(attrs={'class':'form-control'}))
    )

    last_name=forms.CharField(
        min_length=2,
        max_length=100,
        label='Apellido', 
        widget=(forms.TextInput(attrs={'class':'form-control'}))
    )

    password1= forms.CharField(
        label='Contraseña', 
        widget=(forms.PasswordInput(attrs={'class':'form-control'})),
    )

    password2= forms.CharField(
        label='Confirmar Contraseña', 
        widget=(forms.PasswordInput(attrs={'class':'form-control'})),
    )

    is_superuser=forms.IntegerField(
        label='Administrador', 
        widget=(forms.Select(attrs={'class':'form-control'}, choices=[(0,'No'),(1,'Si')]))
    )

    is_staff=forms.IntegerField(
        label='Administrador', 
        widget=(forms.Select(attrs={'class':'form-control'}, choices=[(0,'No'),(1,'Si')]))
    )

    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2','is_superuser','is_staff']
        # help_text={k:"" for k in fields}

    def clean_password2(self):
        password1=self.cleaned_data['password1']
        password2=self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')

    def clean_email(self):
        email=self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Ya existe un usuario con este correo')
        return email

    def clean_username(self):
        username=self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Ya existe un usuario con este nombre')
        return username

