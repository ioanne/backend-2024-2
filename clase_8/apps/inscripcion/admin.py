from django.contrib import admin

from apps.inscripcion.models import Inscripcion


@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    pass
