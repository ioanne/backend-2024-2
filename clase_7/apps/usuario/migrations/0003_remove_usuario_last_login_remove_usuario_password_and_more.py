# Generated by Django 5.1 on 2024-09-13 22:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("usuario", "0002_usuario_username"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usuario",
            name="last_login",
        ),
        migrations.RemoveField(
            model_name="usuario",
            name="password",
        ),
        migrations.RemoveField(
            model_name="usuario",
            name="username",
        ),
    ]
