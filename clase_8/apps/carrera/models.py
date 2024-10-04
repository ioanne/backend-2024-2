from django.db import models


class Carrera(models.Model):
    nombre = models.CharField(max_length=50)
    duracion = models.PositiveIntegerField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
