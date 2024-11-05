from django.db import models


class Cursada(models.Model):
    materia = models.ForeignKey('materia.Materia', on_delete=models.CASCADE)
    profesor = models.ForeignKey('profesor.Profesor', on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()