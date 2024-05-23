from django.db import models

class Membresia(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=1000)
    beneficio1 = models.TextField(max_length=1000, blank=True, null=True)
    beneficio2 = models.TextField(max_length=1000, blank=True, null=True)
    precio = models.IntegerField(default=100000)
    
    def __str__(self) -> str:
        return self.nombre
    
    #def formato_precio(self) -> str:
    #    return "${self.precio:.2f}"

#class Membresia_usuario(models.Model):
#    SELECT = (Membresia.nombre)
#    
#    usuario = models.ForeignKey