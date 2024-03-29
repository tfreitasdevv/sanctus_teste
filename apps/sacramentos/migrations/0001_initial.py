# Generated by Django 5.0.1 on 2024-02-06 15:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batismo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('batizado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batismos_batizado', to='pessoas.paroquiano')),
                ('celebrante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batismos_celebrante', to='pessoas.clero')),
                ('padrinho1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batismos_padrinho1', to='pessoas.paroquiano')),
                ('padrinho2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batismos_padrinho2', to='pessoas.paroquiano')),
            ],
            options={
                'ordering': ['batizado'],
            },
        ),
        migrations.CreateModel(
            name='Crisma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('celebrante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crismas_celebrante', to='pessoas.clero')),
                ('crismado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crismas_crismado', to='pessoas.paroquiano')),
                ('padrinho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crismas_padrinho', to='pessoas.paroquiano')),
            ],
            options={
                'ordering': ['crismado'],
            },
        ),
        migrations.CreateModel(
            name='Eucaristia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('celebrante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eucaristias_celebrante', to='pessoas.clero')),
                ('comungante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eucaristias_comungante', to='pessoas.paroquiano')),
            ],
            options={
                'ordering': ['comungante'],
            },
        ),
        migrations.CreateModel(
            name='Matrimonio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('celebrante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matrimonios_celebrante', to='pessoas.clero')),
                ('noiva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matrimonios_noiva', to='pessoas.paroquiano')),
                ('noivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matrimonios_noivo', to='pessoas.paroquiano')),
                ('testemunha1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matrimonios_testemunha1', to='pessoas.paroquiano')),
                ('testemunha2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matrimonios_testemunha2', to='pessoas.paroquiano')),
            ],
            options={
                'ordering': ['noivo'],
            },
        ),
    ]
