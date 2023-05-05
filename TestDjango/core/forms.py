from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import DuenoEstacionamiento,ClienteArrendador, Comuna, Banco



class CustomerUserCreationForm (UserCreationForm):
   class Meta:
    model = User
    fields=['username',"first_name","last_name","email","password1","password2"]

class ModificarUsuario (ModelForm):
   class Meta:
    model = User
    fields=['username',"first_name","last_name","email","password"]

class CrearCuentaAdmin (UserCreationForm):
   class Meta:
    model = User
    fields=['username',"first_name","last_name","email","is_superuser","password1","password2"]

class CrearCuentaDueñoEst (UserCreationForm):
   class Meta:
    model = User
    fields=['username',"first_name","last_name","email","is_superuser","password1","password2"]


class CrearCuentaCliente (UserCreationForm):
   class Meta:
    model = User
    fields=['username',"first_name","last_name","email","is_staff","password1","password2"]

class CrearDueñoForm (forms.ModelForm):
    class Meta:
        model = DuenoEstacionamiento
        password = forms.CharField(widget=forms.PasswordInput)
        fields = ("nombreUsuario","nombre","p_apellido","s_apellido","rut","telefono","direccion","nombreCalle","cuentaBancaria","correo","comuna","region","password")

class CrearClienteForm (forms.ModelForm):
    class Meta:
        model = ClienteArrendador
        fields = ("nombreUsuario","nombre","p_apellido","s_apellido","rut","telefono","direccion","tarjetaCredito","correo","comuna","banco","region","password")
