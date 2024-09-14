# Generated by Django 5.1 on 2024-09-06 22:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("alumno", "0001_initial"),
        ("carrera", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cursada",
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
                ("fecha_inscripcion", models.DateField()),
                ("activa", models.BooleanField(default=True)),
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