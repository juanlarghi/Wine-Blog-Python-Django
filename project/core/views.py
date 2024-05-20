from django.contrib.auth.views import LoginView
from django.shortcuts import render
from . import models
from .forms import CustomAuthenticationForm

def home(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/components/about.html')

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "core/login.html"