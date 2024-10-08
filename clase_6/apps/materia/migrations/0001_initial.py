# Generated by Django 5.1 on 2024-09-06 22:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("carrera", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Materia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50)),
                (
                    "carrera",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="carrera.carrera",
                    ),
                ),
            ],
        ),
    ]
