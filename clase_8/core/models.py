from django.db import models


class PersonaModelo(models.Model):
    """Los modelos con Meta abstract True, no son tablas. Son clases de las que se puede heredar para no repetir atributos"""
    class Meta:
        abstract = True

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"