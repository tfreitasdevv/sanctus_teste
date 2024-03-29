# Generated by Django 5.0.1 on 2024-02-06 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnderecoClero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=8)),
                ('logradouro', models.CharField(max_length=200)),
                ('numero', models.CharField(max_length=15)),
                ('complemento', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=360)),
                ('cidade', models.CharField(max_length=360)),
                ('estado', models.CharField(max_length=360)),
            ],
        ),
        migrations.CreateModel(
            name='EnderecoFuncionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=8)),
                ('logradouro', models.CharField(max_length=200)),
                ('numero', models.CharField(max_length=15)),
                ('complemento', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=360)),
                ('cidade', models.CharField(max_length=360)),
                ('estado', models.CharField(max_length=360)),
            ],
        ),
        migrations.CreateModel(
            name='EnderecoIgreja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=8)),
                ('logradouro', models.CharField(max_length=200)),
                ('numero', models.CharField(max_length=15)),
                ('complemento', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=360)),
                ('cidade', models.CharField(max_length=360)),
                ('estado', models.CharField(max_length=360)),
            ],
        ),
        migrations.CreateModel(
            name='EnderecoParoquiano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=8)),
                ('logradouro', models.CharField(max_length=200)),
                ('numero', models.CharField(max_length=15)),
                ('complemento', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=360)),
                ('cidade', models.CharField(max_length=360)),
                ('estado', models.CharField(max_length=360)),
            ],
        ),
        migrations.CreateModel(
            name='FuncoesClero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=360)),
            ],
            options={
                'verbose_name_plural': 'Funções Clero',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='FuncoesFuncionarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=360)),
            ],
            options={
                'verbose_name_plural': 'Funções Funcionários',
                'ordering': ['nome'],
            },
        ),
    ]
