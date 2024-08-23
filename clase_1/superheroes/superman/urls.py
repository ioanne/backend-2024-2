from django.urls import path

from superman.views import SupermanTemplateView

urlpatterns = [
    path("", SupermanTemplateView.as_view()), # /superman/ --> localhost:8000/superman/
]