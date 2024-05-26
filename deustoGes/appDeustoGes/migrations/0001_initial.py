# Generated by Django 4.2.11 on 2024-05-26 16:20

import datetime
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
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
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
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
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
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
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
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
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appDeustoGes.empleado')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appDeustoGes.proyecto')),
            ],
            options={
                'verbose_name': 'tarea',
                'verbose_name_plural': 'tareas',
            },
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=31)),
                ('descripcion', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appDeustoGes.cliente')),
            ],
            options={
                'verbose_name': 'solicitud',
                'verbose_name_plural': 'solicitudes',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuarios',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
