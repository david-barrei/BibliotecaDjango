from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import PrestamoForm
from .models import Prestamo
# Create your views here.

class RegistarPrestamo(FormView):
    template_name = 'lector/add_prestamo.html'
    form_class = PrestamoForm
    success_url = '.'

    def form_valid(self, form):


        return super(RegistarPrestamo, self).form_valid(form) 
