from django.db import models

class Autor(models.Model):
    nombre = models.CharField( max_length=50)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models,models.CharField( max_length=50)
    edad = models.PositiveBigIntegerField()

    def __str__(self):
        return self.nombre + '-' + self.apellidos
