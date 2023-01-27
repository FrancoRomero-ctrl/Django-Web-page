from django.urls import path

from AppCoder import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
   
    path('', views.index, name="index"), #este era nuestro primer view

    path('opinion', views.opiniones, name="opinion"),
    path('contact', views.crear_contacto, name= "contact" ),
    path('reservar', views.reserva, name= "reservar" ),
    path('busqueda', views.busquedaContacto, name= "busqueda" ),
    path('buscar/', views.buscar), 
    path('leerOpiniones', views.leerOpiniones, name= "leerOpiniones"),
    path('eliminarOpiniones/<comentario_nombre>/', views.eliminarOpiniones, name="EliminarOpiniones"),
    path('editarOpiniones/<comentario_nombre>/', views.editarOpiniones, name="EditarOpiniones"),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),

]


