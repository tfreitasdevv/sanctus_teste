# Generated by Django 5.0.1 on 2024-01-30 21:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pessoas", "0006_alter_funcionario_funcao"),
    ]

    operations = [
        migrations.AlterField(
            model_name="funcionario",
            name="funcao",
            field=models.CharField(max_length=360),
        ),
    ]
