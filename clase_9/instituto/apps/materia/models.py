from django.db import models


class Materia(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
