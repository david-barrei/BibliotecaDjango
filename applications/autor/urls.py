
from django.contrib import admin
from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('autores/', views.ListAutores.as_view(), name="autores"),
   
]


