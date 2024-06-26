from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView
from pyexpat.errors import messages
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm, RegistroForm, TareaUpdateClienteForm

from .forms import EmpleadoForm, ProyectoForm, ClienteForm, TareaForm, SolicitudForm, TareaUpdateForm
from .models import Empleado, Proyecto, Cliente, Tarea, Solicitud


# Función para obtener la pantalla principal del rol cliente.
def pantalla_cliente(request, id_cliente):
    cliente = get_object_or_404(Cliente, id=id_cliente)
    proyectos = Proyecto.objects.all()
    return render(request, 'appDeustoGes/pantalla_cliente.html', {'proyectos': proyectos,
                                                                  'cliente': cliente})


# Función para obtener la pantalla principal del rol empleado.
def pantalla_empleado(request, id_empleado):
    empleado = get_object_or_404(Empleado, id=id_empleado)
    tareas = Tarea.objects.all()
    return render(request, 'appDeustoGes/pantalla_empleado.html', {'tareas': tareas,
                                                                   'empleado': empleado})


# Función para obtener la pantalla principal del rol responsable.
def pantalla_responsable(request, id_responsable):
    responsable = get_object_or_404(Empleado, id=id_responsable)
    empleados = Empleado.objects.all()
    proyectos = Proyecto.objects.all()
    clientes = Cliente.objects.all()
    solicitudes = Solicitud.objects.all()
    return render(request, 'appDeustoGes/pantalla_responsable.html', {'empleados': empleados,
                                                                      'responsable': responsable,
                                                                      'proyectos': proyectos,
                                                                      'clientes': clientes, 'solicitudes': solicitudes})


# ------------------------------------------------------INDEX---------------------------------------------------
# Función para obtener la pantalla login.
@login_required
def login(request):
    clientes = Cliente.objects.all()
    empleados = Empleado.objects.all()
    return render(request, 'appDeustoGes/pantalla_inicio_app.html',
                  {'clientes': clientes, 'empleados': empleados})


def logout(request):
    logout(request)
    clientes = Cliente.objects.all()
    empleados = Empleado.objects.all()
    return render(request, 'appDeustoGes/pantalla_inicio_app.html',
                  {'clientes': clientes, 'empleados': empleados})


def registro(request):
    """formulario = ClienteForm(data=request.POST)
    if formulario.is_valid():
        formulario.save()
        return HttpResponseRedirect(reverse_lazy('login'))
    """
    formulario = RegistroForm(data=request.POST)
    if formulario.is_valid():
        formulario.save()
        return render(request, 'appDeustoGes/registro_exitoso.html')
    else:
        print(formulario.errors)
    return render(request, 'appDeustoGes/pantalla_registro_usuario.html', {'formulario': formulario})


# Función para obtener el listado de proyectos.
def index_proyectos(request, id_responsable):
    responsable = get_object_or_404(Empleado, id=id_responsable)
    proyectos = Proyecto.objects.all()
    return render(request, "appDeustoGes/gestion_proyectos.html", {"proyectos": proyectos,
                                                                   "responsable": responsable})


# Función para obtener los proyectos del cliente.
@login_required
def index_proyectos_del_cliente(request, cliente_id):
    proyectos = Proyecto.objects.get(cliente=cliente_id)
    return render(request, 'appDeustoGes/proyectos_del_cliente.html', {"proyectos": proyectos})


# Función para obtener las solicitudes generadas por el cliente.
@login_required
def index_solicitud(request, id_responsable, id_solicitud):
    responsable = get_object_or_404(Empleado, id=id_responsable)
    solicitud = get_object_or_404(Empleado, id=id_solicitud)
    context = {'responsable': responsable, 'solicitud': solicitud}
    return render(request, "appDeustoGes/solicitud_index.html", context)


# ------------------------------------------------------SHOW---------------------------------------------------
# Función para obtener los detalles de un empleado.
@login_required
def show_empleado(request, id_responsable, id_empleado):
    responsable = get_object_or_404(Empleado, id=id_responsable)
    empleado = get_object_or_404(Empleado, id=id_empleado)
    return render(request, "appDeustoGes/empleado_detail.html", {'responsable': responsable,
                                                                 "empleado": empleado})


