# Generated by Django 4.2.11 on 2024-04-22 19:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=9)),
                ('nombre', models.CharField(max_length=15)),
                ('apellidos', models.CharField(default='', max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.PositiveIntegerField()),
                ('responsable', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'empleado',
                'verbose_name_plural': 'empleados',
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateField(default=datetime.date(2020, 1, 1))),
                ('fecha_fin', models.DateField(default=datetime.date(2020, 1, 1))),
                ('presupuesto', models.IntegerField()),
                ('tareas', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appDeustoGes.cliente')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appDeustoGes.empleado')),
            ],
            options={
                'verbose_name': 'proyecto',
                'verbose_name_plural': 'proyectos',
            },
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('prioridad', models.CharField(choices=[('alta', 'Alta'), ('media', 'Media'), ('baja', 'Baja')], max_length=10)),
                ('estado', models.CharField(choices=[('abierta', 'Abierta'), ('asignada', 'Asignada'), ('en_proceso', 'En proceso'), ('finalizada', 'Finalizada')], max_length=20)),
                ('notas_adicionales', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appDeustoGes.empleado')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appDeustoGes.proyecto')),
            ],
            options={
                'verbose_name': 'tarea',
                'verbose_name_plural': 'tareas',
            },
        ),
    ]
