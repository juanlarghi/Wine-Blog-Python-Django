from django.shortcuts import render
from . import models

def home(request):
    query = models.Membresia.objects.all()
    return render(request, 'membresia/index.html', {"membresia": query})
