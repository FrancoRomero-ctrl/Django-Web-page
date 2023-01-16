from django import forms
from AppCoder.models import *
class Formulario(forms.Form):

    Nombre = forms.CharField()
    Email = forms.CharField()
    Subject = forms.CharField()
    Messaje= forms.CharField()
    