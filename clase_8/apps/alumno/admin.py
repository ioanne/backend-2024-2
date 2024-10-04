from django.contrib import admin

from apps.alumno.models import Alumno


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "apellido", "dni", "fecha_nacimiento"]
    search_fields = ["nombre", "apellido", "dni"]
    list_filter = ["fecha_nacimiento"]
