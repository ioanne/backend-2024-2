from django.db import models


class Carrera(models.Model):
    nombre = models.CharField(max_length=50)
    duracion = models.PositiveIntegerField()
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre