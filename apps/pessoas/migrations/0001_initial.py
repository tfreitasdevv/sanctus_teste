# Generated by Django 5.0.1 on 2024-02-02 02:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("geral", "0001_initial"),
        ("igrejas", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Clero",
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
                ("data_nascimento", models.DateField()),
                ("telefone", models.CharField(max_length=30)),
                ("data_inicio", models.DateField()),
                ("data_saida", models.DateField(blank=True, null=True)),
                (
                    "funcao",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="geral.funcoesclero",
                    ),
                ),
                (
                    "igreja",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="igrejas.igreja"
                    ),
                ),
                (
                    "usuario",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Clero",
                "ordering": ["nome"],
            },
        ),
        migrations.CreateModel(
            name="Funcionario",
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
                ("data_nascimento", models.DateField()),
                ("telefone", models.CharField(max_length=30)),
                ("data_admissao", models.DateField()),
                ("data_demissao", models.DateField(blank=True, null=True)),
                (
                    "funcao",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="geral.funcoesfuncionarios",
                    ),
                ),
                (
                    "igreja",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="igrejas.igreja"
                    ),
                ),
                (
                    "usuario",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Funcionarios",
                "ordering": ["nome"],
            },
        ),
        migrations.CreateModel(
            name="Paroquiano",
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
                ("data_nascimento", models.DateField()),
                ("telefone", models.CharField(max_length=30)),
                ("batizado", models.BooleanField(default=False)),
                ("data_cadastro", models.DateTimeField(auto_now_add=True)),
                (
                    "igreja",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="igrejas.igreja"
                    ),
                ),
                (
                    "usuario",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Paroquianos",
                "ordering": ["nome"],
            },
        ),
    ]
