from django.urls import path

from libro.views import libros, libroView

urlpatterns = [
    path("", libros, name="libros"),
    path("vista/", libroView.as_view(), name="libros_vista")
]


"""

Desde un navegador llamamos a una URL.
ienes buscan controla/https

dominio local: localhost
ip: 127.0.0.1

protocolo:dominio.algo:puerto



https://<dominio>
Ej:
https://google.com
"""