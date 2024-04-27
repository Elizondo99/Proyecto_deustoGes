"""
URL configuration for appDeustoGes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import EmpleadoCreateView

urlpatterns = [
    path('', views.index, name='login'),
    path("/introduccion_cliente", views.introduccion_cliente, name='introduccion_cliente'),
    path("/empleados", views.index_empleados, name='empleados_index'),
    path("/empleados/<int:id_empleado>", views.show_empleado, name='empleado_detail'),
    #path("/empleados/new", views.new_empleado, name='empleados_new'),
    path('/empleados/create', EmpleadoCreateView.as_view(), name="empleado_create"),

    path("/proyectos", views.index_proyectos, name='proyectos_index'),
    path("/proyectos/<int:id_proyecto>", views.show_proyecto, name='proyecto_detail'),
    path("/proyectos/new", views.new_proyecto, name='proyectos_new'),

    path("/clientes", views.index_clientes, name='clientes_index'),
    path("/clientes/<int:id_cliente>", views.show_cliente, name='cliente_detail'),
    path("/clientes/new", views.new_cliente, name='clientes_new'),
    path("/clientes/<int:id_cliente>/proyectos", views.index_proyectos_del_cliente, name='proyectos_del_cliente')
]
