from django.contrib import admin

from apps.carrito.models import Carrito, Item

@admin.register(Carrito)
class AdminCarrito(admin.ModelAdmin):
    list_display = ["id", "usuario", "finalizado", "cancelado", "creado",]



@admin.register(Item)
class AdminItem(admin.ModelAdmin):
    list_display = ["id", "producto", "cantidad", "carrito",]
