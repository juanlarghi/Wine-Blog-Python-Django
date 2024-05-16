from django.db import models

class Membresia(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=3000)
    precio = models.FloatField()
    
    def __str__(self) -> str:
        return self.nombre
    
    #def currency_format(precio):
    #    return '${:.,2f}'.format(precio)

