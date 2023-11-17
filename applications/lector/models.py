from django.db import models
from django.db.models.signals import post_delete

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

   def save(self, *args, **kwargs):
        self.libro.stock = self.libro.stock -1 #Desminuir stock
        self.libro.save()
        super(Prestamo, self).save(*args, **kwargs)

   def __str__(self):
       return  str(self.id) + '-' + self.libro.titulo
   

def update_libro_stok(sender, instance, **kwargs): #si se devuelve el libro suma el stock
    instance.libro.stock = instance.libro.stock + 1
    instance.libro.save()

post_delete.connect(update_libro_stok, sender = Prestamo)