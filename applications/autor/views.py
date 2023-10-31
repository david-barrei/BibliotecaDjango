from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.

from .models import Autor

class ListAutores(ListView):
    model = Autor
    
    template_name = 'autor/lista.html'

