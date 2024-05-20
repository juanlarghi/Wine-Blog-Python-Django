from django.shortcuts import render
from . import models

def home(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/components/about.html' )