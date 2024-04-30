from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from sqlparse.filters import output

from .forms import EmpleadoForm, ProyectoForm
from .models import Empleado, Proyecto, Cliente, Tarea


def index(request):
    clientes = Cliente.objects.all()
    return render(request, 'appDeustoGes/login.html', {'clientes': clientes})


def introduccion_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id=id_cliente)
    proyectos = Proyecto.objects.all()
    return render(request, 'appDeustoGes/introduccion_cliente.html', {'proyectos': proyectos,
                                                                      'cliente': cliente},)


def introduccion_empleado(request):
    return render(request, 'appDeustoGes/introduccion_empleado.html')


# Función para crear un nuevo empleado.
class EmpleadoCreateView(View):
    def get(self, request):
        formulario = EmpleadoForm()
        context = {'formulario': formulario}
        return render(request, 'appDeustoGes/empleado_create.html', context)

    def post(self, request):
        formulario = EmpleadoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('empleado_create')
        return render(request, 'appDeustoGes/empleado_create.html', {'formulario': formulario})


# Función para obtener una lista de empleados.
def index_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, "appDeustoGes/empleados_index.html", {"empleados": empleados})


# Función para obtener la información de un empleado
def show_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, id=id_empleado)
    return render(request, "appDeustoGes/empleado_detail.html", {"empleado": empleado})


# Función para crear un nuevo proyecto
class ProyectoCreateView(View):
    def get(self, request):
        formulario = ProyectoForm()
        context = {'formulario': formulario}
        return render(request, 'appDeustoGes/proyecto_create.html', context)

    def post(self, request):
        formulario = ProyectoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('proyecto_create')
        return render(request, 'appDeustoGes/proyecto_create.html', {'formulario': formulario})


# Función para obtener una lista de proyectos.
def index_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, "appDeustoGes/proyectos_index.html", {"proyectos": proyectos})


# Función para obtener la información de un proyecto
def show_proyecto(request, id_proyecto):
    proyecto = get_object_or_404(Proyecto, id=id_proyecto)
    return render(request, "appDeustoGes/proyecto_detail.html", {"proyecto": proyecto})


# Función para crear un nuevo cliente
def new_cliente(nombre, telefono, email, direccion):
    created = datetime.now()
    updated = datetime.now()
    cliente = Cliente(nombre=nombre, telefono=telefono, email=email, direccion=direccion, created=created,
                      updated=updated)
    cliente.save()


# Función para obtener una lista de clientes
def index_clientes(request):
    cliente = Cliente.objects.all()
    return HttpResponse("clientes_index.html")


# Función para mostrar los detailes de un cliente
def show_cliente(request, id_cliente):
    cliente = get_object_or_404(Proyecto, id=id_cliente)
    return HttpResponse("show_cliente.html")


# Función para mostrar los proyectos de un cliente
def index_proyectos_del_cliente(request, cliente_id):
    proyectos = Proyecto.objects.get(cliente=cliente_id)
    return render(request, 'appDeustoGes/proyectos_del_cliente.html', {"proyectos": proyectos})


# Función para crear una nueva tarea.
def new_tareas(nombre, descripccion, fecha_inicio, fecha_fin, prioidad, estado, empleado, notas_adicionales, proyecto):
    created = datetime.now()
    updated = datetime.now()
    tarea = Tarea(nombre=nombre, descripcion=descripccion, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin,
                  prioidad=prioidad, estado=estado, empleado=empleado, notas_adicionales=notas_adicionales,
                  proyecto=proyecto)
    tarea.save()


def index_tareas(request):
    tareas = Tarea.objects.all()
    return HttpResponse('tareas_index.html')


def show_tareas(request, id_tarea):
    tarea = get_object_or_404(Proyecto, id_tarea=id_tarea)
    return HttpResponse('tareas_show.html')
