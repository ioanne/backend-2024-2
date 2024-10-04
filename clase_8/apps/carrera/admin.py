from django.contrib import admin

from apps.carrera.models import Carrera


@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    pass
