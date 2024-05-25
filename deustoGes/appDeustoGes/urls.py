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
from django.contrib.auth.views import LoginView
from django.urls import path
from . import views
from .views import (EmpleadoCreateView, ProyectoCreateView, ClienteUpdateView, ClienteCreateView, SolicitudCreateView,
                    EmpleadoUpdateView, TareaCreateView, TareaUpdateView)


urlpatterns = [


    # URL DE LOGIN
    path('/', views.login, name='pantalla_inicio'),
    path('/registro', views.registro, name='registro'),

    # URL DE INICIO DE CADA ROL
    path("/clientes/<int:id_cliente>", views.pantalla_cliente, name='pantalla_cliente'),
    path("/empleados/<int:id_empleado>", views.pantalla_empleado, name='pantalla_empleado'),
    path("/responsables/<int:id_responsable>", views.pantalla_responsable, name='pantalla_responsable'),

    # URL PARA LISTAR
    path("/responsables/<int:id_responsable>/proyectos/", views.index_proyectos, name='proyectos_index'),

    # URL PARA OBTENER DETALLES
    path("/responsables/<int:id_responsable>/empleados/<int:id_empleado>/detalle", views.show_empleado, name='empleado_detail'),
    path("/responsables/<int:id_responsable>/proyectos/<int:id_proyecto>", views.show_proyecto, name='proyecto_detail'),
    path("/clientes/<int:id_cliente>/proyectos/<int:id_proyecto>", views.show_proyecto_cliente, name='proyecto_detail_cliente'),
    path("/empleados/<int:id_empleado>/tareas/<int:id_tarea>", views.show_tarea, name='tarea_detail'),

    # URL DE FORMULARIOS PARA CREAR
    path('/responsables/<int:id_responsable>/empleados/create', EmpleadoCreateView.as_view(), name="empleado_create"),
    path('/responsables/<int:id_responsable>/proyectos/<int:id_solicitud>/create', ProyectoCreateView.as_view(), name="proyecto_create"),
    path('/responsables/<int:id_responsable>/clientes/create', ClienteCreateView.as_view(), name="cliente_create"),
    path('/clientes/<int:id_cliente>/solicitud', SolicitudCreateView.as_view(), name="solicitud_create"),
    path('/responsables/<int:id_responsable>/tareas/create', TareaCreateView.as_view(), name="tarea_create"),

    # URL DE UPDATE
    path('/clientes/<int:id_cliente>/update', ClienteUpdateView.as_view(), name="cliente_update"),
    path('/responsables/<int:id_responsable>/empleados/<int:id_empleado>/update', EmpleadoUpdateView.as_view(), name="empleado_update"),
    path('/empleados/<int:id_empleado>/tareas/<int:id_tarea>/update', TareaUpdateView.as_view(), name="tarea_update"),

    # URL DE DELETE
    path('/responsables/<int:id_responsable>/deleted/empleado/<int:id_empleado>', views.delete_empleado, name="delete_empleado"),
    path('/responsables/<int:id_responsable>/deleted/proyecto/<int:id_proyecto>', views.delete_proyecto, name="delete_proyecto"),
    path('/responsables/<int:id_responsable>/deleted/cliente/<int:id_cliente>', views.delete_cliente, name="delete_cliente"),

    path("/clientes/<int:id_cliente>/preguntas_frecuentes", views.preguntas_frecuentes, name='preguntas_frecuentes'),
    path("/clientes/<int:id_cliente>/contacto", views.contact_view, name='contacto')
]
