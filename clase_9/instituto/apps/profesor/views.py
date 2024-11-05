from typing import Any
from django.views.generic import TemplateView

from apps.profesor.models import Profesor


class ProfesorTemplateView(TemplateView):
    template_name = 'profesores.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['profesores'] = Profesor.objects.all()
        return context
