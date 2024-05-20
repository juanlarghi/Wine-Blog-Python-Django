from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('login/', views.CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(template_name="core/logout.html"), name = 'logout'),
] 