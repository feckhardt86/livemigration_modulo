# Generated by Django 2.1.2 on 2018-10-21 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastroagendamento',
            name='data',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='logslivemotion',
            name='data_fim',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='logslivemotion',
            name='data_inicio',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
