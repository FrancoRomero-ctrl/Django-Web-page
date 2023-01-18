from django.contrib import admin
from  .models import * #importamos el archivo models

# Register your models here.
#registramos los modelos

admin.site.register(contacto)

admin.site.register(opinar)

admin.site.register(reservar)


