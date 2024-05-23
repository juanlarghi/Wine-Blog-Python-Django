from django.db import models
from django.contrib.auth.models import User

class Pais(models.Model):
    nombre = models.CharField(max_length=45, verbose_name='país')

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = 'Países'
    
class Provincia(models.Model):
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=45, null=True)
    apellido = models.CharField(max_length=45, null=True)
    direccion = models.CharField(max_length=200, null=True,verbose_name='dirección')
    pais_origen_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="país de origen")
    prov_origen_id = models.ForeignKey(Provincia, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="provincia de origen")
    email = models.EmailField(max_length=100, null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    
    def __str__(self) -> str:
        return f"{self.nombre}, {self.apellido}"