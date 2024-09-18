from django.db import models


class Usuario(models.Model):
    username = models.CharField(max_length=150, default=None, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.username} - {self.telefono}"

"""
usuario_creado = Usuario.objects.create(username="Pedro", telefono="123456") # Usuario creado
usuario_creado = Usuario(username="Pedro", telefono="123456").save()

usuario_sin_crear = Usuario(username="Pedro", telefono="123456") # Usuario sin crear
usuario_sin_crear.username
usuario_sin_crear.telefono

usuario_sin_crear.save()

diccionario = {
    "username": "Pedro",
    "telefono": "123456"
}
usuario = Usuario(**diccionario)

"""
# def foo(**kwargs):
#     print(kwargs)

# foo(telefono="123456", username="Pedro")

# def foo2(*args):
#     print(args)

# foo2("Pedro", "123456")