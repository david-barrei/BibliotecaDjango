from django.contrib import admin
from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('libros/', views.ListLibros.as_view(), name="libros"),
   
]
