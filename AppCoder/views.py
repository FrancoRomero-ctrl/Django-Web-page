from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.http import HttpResponse
from AppCoder.models import *
from django import forms
from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
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

def leerOpiniones(request):

      comentarios = opinar.objects.all() #trae todos los profesores

      contexto= {"comentarios":comentarios} 

      return render(request, "AppCoder/leerOpiniones.html",contexto)

def eliminarOpiniones(request, comentario_nombre):
 
    comentario = opinar.objects.get(nombre= comentario_nombre)
    comentario.delete()
 
    # vuelvo al menú
    comentarios = opinar.objects.all()  # trae todos los profesores
 
    contexto = {"comentarios": comentarios}
 
    return render(request, "AppCoder/leerOpiniones.html", contexto)


def editarOpiniones(request, comentario_nombre):

    # Recibe el nombre del profesor que vamos a modificar
    comentario = opinar.objects.get(nombre= comentario_nombre)

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':

        # aquí mellega toda la información del html
        miFormulario = opinar(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            comentario.nombre = informacion['nombre']
            comentario.apellido = informacion['apellido']
            comentario.email = informacion['email']
            comentario.opinion = informacion['opinion']

            comentario.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "AppCoder/index.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = opinar(initial={'nombre': comentario.nombre, 'apellido': comentario.apellido,
                                                   'email': comentario.email, 'profesion': comentario.opinion})

    # Voy al html que me permite editar
    return render(request, "AppCoder/editarOpiniones.html", {"miFormulario": miFormulario, "comentario_nombre": comentario_nombre})

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "AppCoder/index.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppCoder/index.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "AppCoder/index.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {"form": form})




from AppCoder.forms import  UserRegisterForm
# Vista de registro
def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/index.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppCoder/registro.html" ,  {"form":form})

from AppCoder.forms import UserRegisterForm, UserEditForm

# Vista de editar el perfil

def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "AppCoder/index.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "AppCoder/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})

   





 



      


