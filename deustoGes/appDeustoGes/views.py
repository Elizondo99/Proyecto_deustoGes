from django.http import HttpResponse
from django.shortcuts import render
#from appEmpresaDjango.models import Empleado, Departamento, Habilidad

def index(request):
    return HttpResponse("Hello World")