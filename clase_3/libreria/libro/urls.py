from django.urls import path

from libro.views import libros, libroView

urlpatterns = [
    path("", libros, name="libros"),
    path("vista/", libroView.as_view(), name="libros_vista")
]