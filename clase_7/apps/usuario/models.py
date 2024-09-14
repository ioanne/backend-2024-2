from django.db import models


class Usuario(models.Model):
    username = models.CharField(max_length=150, default=None, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.username} - {self.telefono}"