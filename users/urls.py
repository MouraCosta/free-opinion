"""Users urls"""
from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # Basics users privileges
    path('', include('django.contrib.auth.urls'), name='login'),
    path('register', views.register, name='register')
]
