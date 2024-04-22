from datetime import date
from django.db import models


# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=15)
    telefono = models.IntegerField()
    email = models.EmailField()
    direccion = models.CharField(max_length=50)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.nombre) + " (" + str(self.direccion) + ")"

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"


class Empleado(models.Model):
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=15)
    apellidos = models.CharField(max_length=40, default="")
    email = models.EmailField()
    telefono = models.PositiveIntegerField()
    responsable = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.nombre) + " " + str(self.apellidos)

    class Meta:
        verbose_name = "empleado"
        verbose_name_plural = "empleados"


class Proyecto(models.Model):
    nombre = models.CharField(max_length=15)
    descripcion = models.TextField()
    fecha_inicio = models.DateField(default=date(2020, 1, 1))
    fecha_fin = models.DateField(default=date(2020, 1, 1))
    presupuesto = models.IntegerField()
    tareas = models.TextField(
        blank=True)  # AQUI PONEMOS LO DE blank=True ? significa que en el formulario de django se puede
    # quedar "tareas" vacio

    # miembros = models.ManyToManyField(Empleado, blank=True)
    responsable = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.nombre) + " (Responsable: " + str(self.responsable) + ")"

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"


class Tarea(models.Model):
    nombre = models.CharField(max_length=15)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    prioridad = models.CharField(max_length=10, choices=(('alta', 'Alta'), ('media', 'Media'), ('baja', 'Baja')))
    estado = models.CharField(max_length=20, choices=(
        ('abierta', 'Abierta'), ('asignada', 'Asignada'), ('en_proceso', 'En proceso'), ('finalizada', 'Finalizada')))
    notas_adicionales = models.TextField()

    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.nombre) + " (prioridad: " + str(self.prioridad) + ")"

    class Meta:
        verbose_name = 'tarea'
        verbose_name_plural = 'tareas'
