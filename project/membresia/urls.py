from django.urls import path
from . import views

app_name = 'membresia'

urlpatterns = [
    path('', views.home, name='home'),
]