# Función para obtener los detalles de un proyecto.
def show_proyecto(request, id_responsable, id_proyecto):
    responsable = get_object_or_404(Empleado, id=id_responsable)
    proyecto = get_object_or_404(Proyecto, id=id_proyecto)
    tareas = Tarea.objects.all()
    return render(request, "appDeustoGes/proyecto_detail.html", {"responsable": responsable,
                                                                 "proyecto": proyecto, "tareas": tareas})


# Función para obtener los detalles de un proyecto de un cliente.
def show_proyecto_cliente(request, id_proyecto, id_cliente):
    cliente = get_object_or_404(Cliente, id=id_cliente)
    proyecto = get_object_or_404(Proyecto, id=id_proyecto)
    tareas = Tarea.objects.all()
    return render(request, "appDeustoGes/proyecto_detail_cliente.html", {"proyecto": proyecto,
                                                                         'cliente': cliente, "tareas": tareas})


# Función para obtener los detalles de una tarea.
def show_tarea(request, id_tarea, id_empleado):
    tarea = get_object_or_404(Tarea, id=id_tarea)
    empleado = get_object_or_404(Empleado, id=id_empleado)
    context = {'tarea': tarea, 'empleado': empleado}
    return render(request, "appDeustoGes/tarea_detail.html", context)


# ------------------------------------------------------CREATE---------------------------------------------------
# Función para crear un nuevo empleado.
class EmpleadoCreateView(View):
    def get(self, request, id_responsable):
        formulario = EmpleadoForm()
        responsable = get_object_or_404(Empleado, id=id_responsable)
        context = {'formulario': formulario, 'responsable': responsable}
        return render(request, 'appDeustoGes/empleado_create.html', context)

    def post(self, request, id_responsable):
        responsable = get_object_or_404(Empleado, id=id_responsable)
        formulario = EmpleadoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect(reverse_lazy('pantalla_responsable', args=[responsable.id]))
        return render(request, 'appDeustoGes/empleado_create.html', {'formulario': formulario})


# Función para crear un nuevo proyecto.
class ProyectoCreateView(View):
    def get(self, request, id_responsable, id_solicitud):
        formulario = ProyectoForm()
        responsable = get_object_or_404(Empleado, id=id_responsable)
        solicitud = get_object_or_404(Solicitud, id=id_solicitud)
        context = {'formulario': formulario, 'responsable': responsable, 'solicitud': solicitud}
        return render(request, 'appDeustoGes/proyecto_create.html', context)

    def post(self, request, id_responsable, id_solicitud):
        responsable = get_object_or_404(Empleado, id=id_responsable)
        formulario = ProyectoForm(data=request.POST)
        solicitud = get_object_or_404(Solicitud, id=id_solicitud)
        if formulario.is_valid():
            formulario.save()
            solicitud.delete()
            return HttpResponseRedirect(reverse_lazy('pantalla_responsable', args=[responsable.id]))
        return render(request, 'appDeustoGes/proyecto_create.html', {'formulario': formulario,
                                                                     'responsable': responsable,
                                                                     'solicitud': solicitud})


# Función para crear un nuevo cliente.
class ClienteCreateView(View):
    def get(self, request, id_responsable):
        formulario = ClienteForm()
        responsable = get_object_or_404(Empleado, id=id_responsable)
        context = {'formulario': formulario, 'responsable': responsable}
        return render(request, 'appDeustoGes/cliente_create.html', context)

    def post(self, request, id_responsable):
        responsable = get_object_or_404(Empleado, id=id_responsable)
        formulario = ClienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect(reverse_lazy('pantalla_responsable', args=[responsable.id]))
        return render(request, 'appDeustoGes/cliente_create.html',
                      {'formulario': formulario, 'responsable': responsable})


