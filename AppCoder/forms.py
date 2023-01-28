from django import forms
from AppCoder.models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class contacto(forms.Form):

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    mensaje= models.CharField(max_length=400)


class reservar(forms.Form):
    nombre= models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    diaInicio=models.IntegerField(max_length=2)
    diaFin=models.IntegerField(max_length=2)
    mes=models.IntegerField(max_length=2)
    

class opinar(forms.Form):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    opinion= models.CharField(max_length=400)
    
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

# Clase 24, agregamos el UserEditForm
class UserEditForm(UserCreationForm):

    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repetir la contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']




    
