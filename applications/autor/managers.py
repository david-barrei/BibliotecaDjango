from django.db import models
from django.db.models import Q

class AutorManager(models.Manager):
    # Managers para el modelo autor

    def buscar_autor(self, kword):

        resultado = self.filter(
            nombre__icontains= kword) # para buscar conicidencias icontains

        return   resultado 

    def buscar_autor2(self, kword):

        resultado = self.filter(
            Q(nombre__icontains= kword) | Q(apellidos__icontains= kword ) 
        )
        return   resultado 
