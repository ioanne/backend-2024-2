from django.contrib import admin

from apps.cursada.models import Cursada, Cursando


@admin.register(Cursada)
class CursadaAdmin(admin.ModelAdmin):
    pass


@admin.register(Cursando)
class CursandoAdmin(admin.ModelAdmin):
    pass
