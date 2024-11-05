from django.urls import path

from apps.profesor.views import ProfesorTemplateView


urlpatterns = [
    path("", ProfesorTemplateView.as_view(), name='profesor'),
]
