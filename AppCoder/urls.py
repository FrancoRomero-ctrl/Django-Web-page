from django.urls import path

from AppCoder import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

   
    path('', views.index, name="index"),
    path('aboutMe', views.aboutMe, name="aboutMe"), 

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
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"), 
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




