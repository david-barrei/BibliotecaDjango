from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.

from .models import Autor

class ListAutores(ListView):
    
    context_object_name = 'lista_autores'
    template_name = 'autor/lista.html'

    def get_queryset(self): 

        
        return Autor.objects.all()
