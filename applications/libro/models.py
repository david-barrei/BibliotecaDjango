from django.db import models
from django.db.models.signals import post_save

from PIL import Image

from applications.autor.models import Autor

from .managers import LibroManager, CategoriaManager
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField( max_length=50)

    objects = CategoriaManager()
    def __str__(self):
        return str(self.id) +'-' + self.nombre
    
class Libro(models.Model):
   categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria_libro')
   autores = models.ManyToManyField(Autor)
   titulo = models.CharField(max_length=50)
   fecha = models.DateField('Fecha de lanzamiento')
   portada = models.ImageField(upload_to='portada')
   visitas = models.PositiveIntegerField()
   stock = models.PositiveBigIntegerField(default=0) #agregando stock

   objects = LibroManager()

   class Meta:
       verbose_name = 'Libro'
       verbose_name_plural = 'Libros'
       ordering = ['titulo','fecha']


   def __str__(self):
       return str(self.id) + '-' + self.titulo + ' - ' +  str(self.fecha)

def optimize_image(sender, instance, **kwargs): # sender hacia donde se va a enviar
       print("------------")
       if instance.portada:
           portada = Image.open(instance.portada.path) 
           portada.save(instance.portada.path, quality=20, optimize=True) # Para optimizar la imagen
       
post_save.connect(optimize_image, sender= Libro)