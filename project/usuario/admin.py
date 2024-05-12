from django.contrib import admin

#Registro mi modelo aca

from . import models

admin.site.register(models.Usuario)
admin.site.register(models.Pais)
