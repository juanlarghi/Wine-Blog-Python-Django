from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    path('', views.home, name='home'),
    path('usuario/<int:pk>', views.usuario, name='usuario'),
]
