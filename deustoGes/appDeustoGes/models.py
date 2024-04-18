from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=15)
    telefono = models.IntegerField()
    email = models.EmailField()
    direccion = models.CharField(max_length=50)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Empleado(models.Model):

    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=15)
    apellidos = models.CharField(max_length=40)
    email = models.EmailField()
    telefono = models.IntegerField()
    responsable = models.BooleanField(default=False)


    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Proyecto(models.Model):

    nombre = models.CharField(max_length=15)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    presupuesto = models.IntegerField()
    tareas = models.TextField(blank=True)

    miembros = models.ManyToManyField(Empleado, blank=True)
    responsable  = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    cliente =models.ForeignKey(Cliente, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Tarea(models.Model):

    nombre = models.CharField(max_length=15)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    prioridad = models.CharField(max_length=10, choices=(('alta', 'Alta'), ('media', 'Media'), ('baja', 'Baja')))
    estado = models.CharField(max_length=20, choices=(('abierta', 'Abierta'), ('asignada', 'Asignada'), ('en_proceso', 'En proceso'), ('finalizada', 'Finalizada')))
    notas_adicionales = models.TextField()

    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)