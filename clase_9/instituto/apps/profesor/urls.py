from django.urls import path

from apps.profesor.views import ProfesorTemplateView, AltaProfesorCreateView


urlpatterns = [
    path("", ProfesorTemplateView.as_view(), name='profesor'),
    path("alta/", AltaProfesorCreateView.as_view(), name='alta_profesor'),
]
