from django.db import models

# Create your models here.


class Persona(models.Model):

    full_name = models.CharField('nombres', max_length=50)
    pais = models.CharField('Pais', max_length=30)
    pasaporte = models.CharField('Pasaporte', max_length=50)
    edad = models.IntegerField()
    apelativo = models.CharField('Apelativo', max_length=10)

    class Meta:
        verbose_name =("Persona")
        verbose_name_plural = ("Personas")
        db_table = 'persona'
        unique_together = ['pais', 'apelativo']
        constraints = [
            models.CheckConstraint(check=models.Q(edad__gte=18), name='edad_mayor_18')
        ]
        abstract = True # Para que no se cree en la base de datos 


    def __str__(self):
        return self.full_name
    
class Empleados(Persona): #Hereda de el Modelo Persona
    empleo = models.CharField('Empleado', max_length=50)
#Persona 1
class Cliente(Persona): #Hereda de el modelo Persona
    email = models.CharField('Email', max_length=50)
#Perona 1







