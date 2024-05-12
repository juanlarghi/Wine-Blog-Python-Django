from django.shortcuts import render
from . import models

#def home(request):
#    consulta_articulos = models.Blog.objects.all().order_by('fecha')
#    context = {'articulos': consulta_articulos}
#    return render(request, 'blog/index.html', context)


def home(request):
    blogs = models.Blog.objects.all().order_by('fecha')
    return render(request, 'blog/index.html', {'blogs': blogs})