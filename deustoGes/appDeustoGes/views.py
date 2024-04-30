from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, UpdateView
from sqlparse.filters import output

from .forms import EmpleadoForm, ProyectoForm, ClienteForm, TareaForm, SolicitudForm
from .models import Empleado, Proyecto, Cliente, Tarea, Solicitud


def index(request):
    clientes = Cliente.objects.all()
    empleados = Empleado.objects.all()
    return render(request, 'appDeustoGes/login.html', {'clientes': clientes, 'empleados': empleados})


def pantalla_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id=id_cliente)
    proyectos = Proyecto.objects.all()
    return render(request, 'appDeustoGes/pantalla_cliente.html', {'proyectos': proyectos,
                                                                  'cliente': cliente}, )


def pantalla_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, id=id_empleado)
    tareas = Tarea.objects.all()
    return render(request, 'appDeustoGes/pantalla_empleado.html', {'tareas': tareas,
                                                                   'empleado': empleado})


def pantalla_responsable(request, id_empleado):
    empleado = get_object_or_404(Empleado, id=id_empleado)
    empleados = Empleado.objects.all()
    proyectos = Proyecto.objects.all()
    clientes = Cliente.objects.all()
    return render(request, 'appDeustoGes/pantalla_responsable.html', {'empleados': empleados,
                                                                      'empleado': empleado, 'proyectos': proyectos,
                                                                      'clientes': clientes})


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
        solicitudes = Solicitud.objects.all()
        context = {'formulario': formulario, 'solicitudes': solicitudes}
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
class ClienteCreateView(View):
    def get(self, request):
        formulario = ClienteForm()
        context = {'formulario': formulario}
        return render(request, 'appDeustoGes/cliente_create.html', context)

    def post(self, request):
        formulario = ClienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('cliente_create')
        return render(request, 'appDeustoGes/cliente_create.html', {'formulario': formulario})


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
class TareaCreateView(View):
    def get(self, request):
        formulario = TareaForm()
        context = {'formulario': formulario}
        return render(request, 'appDeustoGes/tarea_create.html', context)

    def post(self, request):
        formulario = TareaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('tarea_create')
        return render(request, 'appDeustoGes/tarea_create.html', {'formulario': formulario})


def index_tareas(request):
    tareas = Tarea.objects.all()
    return HttpResponse('tareas_index.html')


def show_tareas(request, id_tarea):
    tarea = get_object_or_404(Proyecto, id_tarea=id_tarea)
    return HttpResponse('tareas_show.html')


class ClienteUpdateView(UpdateView):
    model = Cliente

    def get(self, request, pk):
        cliente = Cliente.objects.get(id=pk)
        formulario = ClienteForm(instance=cliente)
        context = {
            'formulario': formulario,
            'cliente': cliente
        }
        return render(request, 'appDeustoGes/cliente_update.html', context)

    def post(self, request, pk):
        cliente = Cliente.objects.get(id=pk)
        formulario = ClienteForm(request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect('clientes_index', cliente.id)
        else:
            formulario = ClienteForm(instance=cliente)
        return render(request, 'appDeustoGes/cliente_update.html', {'formulario': formulario})


class SolicitudCreateView(View):
    def get(self, request):
        formulario = SolicitudForm()
        context = {'formulario': formulario}
        return render(request, 'appDeustoGes/pantalla_cliente.html', context)

    def post(self, request):
        formulario = SolicitudForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('solicitud_create')
        return render(request, 'appDeustoGes/pantalla_cliente.html', {'formulario': formulario})
