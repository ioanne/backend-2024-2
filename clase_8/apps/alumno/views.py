from django.views.generic import TemplateView, ListView

from apps.alumno.models import Alumno


class AlumnoView(TemplateView):
    template_name = "lista_alumnos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["alumnos"] = Alumno.objects.all().order_by("-nombre")
        return context


class DetalleAlumnoView(TemplateView):
    template_name = "detalle_alumno.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["alumno"] = Alumno.objects.get(pk=self.kwargs.get("pk"))
        return context
