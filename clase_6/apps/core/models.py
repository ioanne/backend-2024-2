from django.db import models


class Persona(models.Model):
    class Meta:
        abstract = True

    # Todos los modelos de django tienen un campos id
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=8)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)


# Mas clases en comun