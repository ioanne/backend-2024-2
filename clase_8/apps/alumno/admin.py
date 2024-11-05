from django.contrib import admin

from apps.alumno.models import Alumno


@admin.action(description="Deshablitar usuario")
def disable_user(modeladmin, request, queryset):
    queryset.update(habilitado=False)
    # Agregar al history de django
    for user in queryset:
        modeladmin.log_change(request, user, "Deshabilitar usuario")


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "apellido", "dni", "fecha_nacimiento"]
    search_fields = ["nombre", "apellido", "dni", "fecha_nacimiento"]
    list_filter = ["fecha_nacimiento"]

    actions = [disable_user]
