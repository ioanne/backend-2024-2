from django.contrib import admin

from apps.alumno.models import Alumno


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido')
    search_fields = ('nombre', 'apellido')
    list_filter = ('nombre', 'apellido')
