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


"""
'SELECT "carrito_item"."id", "carrito_item"."producto_id", "carrito_item"."cantidad", "carrito_item"."carrito_id" FROM "carrito_item" INNER JOIN "carrito_carrito" ON ("carrito_item"."carrito_id" = "carrito_carrito"."id") INNER JOIN "usuario_usuario" ON ("carrito_carrito"."usuario_id" = "usuario_usuario"."id") WHERE ("carrito_carrito"."finalizado" AND "usuario_usuario"."username" = Pedro)'

Item.objects.filter(carrito__usuario__username="Pedro", carrito__finalizado=True)

filter
    Lo que coincide
exclude
    Lo que no coincide
get
    Solo un resultado
delete
    Eliminar
all
    Todos
first
    Primer resultado
last
    Ultimo resultado
count
    Cantidad de resultados
exists
    Si existe o no

<QuerySet [<Producto: 1 - Celular - $1000.00>, <Producto: 3 - Cargador - $100.00>]>
>>> Producto.objects.all().delete()


>>> Usuario.objects.filter(username="Pedro")
<QuerySet [<Usuario: 2 - Pedro - 12312>]>
>>> pedro = _
>>> pedro.delete()
(4, {'carrito.Item': 2, 'carrito.Carrito': 1, 'usuario.Usuario': 1})

"""

