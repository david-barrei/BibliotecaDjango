from django.db import models
from applications.libro.models import Libro
from .managers import PrestamoManager

# Create your models here.

class Lector(models.Model):
    nombre = models.CharField( max_length=50)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=25)
    edad = models.IntegerField(default=0)

    def __str__(self):
        return  str(self.id) + '-' + self.nombre + '-' + self.apellidos

class Prestamo(models.Model):
   lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
   libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='libro_prestamo')
   fecha_devolucion = models.DateField(blank=True, null=True)
   devuelto = models.BooleanField()

   objects = PrestamoManager()

   def __str__(self):
       return  str(self.id) + '-' + self.libro.titulo
   
   