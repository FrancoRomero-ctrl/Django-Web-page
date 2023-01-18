from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.http import HttpResponse
from AppCoder.models import *
# Create your views here.



def index(request):

      return render(request, "AppCoder/index.html")


def crear_contacto(request):
      if request.method == "POST":
            data = request.POST
            contacto_nombre = contacto(nombre=data['nname'], apellido=data['lastname'], email=data['mail'], mensaje=data['messaje'])
            contacto_nombre.save()
           
            return render(request, "AppCoder/index.html")
      else: #GET
            return render(request, "AppCoder/contact.html")

def reserva(request):
      if request.method == "POST":
            data = request.POST
            reservar_nombre = reservar(nombre=data['name'], apellido=data['lastname'], email=data['mail'], diaInicio=data['diaInicio'], diaFin= data['diaFin'], mes=data['mes'])
            reservar_nombre.save()
           
            return render(request, "AppCoder/index.html")
      else: #GET
            return render(request, "AppCoder/about.html")

 
def opiniones(request):
      if request.method == "POST":
            data = request.POST
            opinion_nombre = opinar(nombre=data['name'], apellido=data['lastname'], email=data['mail'], opinion=data['opinar'])
            opinion_nombre.save()
           
            return render(request, "AppCoder/index.html")
      else: #GET
            return render(request, "AppCoder/opiniones.html")



def busquedaContacto(request):
      return render(request, "AppCoder/busquedaContacto.html")

def buscar(request):
      if request.GET["nombree"]:
            nombre = request.GET['nombree']
            contactos= contacto.objects.filter(nombre__icontains= nombre )
            return render(request, "AppCoder/resultadoBusqueda.html", {"contacto": contactos, "nombree": nombre})
      else:
            respuesta= "No enviaste datos"
      return HttpResponse(respuesta)



      





 
#def crear_contacto(request):
 
      if request.method == "POST":
 
            miFormulario = contacto(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
                  curso.save()
                  return render(request, "AppCoder/index.html")
      else:
            miFormulario = CursoFormulario()
 
      return render(request, "AppCoder/contact.html", {"miFormulario": miFormulario})


      


