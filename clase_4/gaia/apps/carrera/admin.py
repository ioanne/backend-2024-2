from django.contrib import admin

from apps.carrera.models import Carrera


@admin.register(Carrera)
class AdminCarrera(admin.ModelAdmin):
    list_display = ('nombre',)