# Función para crear una nueva tarea.
class TareaCreateView(View):
    def get(self, request, id_responsable):
        responsable = get_object_or_404(Empleado, id=id_responsable)
        formulario = TareaForm()
        context = {'formulario': formulario, 'responsable': responsable}
        return render(request, 'appDeustoGes/tarea_create.html', context)

    def post(self, request, id_responsable):
        responsable = get_object_or_404(Empleado, id=id_responsable)
        formulario = TareaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect(reverse_lazy('pantalla_responsable', args=[responsable.id]))
        return render(request, 'appDeustoGes/tarea_create.html', {'formulario': formulario})


# Función para crear una nueva solicitud.
class SolicitudCreateView(View):
    def get(self, request, id_cliente):
        cliente = Cliente.objects.get(id=id_cliente)
        formulario = SolicitudForm()
        context = {'formulario': formulario, 'cliente': cliente}
        return render(request, 'appDeustoGes/solicitud_create.html', context)

    def post(self, request, id_cliente):
        cliente = Cliente.objects.get(id=id_cliente)
        formulario = SolicitudForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect(reverse_lazy('pantalla_cliente', args=[cliente.id]))
        return render(request, 'appDeustoGes/solicitud_create.html', {'formulario': formulario})


# ------------------------------------------------------UPDATE---------------------------------------------------
# Función para editar los datos de un cliente.
class ClienteUpdateView(UpdateView):
    model = Cliente

    def get(self, request, id_cliente):
        cliente = Cliente.objects.get(id=id_cliente)
        formulario = ClienteForm(instance=cliente)
        context = {
            'formulario': formulario,
            'cliente': cliente
        }
        return render(request, 'appDeustoGes/cliente_update.html', context)

    def post(self, request, id_cliente):
        cliente = Cliente.objects.get(id=id_cliente)
        formulario = ClienteForm(request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect(reverse_lazy('pantalla_cliente', args=[cliente.id]))
        else:
            formulario = ClienteForm(instance=cliente)
        return render(request, 'appDeustoGes/cliente_update.html', {'formulario': formulario})


# Función para editar los datos de un empleado.
class EmpleadoUpdateView(UpdateView):
    model = Empleado

    def get(self, request, id_responsable, id_empleado):
        responsable = get_object_or_404(Empleado, id=id_responsable)
        empleado = Empleado.objects.get(id=id_empleado)
        formulario = EmpleadoForm(instance=empleado)
        context = {
            'responsable': responsable,
            'formulario': formulario,
            'empleado': empleado
        }
        return render(request, 'appDeustoGes/empleado_update.html', context)

    def post(self, request, id_responsable, id_empleado):
        responsable = get_object_or_404(Empleado, id=id_responsable)
        empleado = Empleado.objects.get(id=id_empleado)
        formulario = EmpleadoForm(request.POST, instance=empleado)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect(reverse_lazy('pantalla_responsable', args=[responsable.id]))
        else:
            formulario = ClienteForm(instance=empleado)
        return render(request, 'appDeustoGes/empleado_update.html', {'formulario': formulario,
                                                                     'responsable': responsable})


# Función para editar los datos de una tarea.
class TareaUpdateView(UpdateView):
    model = Tarea

    def get(self, request, id_empleado, id_tarea):
        tarea = get_object_or_404(Tarea, id=id_tarea)
        empleado = get_object_or_404(Empleado, id=id_empleado)
        formulario = TareaUpdateClienteForm(instance=tarea)
        context = {
            'formulario': formulario,
            'empleado': empleado,
            'tarea': tarea
        }
        return render(request, 'appDeustoGes/tarea_update.html', context)

    def post(self, request, id_empleado, id_tarea):
        tarea = get_object_or_404(Tarea, id=id_tarea)
        empleado = Empleado.objects.get(id=id_empleado)
        formulario = TareaUpdateClienteForm(request.POST, instance=tarea)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect(reverse_lazy('pantalla_empleado', args=[empleado.id]))
        else:
            formulario = TareaUpdateForm(instance=tarea)
        return render(request, 'appDeustoGes/tarea_update.html', {'formulario': formulario,
                                                                  'empleado': empleado})


def updateTareaResponsable(request, id_responsable, id_tarea):
    tarea = get_object_or_404(Tarea, id=id_tarea)
    tareas = Tarea.objects.all()
    responsable = get_object_or_404(Empleado, id=id_responsable)
    if request.method == 'POST':
        formulario = TareaUpdateForm(request.POST, instance=tarea)
        if formulario.is_valid():
            formulario.save()
            return render(request, 'appDeustoGes/gestion_tareas.html',
                          {'responsable': responsable, 'tareas': tareas})
    else:
        formulario = TareaUpdateForm(instance=tarea)
    context = {
        'formulario': formulario,
        'responsable': responsable,
        'tarea': tarea
    }
    return render(request, 'appDeustoGes/tarea_update_responsable.html', context)


# ------------------------------------------------------DELETE---------------------------------------------------
# Función para borrar un empleado.
def delete_empleado(request, id_responsable, id_empleado):
    empleado = get_object_or_404(Empleado, id=id_empleado)
    responsable = get_object_or_404(Empleado, id=id_responsable)
    if empleado.delete():
        return render(request, 'appDeustoGes/pantalla_borrado_exitoso.html',
                      {'responsable': responsable})


# Función para borrar un proyecto.
def delete_proyecto(request, id_responsable, id_proyecto):
    responsable = get_object_or_404(Empleado, id=id_responsable)
    proyecto = get_object_or_404(Proyecto, id=id_proyecto)
    if proyecto.delete():
        return render(request, 'appDeustoGes/pantalla_borrado_exitoso.html',
                      {'responsable': responsable})


# Función para borrar un cliente.
def delete_cliente(request, id_responsable, id_cliente):
    cliente = get_object_or_404(Cliente, id=id_cliente)
    responsable = get_object_or_404(Empleado, id=id_responsable)
    if cliente.delete():
        return render(request, 'appDeustoGes/pantalla_borrado_exitoso.html',
                      {'responsable': responsable})


# Función para borrar una tarea.
def delete_tarea(request, id_responsable, id_tarea):
    tarea = get_object_or_404(Cliente, id=id_tarea)
    responsable = get_object_or_404(Empleado, id=id_responsable)
    if tarea.delete():
        return render(request, 'appDeustoGes/pantalla_borrado_exitoso.html',
                      {'responsable': responsable})


def preguntas_frecuentes(request, id_cliente):
    cliente = get_object_or_404(Cliente, id=id_cliente)

    return render(request, 'appDeustoGes/preguntas_frecuentes.html', {'cliente': cliente})


def contact_view(request, id_cliente):
    cliente = get_object_or_404(Cliente, id=id_cliente)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = 'deustoges.contacto@gmail.com'
            message = form.cleaned_data['message']
            send_mail(
                subject,
                message,
                email,
                ['deustoges.contacto@gmail.com'],
            )
            return render(request, 'appDeustoGes/pantalla_cliente.html', {'form': form, 'cliente': cliente})
    else:
        form = ContactForm()
    return render(request, 'appDeustoGes/contacto.html', {'form': form, 'cliente': cliente})


def gestion_empleados(request, id_responsable):
    responsable = get_object_or_404(Empleado, id=id_responsable)
    empleados = Empleado.objects.all()
    return render(request, 'appDeustoGes/gestion_empleados.html',
                  {'responsable': responsable, 'empleados': empleados})


def gestion_clientes(request, id_responsable):
    responsable = get_object_or_404(Empleado, id=id_responsable)
    clientes = Cliente.objects.all()
    return render(request, 'appDeustoGes/gestion_clientes.html',
                  {'responsable': responsable, 'clientes': clientes})


def gestion_tareas(request, id_responsable):
    responsable = get_object_or_404(Empleado, id=id_responsable)
    tareas = Tarea.objects.all()
    return render(request, 'appDeustoGes/gestion_tareas.html',
                  {'responsable': responsable, 'tareas': tareas})


def gestion_solicitudes(request, id_responsable):
    responsable = get_object_or_404(Empleado, id=id_responsable)
    solicitudes = Solicitud.objects.all()
    return render(request, 'appDeustoGes/gestion_solicitudes.html',
                  {'responsable': responsable, 'solicitudes': solicitudes})
