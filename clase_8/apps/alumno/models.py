from django.db import models

from core.models import PersonaModelo


class Alumno(PersonaModelo):

    habilitado = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
