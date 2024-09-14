# Generated by Django 5.1 on 2024-09-13 23:32

import django.db.models.deletion
import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("carrito", "0002_carrito_cancelado_carrito_creado_carrito_finalizado"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="carrito",
            managers=[
                ("objects_default", django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name="item",
            name="carrito",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="carrito.carrito",
            ),
        ),
    ]