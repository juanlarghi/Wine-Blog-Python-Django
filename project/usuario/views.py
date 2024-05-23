from django.shortcuts import render
from . import models


def home(request):
    return render(request, 'usuario/index.html')

def usuario(request, pk):
    usuario = models.Usuario.objects.get(id=pk)
    return render(request, 'usuario/index.html', context={"usuarios": usuario})

#def profile(request, pk):
#    profile = models.Usuario.objects.get(id=pk)
#    return render(request, 'usuario/index.html', {'profiles': profile})

