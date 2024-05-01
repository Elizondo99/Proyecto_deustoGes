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
from .views import EmpleadoCreateView, ProyectoCreateView, ClienteUpdateView, ClienteCreateView, SolicitudCreateView, \
    EmpleadoDeleteView


class DepartamentoDeleteView:
    pass


urlpatterns = [

    # URL DE LOGIN
    path('/', views.index, name='login'),

    # URL DE INICIO DE CADA ROL
    path("/clientes/<int:id_cliente>", views.pantalla_cliente, name='pantalla_cliente'),
    path("/empleados/<int:id_empleado>", views.pantalla_empleado, name='pantalla_empleado'),
    path("/responsables/<int:id_empleado>", views.pantalla_responsable, name='pantalla_responsable'),

    # URL PARA LISTAR
    path("/empleados", views.index_empleados, name='empleados_index'),
    path("/proyectos", views.index_proyectos, name='proyectos_index'),
    path("/clientes", views.index_clientes, name='clientes_index'),
    # path("/clientes/<int:id_cliente>/proyectos", views.index_proyectos_del_cliente, name='proyectos_del_cliente'),

    # URL PARA OBTENER DETALLES
    path("/empleados/<int:id_empleado>", views.show_empleado, name='empleado_detail'),
    path("/proyectos/<int:id_proyecto>", views.show_proyecto, name='proyecto_detail'),
    path("/proyectos/cliente/<int:id_proyecto>", views.show_proyecto_cliente, name='proyecto_detail_cliente'),
    path("/clientes/<int:id_cliente>", views.show_cliente, name='cliente_detail'),
    path("/tareas/<int:id_tarea>", views.show_tarea, name='tarea_detail'),


    # URL DE FORMULARIOS PARA CREAR
    path('/empleados/create', EmpleadoCreateView.as_view(), name="empleado_create"),
    path('/proyectos/create', ProyectoCreateView.as_view(), name="proyecto_create"),
    path('/clientes/create', ClienteCreateView.as_view(), name="cliente_create"),
    path('/clientes/solicitud', SolicitudCreateView.as_view(), name="solicitud_create"),
    # path("/empleados/new", views.new_empleado, name='empleados_new'),
    #path("/proyectos/new", views.new_proyecto, name='proyectos_new'),
    #path("/clientes/new", views.new_cliente, name='clientes_new'),

    # URL DE UPDATE
    path('/clientes/update/<int:pk>', ClienteUpdateView.as_view(), name="cliente_update"),

    # URL DE UPDATE
    path('/empleados/delete/<int:pk>', EmpleadoDeleteView.as_view(), name='empleado_delete'),

]
