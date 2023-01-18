from django import forms
from AppCoder.models import *

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
    


    
