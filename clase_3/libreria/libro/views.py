from django.shortcuts import render

from django.http import HttpResponse
from django.views import View


def libros(request):
    # Hacer algo
    # Hacer otra cosa
    return HttpResponse("Mensaje!") # Devuelve un objeto de tipo HttpResponse


class MiVistaCustom(View):
    pass


class libroView(MiVistaCustom):
    def get(self, request, *args, **kwargs):

        return render(request)

    # def post():
