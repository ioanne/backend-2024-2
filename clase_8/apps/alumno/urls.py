from django.urls import path

from apps.alumno.views import AlumnoView, DetalleAlumnoView


urlpatterns = [
    path("", AlumnoView.as_view(), name="alumno"),
    path("detalle/<int:pk>/", DetalleAlumnoView.as_view(), name="detalle_alumno"),
]