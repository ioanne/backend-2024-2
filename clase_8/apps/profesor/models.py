from django.db import models

from core.models import PersonaModelo


class Profesor(PersonaModelo):
    titulo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"