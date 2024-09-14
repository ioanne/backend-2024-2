# Generated by Django 5.1 on 2024-09-13 22:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("carrito", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="carrito",
            name="cancelado",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="carrito",
            name="creado",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="carrito",
            name="finalizado",
            field=models.BooleanField(default=False),
        ),
    ]