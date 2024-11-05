from django.contrib import admin

from apps.alumno import models


@admin.register(models.Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'dni', 'email')
    search_fields = ('nombre', 'apellido', 'dni', 'email')
