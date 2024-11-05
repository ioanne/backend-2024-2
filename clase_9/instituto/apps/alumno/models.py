from apps.utils.models import Persona


class Alumno(Persona):

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
