from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView, DeleteView
from sqlparse.filters import output

from .forms import EmpleadoForm, ProyectoForm, ClienteForm, TareaForm, SolicitudForm
from .models import Empleado, Proyecto, Cliente, Tarea, Solicitud


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


def pantalla_responsable(request, id_empleado_responsable):
    responsable = get_object_or_404(Empleado, id=id_empleado_responsable)
    empleados = Empleado.objects.all()
    proyectos = Proyecto.objects.all()
    clientes = Cliente.objects.all()
    solicitudes = Solicitud.objects.all()
    return render(request, 'appDeustoGes/pantalla_responsable.html', {'empleados': empleados,
                                                                      'responsable': responsable, 'proyectos': proyectos,
                                                                      'clientes': clientes, 'solicitudes':solicitudes})


#------------------------------------------------------INDEX---------------------------------------------------
def index(request):
    clientes = Cliente.objects.all()
    empleados = Empleado.objects.all()
    return render(request, 'appDeustoGes/login.html', {'clientes': clientes, 'empleados': empleados})


def index_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, "appDeustoGes/empleados_index.html", {"empleados": empleados})


def index_proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, "appDeustoGes/proyectos_index.html", {"proyectos": proyectos})

def index_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'appDeustoGes/clientes_index.html', {'clientes': clientes})

def index_proyectos_del_cliente(request, cliente_id):
    proyectos = Proyecto.objects.get(cliente=cliente_id)
    return render(request, 'appDeustoGes/proyectos_del_cliente.html', {"proyectos": proyectos})

def index_tareas(request):
    tareas = Tarea.objects.all()
    return HttpResponse('tareas_index.html')

def index_solicitud(request, id_responsable, id_solicitud):
    responsable = get_object_or_404(Empleado, id=id_responsable)
    solicitud = get_object_or_404(Empleado, id=id_solicitud)
    context = {'responsable': responsable, 'solicitud': solicitud}
    return render(request, "appDeustoGes/solicitud_index.html", context)


#------------------------------------------------------SHOW---------------------------------------------------

def show_empleado(request, id_empleado_responsable, id_empleado):
    responsable = get_object_or_404(Empleado,id=id_empleado_responsable)
    empleado = get_object_or_404(Empleado, id=id_empleado)
    return render(request, "appDeustoGes/empleado_detail.html", {'responsable': responsable,
                                                                 "empleado": empleado})

def show_proyecto(request, id_responsable, id_proyecto):
    responsable = get_object_or_404(Empleado, id=id_responsable)
    proyecto = get_object_or_404(Proyecto, id=id_proyecto)
    return render(request, "appDeustoGes/proyecto_detail.html", {"responsable": responsable,
                                                                 "proyecto": proyecto})


def show_proyecto_cliente(request, id_proyecto, id_cliente):
    cliente = get_object_or_404(Cliente, id=id_cliente)
    proyecto = get_object_or_404(Proyecto, id=id_proyecto)
    return render(request, "appDeustoGes/proyecto_detail_cliente.html", {"proyecto": proyecto,
                                                                         'cliente': cliente})

def show_cliente(request, id_cliente):
    cliente = get_object_or_404(Proyecto, id=id_cliente)
    return HttpResponse("show_cliente.html")


def show_tarea(request, id_tarea, id_empleado):
    tarea = get_object_or_404(Tarea, id=id_tarea)
    empleado = get_object_or_404(Empleado, id=id_empleado)
    context = {'tarea': tarea, 'empleado': empleado}
    return render(request, "appDeustoGes/tarea_detail.html", context)



#------------------------------------------------------CREATE---------------------------------------------------

class EmpleadoCreateView(View):
    def get(self, request, id_empleado):
        formulario = EmpleadoForm()
        empleado = get_object_or_404(Empleado, id=id_empleado)
        context = {'formulario': formulario, 'empleado': empleado}
        return render(request, 'appDeustoGes/empleado_create.html', context)

    def post(self, request):
        formulario = EmpleadoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('empleado_create')
        return render(request, 'appDeustoGes/empleado_create.html', {'formulario': formulario})

class ProyectoCreateView(View):
    def get(self, request, id_empleado):
        formulario = ProyectoForm()
        empleado = get_object_or_404(Empleado, id=id_empleado)
        solicitudes = Solicitud.objects.all()
        context = {'formulario': formulario,'empleado': empleado, 'solicitudes': solicitudes}
        return render(request, 'appDeustoGes/proyecto_create.html', context)

    def post(self, request):
        formulario = ProyectoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('proyecto_create')
        return render(request, 'appDeustoGes/proyecto_create.html', {'formulario': formulario})


class ClienteCreateView(View):
    def get(self, request, id_empleado):
        formulario = ClienteForm()
        empleado = get_object_or_404(Empleado, id=id_empleado)
        context = {'formulario': formulario, 'empleado': empleado}
        return render(request, 'appDeustoGes/cliente_create.html', context)

    def post(self, request):
        formulario = ClienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('cliente_create')
        return render(request, 'appDeustoGes/cliente_create.html', {'formulario': formulario})

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



#------------------------------------------------------UPDATE---------------------------------------------------

class ClienteUpdateView(UpdateView):
    model = Cliente

    def get(self, request, id_empleado, pk=None):
        cliente = Cliente.objects.get(id=pk)
        formulario = ClienteForm(instance=cliente)
        context = {
            'formulario': formulario,
            'cliente': cliente
        }
        return render(request, 'appDeustoGes/cliente_update.html', context)

    def post(self, request, id_empleado, pk=None):
        cliente = Cliente.objects.get(id=pk)
        formulario = ClienteForm(request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect('clientes_index')
        else:
            formulario = ClienteForm(instance=cliente)
        return render(request, 'appDeustoGes/cliente_update.html', {'formulario': formulario})



class EmpleadoUpdateView(UpdateView):
    model = Empleado

    def get(self, request, pk, empleado=None):
        cliente = Empleado.objects.get(id=pk)
        formulario = EmpleadoForm(instance=empleado)
        context = {
            'formulario': formulario,
            'empleado': empleado
        }
        return render(request, 'appDeustoGes/empleado_update.html', context)

    def post(self, request, pk):
        empleado = Empleado.objects.get(id=pk)
        formulario = EmpleadoForm(request.POST, instance=empleado)
        if formulario.is_valid():
            formulario.save()
            return redirect('empleados_index')
        else:
            formulario = ClienteForm(instance=empleado)
        return render(request, 'appDeustoGes/empleado_update.html', {'formulario': formulario})



#------------------------------------------------------DELETE---------------------------------------------------

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    success_url = reverse_lazy('empleados_index')











