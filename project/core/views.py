from django.contrib.auth.views import LoginView
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.shortcuts import render, redirect
from . import models
from .forms import CustomAuthenticationForm, CustomUserCreationForm

def home(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/components/about.html')

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "core/login.html"
    
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            #user signup
            form.save()
            messages.success(request, f'Cuenta creada exitosamente! Ya puedes iniciar sesión!')
            return redirect("core:login")
        else:    
            return render(request, 'core/index.html')
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/register.html', {"form": form})
    