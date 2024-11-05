# Generated by Django 5.1 on 2024-11-01 22:48

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Alumno",
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
                ("apellido", models.CharField(max_length=50)),
                ("edad", models.IntegerField()),
                ("dni", models.CharField(max_length=8)),
                ("telefono", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254)),
                ("fecha_nacimiento", models.DateField()),
                ("activo", models.BooleanField(default=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]