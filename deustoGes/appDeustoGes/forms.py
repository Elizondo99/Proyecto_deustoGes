from django import forms

from appDeustoGes.models import Tarea, Empleado, Cliente, Proyecto, Solicitud, User
from django.contrib.auth.forms import UserCreationForm


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


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'


class TareaUpdateForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['estado', 'notas_adicionales']


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = '__all__'


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, label='Título')
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Descripción')


class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
