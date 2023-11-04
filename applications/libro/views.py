from django.shortcuts import render

from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView
# Create your views here.

from .models import Libro

class ListLibros(ListView):
    
    context_object_name = 'lista_libros'
    template_name = 'libro/lista.html'

    def get_queryset(self): 
        palabra_clave = self.request.GET.get("kword", "")


        return Libro.objects.listar_libros(palabra_clave)

