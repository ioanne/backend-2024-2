from django.db import models

from django.db.models import Manager


class CustomManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(cancelado=False)


class Carrito(models.Model):
    usuario = models.ForeignKey("usuario.Usuario", on_delete=models.CASCADE)
    finalizado = models.BooleanField(default=False)
    cancelado = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)

    objects_default = Manager()
    objects = CustomManager()

    def __str__(self):
        return f"{self.id} - {self.usuario.username}"


class Item(models.Model):
    producto = models.ForeignKey("producto.Producto", on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    carrito = models.ForeignKey("carrito.Carrito", on_delete=models.CASCADE, related_name="items")

    def __str__(self):
        return f"{self.id} - {self.producto.nombre} - {self.cantidad}"
