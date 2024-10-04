from django.contrib import admin

from apps.materia.models import Materia


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    pass