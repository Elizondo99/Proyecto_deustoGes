# Generated by Django 4.2.11 on 2024-04-18 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDeustoGes', '0004_alter_proyecto_fecha_fin_alter_proyecto_fecha_inicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_fin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_inicio',
            field=models.DateField(),
        ),
    ]
