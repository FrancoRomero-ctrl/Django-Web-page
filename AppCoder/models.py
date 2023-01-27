from django.db import models

# Create your models here.
class contacto(models.Model):

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    mensaje= models.CharField(max_length=400)
    



class reservar(models.Model):
    nombre= models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    diaInicio=models.IntegerField(max_length=2)
    diaFin=models.IntegerField(max_length=2)
    mes=models.IntegerField(max_length=2)
    

class opinar(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    opinion= models.CharField(max_length=400)
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email} - opinion {self.opinion}"
    


    
