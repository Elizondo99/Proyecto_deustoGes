from django.contrib import admin

from appDeustoGes.models import Cliente, Proyecto, Empleado, Tarea, Solicitud


# Register your models here.
admin.site.register(Cliente)
admin.site.register(Proyecto)
admin.site.register(Empleado)
admin.site.register(Tarea)
admin.site.register(Solicitud)