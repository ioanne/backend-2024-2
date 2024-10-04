from django.db import models


class Cursada(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cupo = models.PositiveIntegerField()
    profesor = models.ForeignKey("profesor.Profesor", on_delete=models.CASCADE, related_name="cursadas")
    materia = models.ForeignKey("materia.Materia", on_delete=models.CASCADE, related_name="cursadas")


class Cursando(models.Model):
    cursada = models.ForeignKey("cursada.Cursada", on_delete=models.CASCADE)
    alumno = models.ForeignKey("alumno.Alumno", on_delete=models.CASCADE)
