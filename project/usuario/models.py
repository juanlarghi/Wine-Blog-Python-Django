from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=45, verbose_name='país')

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = 'países'

class Usuario(models.Model):
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    pais_origen_id = models.ForeignKey(Pais, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="país de origen")
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.nombre}, {self.apellido}"