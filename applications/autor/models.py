from django.db import models

from .managers import AutorManager

class Autor(models.Model):
    nombres = models.CharField( max_length=50)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.CharField( max_length=25)
    edad = models.PositiveBigIntegerField()

    objects = AutorManager()
    
    def __str__(self):
        return str(self.id) + '-' +self.nombres + '-' + self.apellidos
