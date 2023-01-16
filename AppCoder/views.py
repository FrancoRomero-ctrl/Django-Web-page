from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.http import HttpResponse
from AppCoder.models import Nombre, Email, Subject, Messaje
from AppCoder.forms import Formulario
# Create your views here.


def index(request):

      return render(request, "AppCoder/index.html")

def about(request):

      return render(request, "AppCoder/about.html")

#def contact(request):
      #return render(request, "AppCoder/contact.html")

#def contactar(request):
      #return render(request, "AppCoder/contact.html")

from AppCoder.forms import Formulario
 
#def respuestaFormulario(request):
 
      #if request.method == "POST":
 
           # miFormulario = Formulario(request.POST) # Aqui me llega la informacion del html
            #print(miFormulario)
 
            #if miFormulario.is_valid:
                  #informacion = miFormulario.cleaned_data
                  #Usuario = Formulario(Nombre=informacion["name"], Email=informacion["mail"], Subject=informacion["subject"], Messaje= informacion["messaje"])
                  #Usuario.save()
                  #return render(request, "AppCoder/index.html")
      #else:
            #miFormulario = Formulario()
 
      #return render(request, "AppCoder/contact.html", {"Formulario": miFormulario})

def crear_contacto(request):
      if request.method == "POST":
            data = request.POST
            contacto_nombre = Nombre(nombre=data['name'])
            contacto_nombre.save()
            contacto_email = Email(nombre=data['mail'])
            contacto_email.save()
            contacto_subject = Subject(nombre=data['subject'])
            contacto_subject.save()
            contacto_messaje= Messaje(nombre=data['messaje'])
            contacto_messaje.save()
            return render(request, "AppCoder/index.html")
      else: #GET
            return render(request, "AppCoder/contact.html")



 

 


      


