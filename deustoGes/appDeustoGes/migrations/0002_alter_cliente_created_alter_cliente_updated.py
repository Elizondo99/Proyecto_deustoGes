# Generated by Django 4.2.11 on 2024-05-02 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appDeustoGes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]