from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]
    

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    apellido = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    
    class Meta:
        model = User
        fields = ["username", "nombre", "apellido", "email", "password1", "password2"]
        help_text = {k: "" for k in fields}
        
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'