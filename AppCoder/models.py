from django.db import models

# Create your models here.
class Nombre(models.Model):

    nombre=models.CharField(max_length=40)
    
class Email(models.Model):
    nombre= models.CharField(max_length=40)
    

class Subject(models.Model):
    nombre= models.CharField(max_length=40)
    

class Messaje(models.Model):
    nombre= models.CharField(max_length=300)
    
