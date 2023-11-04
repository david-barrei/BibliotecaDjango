from django.db import models
from django.db.models import Q

class LibroManager(models.Manager):
    # Managers para el modelo autor

    def listar_libros(self, kword):

        resultado = self.filter(
            titulo__icontains= kword) # para buscar conicidencias icontains

        return   resultado 



