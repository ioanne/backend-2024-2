from apps.utils.models import Persona


class Profesor(Persona):

    def __str__(self):
        return f'{self.nombre} {self.apellido}'