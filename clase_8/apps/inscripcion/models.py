# from datetime import datetime # No es recomendable usar datetime porque no tiene timezone
from django.db import models
from django.utils import timezone


class Inscripcion(models.Model):
    fecha = models.DateField(default=timezone.now)
    carrera = models.ForeignKey("carrera.Carrera", on_delete=models.CASCADE)
    alumno = models.ForeignKey("alumno.Alumno", on_delete=models.CASCADE)
    finalizada = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.alumno} - {self.carrera}"
    

"""
En django podemos usar en default funciones.
La idea es pasarle una función sin ejecutar, es decir, sin (),
para que se ejecute en el momento de la creación del objeto.

Las funciones pueden ser de python o creadas por nosotros

"""