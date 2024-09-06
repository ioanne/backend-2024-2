from django.db import models

from apps.core.models import Persona


class Alumno(Persona):
    # Todos los modelos de django tienen un campos id
    email = models.EmailField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
