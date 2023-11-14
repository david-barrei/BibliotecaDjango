from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('lector/add', views.RegistarPrestamo.as_view(), name="prestamo-add"),
   
]



