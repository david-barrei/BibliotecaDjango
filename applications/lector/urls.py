from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('lector/add', views.AddPrestamo.as_view(), name="prestamo-add"),
   
]



