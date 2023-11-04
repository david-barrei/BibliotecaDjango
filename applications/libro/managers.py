import datetime
from django.db import models
from django.db.models import Q

class LibroManager(models.Manager):
    # Managers para el modelo autor

    def listar_libros(self, kword):

        resultado = self.filter(
            titulo__icontains= kword,
            fecha__range=('2010-10-10','2015-10-10'))

        return resultado 
    
    def listar_libros2(self, kword, fecha1, fecha2):
        date1 = datetime.datetime.strptime(fecha1, '%Y-%m-%d').date()
        date2 = datetime.datetime.strptime(fecha2, '%Y-%m-%d').date()

        resultado = self.filter(
            titulo__icontains= kword,
            fecha__range=(date1,date2))
        
        return resultado 
    
    def listar_libros_categoria(self, categoria):

        return self.filter(categoria__id=categoria).order_by('titulo')



