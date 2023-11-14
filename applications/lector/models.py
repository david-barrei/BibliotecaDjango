from django.db import models
from applications.libro.models import Libro
from .managers import PrestamoManager
from applications.autor.models import Persona

# Create your models here.



class Lector(Persona):
    
    class Meta:
        verbose_name = 'Lector'
        verbose_name_plural = 'Lectores'


class Prestamo(models.Model):
   lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
   libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='libro_prestamo')
   fecha_devolucion = models.DateField(blank=True, null=True)
   devuelto = models.BooleanField()

   objects = PrestamoManager()

   def __str__(self):
       return  str(self.id) + '-' + self.libro.titulo
   
   