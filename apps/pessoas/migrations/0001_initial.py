# Generated by Django 5.0.1 on 2024-01-30 10:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pessoa",
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
                ("nome", models.CharField(max_length=360)),
                ("cpf", models.CharField(max_length=11, unique=True)),
                (
                    "genero",
                    models.CharField(
                        choices=[("F", "Feminino"), ("M", "Masculino")], max_length=1
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("data_nascimento", models.DateTimeField()),
            ],
        ),
    ]
