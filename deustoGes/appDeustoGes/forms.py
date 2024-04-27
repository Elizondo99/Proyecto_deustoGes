from django import forms

from appDeustoGes.models import Tarea, Empleado, Cliente, Proyecto

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        #fields = ['nombre','fecha_nacimiento','antiguedad','departamento','habilidad']
        fields='__all__'