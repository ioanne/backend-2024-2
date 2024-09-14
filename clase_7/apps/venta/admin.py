from django.contrib import admin

from apps.venta.models import Venta, DetalleVenta


@admin.register(Venta)
class AdminVenta(admin.ModelAdmin):
    list_display = ["usuario",]


@admin.register(DetalleVenta)
class AdminVentaDetalle(admin.ModelAdmin):
    list_display = ["producto", "cantidad", "venta",]