from django.contrib import admin

from apps.cursada.models import Cursada


@admin.register(Cursada)
class CursadaAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha_inicio', 'fecha_fin', 'materia__nombre', 'profesor__nombre')
