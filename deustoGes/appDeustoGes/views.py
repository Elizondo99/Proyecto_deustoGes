from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Empleado, Proyecto


# from appEmpresaDjango.models import Empleado, Departamento, Habilidad

def index(request):
    return HttpResponse("Hello World")


# Función para crear un nuevo empleado.
def new_empleado(nombre, apellido, email, telefono, responsable):
    empleado = Empleado(nombre=nombre, apellido=apellido, email=email, telefono=telefono, responsable=responsable)
    empleado.save()
    return HttpResponse("index.html")


# Función para obtener una lista de empleados.
def index_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, "appDeustoGes/empleados_index.html", {"empleados": empleados})


# Función para obtener la información de un empleado
def show_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, id=id_empleado)
    return render(request, "appDeustoGes/empleados_detail.html", {"empleado": empleado})


# Función para crear un nuevo proyecto
def new_proyecto(nombre, descripcion, fecha_inicio, fecha_fin, presupuesto, tareas, responsable, cliente):
    proyecto = Proyecto(nombre=nombre, descripcion=descripcion, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin,
                        presupuesto=presupuesto, tareas=tareas, responsable=responsable, cliente=cliente)
    proyecto.save()
    return HttpResponse("index.html")


# Función para obtener una lista de proyectos.
def index_proyectos(request):
    proyecto = Proyecto.objects.all()
    return HttpResponse("proyectos_index.html")


# Función para obtener la información de un proyecto
def show_proyecto(request, id_proyecto):
    proyecto = get_object_or_404(Proyecto, id=id_proyecto)
    return HttpResponse("show_proyecto.html")
