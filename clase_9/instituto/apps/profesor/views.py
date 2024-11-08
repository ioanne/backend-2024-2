from typing import Any
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView

from apps.profesor.models import Profesor
from apps.profesor.forms import ProfesorForm


class ProfesorTemplateView(TemplateView):
    template_name = 'profesores.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['profesores'] = Profesor.objects.all()
        return context


class AltaProfesorCreateView(CreateView):
    model = Profesor
    form_class = ProfesorForm
    template_name = 'alta_profesor.html'
    success_url = reverse_lazy('profesor')
