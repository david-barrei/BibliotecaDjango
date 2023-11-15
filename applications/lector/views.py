from datetime import date
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from .forms import PrestamoForm
from .models import Prestamo
# Create your views here.

class RegistarPrestamo(FormView):
    template_name = 'lector/add_prestamo.html'
    form_class = PrestamoForm
    success_url = '.'

    def form_valid(self, form):
        Prestamo.objects.create(
            lector=form.cleaned_data['lector'],
            libro=form.cleaned_data['libro'],
            fecha_devolucion=date.today(),
            devuelto=False
            
        )
        # libro = form.cleaned_data['libro']
        # libro.stock = libro.stock - 1      #Desminuir el stock
        # libro.save()

        return super(RegistarPrestamo, self).form_valid(form) 

class AddPrestamo(FormView):
    template_name = 'lector/add_prestamo.html'
    form_class = PrestamoForm
    success_url = '.'

    def form_valid(self, form):

        obj, created = Prestamo.objects.get_or_create( # Si existe no crea lo recupera si no lo crea 
            lector = form.cleaned_data['lector'],
            libro = form.cleaned_data['libro'],
            devuelto = False,
            defaults = {
                   'fecha_devolucion': date.today()       
            }
        )
        if created:
            return super(AddPrestamo, self).form_valid(form)
        else:
            return HttpResponseRedirect('/')
