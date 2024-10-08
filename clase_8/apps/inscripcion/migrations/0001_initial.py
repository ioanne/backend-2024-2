# Generated by Django 5.1 on 2024-10-04 22:16

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("alumno", "0001_initial"),
        ("carrera", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Inscripcion",
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
                ("fecha", models.DateField(default=django.utils.timezone.now)),
                ("finalizada", models.BooleanField(default=False)),
                (
                    "alumno",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="alumno.alumno"
                    ),
                ),
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
