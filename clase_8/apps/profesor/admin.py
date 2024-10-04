from django.contrib import admin

from apps.profesor.models import Profesor


@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    pass