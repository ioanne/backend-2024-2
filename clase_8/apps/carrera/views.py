from django.shortcuts import render

from django.views.generic import TemplateView

from apps.carrera.models import Carrera


class CarreraTemplateView(TemplateView):
    template_name = "carrera.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Esto es un metodo de clase que contiene la query
        carreras = Carrera.obtener_carrera_ingenieria()
        detalle_carreras = [carrera.detalle() for carrera in carreras]
        context['detalle_carreras'] = detalle_carreras
        context['carreras_de_ingenieria'] = carreras

        return context








"""def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    # logica que se ejecuta antes de renderizar el template
    context["clave"] = "Algo"
    return context"""