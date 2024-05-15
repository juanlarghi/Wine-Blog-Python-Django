from django.db import models
from usuario.models import Usuario

class Blog(models.Model):
    titulo = models.CharField(max_length=100)
    cuerpo = models.TextField(max_length=3000)
    autor = models.ForeignKey(Usuario, default=None, on_delete=models.SET_NULL, null=True, blank=True)
    fecha = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.titulo
    
    def snippet(self):
        return self.cuerpo[:100]+'...'