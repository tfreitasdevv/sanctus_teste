# Generated by Django 5.0.1 on 2024-01-30 23:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pessoas", "0013_paroquiano_data_cadastro"),
    ]

    operations = [
        migrations.AlterField(
            model_name="paroquiano",
            name="data_cadastro",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
