from django.db import models


class Materia(models.Model):
    nombre = models.CharField(max_length=50)
    # Relacion uno a muchos
    carrera = models.ForeignKey('carrera.Carrera', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
