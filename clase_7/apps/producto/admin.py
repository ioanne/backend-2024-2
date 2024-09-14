from django.contrib import admin

from apps.producto.models import Producto


@admin.register(Producto)
class AdmninProducto(admin.ModelAdmin):
    list_display = ["nombre", "precio",]
