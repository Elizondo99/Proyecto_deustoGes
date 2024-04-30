from django import forms

from appDeustoGes.models import Tarea, Empleado, Cliente, Proyecto


class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        # fields = ['nombre','fecha_nacimiento','antiguedad','departamento','habilidad']
        fields = '__all__'


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
