from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from deustoGes.appDeustoGes.models import Empleado


#from appEmpresaDjango.models import Empleado, Departamento, Habilidad

def index(request):
    return HttpResponse("Hello World")

#def new_empleado(nombre, apellido, email, telefono, responsable):
#    empleado = Empleado() #SIN ACABAR --> vista para crear empleados

def index_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, "appDeustoGes/empleados_index.html", {"empleados":empleados})

def show_empleado(request, id):
    empleado = get_object_or_404(Empleado, pk=id)
    return render(request, "appDeustoGes/empleados_detail.html", {"empleado":empleado})
