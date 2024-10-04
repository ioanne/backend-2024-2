from django.db import models

from core.models import PersonaModelo


class Alumno(PersonaModelo):
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
