from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from . import models
from .forms import CustomAuthenticationForm, CustomUserCreationForm

def home(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/components/about.html')

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "core/login.html"
    
def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            #log the user in
            return render(request, 'core/index.html', {"mensaje": "Usuario creado"})
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/register.html', {"form": form})
    