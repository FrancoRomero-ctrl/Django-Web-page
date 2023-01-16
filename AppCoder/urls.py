from django.urls import path

from AppCoder import views

urlpatterns = [
   
    path('', views.index, name="index"), #este era nuestro primer view
    path('about', views.about, name="about"),
    path('contact', views.crear_contacto, name= "contact" ),
    
   
]


