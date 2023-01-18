from django.urls import path

from AppCoder import views

urlpatterns = [
   
    path('', views.index, name="index"), #este era nuestro primer view

    path('opinion', views.opiniones, name="opinion"),
    path('contact', views.crear_contacto, name= "contact" ),
    path('reservar', views.reserva, name= "reservar" ),
    path('busqueda', views.busquedaContacto, name= "busqueda" ),
    path('buscar/', views.buscar), 
   
]


