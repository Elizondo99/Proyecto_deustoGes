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

urlpatterns = [
    path('', views.index, name='request'),
    path("empleados", views.index_empleados, name='empleados_index'),
    path("empleados/int:id_empleado", views.show_empleado, name='empleados_detail'),
    path("empleados/new", views.new_empleado, name='empleados_new'),
    path("proyectos", views.index_proyectos, name='proyectos_index'),
    path("proyectos/<int:id_proyecto>", views.show_proyecto, name='proyectos_detail'),
    path("proyectos/new", views.new_proyecto, name='proyectos_new')
]
