from django.db import models


class Persona(models.Model):
    class Meta:
        abstract = True

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    dni = models.CharField(max_length=8)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    activo = models.BooleanField(default=True)
