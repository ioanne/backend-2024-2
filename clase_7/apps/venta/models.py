from django.db import models


class Venta(models.Model):
   usuario = models.ForeignKey("usuario.Usuario", on_delete=models.CASCADE)


class DetalleVenta(models.Model):
    producto = models.ForeignKey("producto.Producto", on_delete=models.CASCADE)
    venta = models.ForeignKey("venta.Venta", on_delete=models.CASCADE)
    carrito = models.ForeignKey("carrito.Carrito", on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()




"""
Usuario

Producto

Carrito
    Usuario
    Items
        Producto
        cantidad

Venta
    Usuario
    DetalleVenta
        Producto
        cantidad
        Venta
    Carrito

"""