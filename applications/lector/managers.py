import datetime

from django.db import models
from django.db.models import Q, Count, Avg


class PrestamoManager(models.Manager):

    def libros_promedio_edades(self):
        resultado = self.filter(
            libro__id='1'
        ).aggregate(
            promedio_edad=Avg('lector__edad')
        )
        return resultado



