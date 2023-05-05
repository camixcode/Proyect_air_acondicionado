from django.shortcuts import redirect,render
from .forms import CustomerUserCreationForm, CrearCuentaCliente, CrearClienteForm, CrearDueñoForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import DuenoEstacionamiento, ClienteArrendador , Estacionamiento





# Create your views here.



def formularioCliente(request):
    data = {
        'form': CrearClienteForm()
    }
    if request.method == 'POST':
        formulario = CrearClienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            nuevaCuenta = User
            nuevaCuenta.objects.create(first_name=formulario.cleaned_data["nombre"],last_name=formulario.cleaned_data["p_apellido"]+" "+formulario.cleaned_data["s_apellido"],email=formulario.cleaned_data["correo"],is_superuser=0,is_staff=0,password=formulario.cleaned_data["password"],username=formulario.cleaned_data["nombreUsuario"])
            u = User.objects.get(username=formulario.cleaned_data["nombreUsuario"])
            u.set_password(formulario.cleaned_data["password"])
            u.save()
            messages.success(request, "Cuenta creada correctamente")
            return redirect(to="index")
        data["form"] = formulario
    return render(request, 'core/formularioCliente.html',data)

def formularioDueñoEst(request):
    data = {
        'form': CrearDueñoForm()
    }
    if request.method == 'POST':
        formulario = CrearDueñoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            nuevaCuenta = User
            nuevaCuenta.objects.create(first_name=formulario.cleaned_data["nombre"],last_name=formulario.cleaned_data["p_apellido"]+" "+formulario.cleaned_data["s_apellido"],email=formulario.cleaned_data["correo"],is_superuser=0,is_staff=1,password=formulario.cleaned_data["password"],username=formulario.cleaned_data["nombreUsuario"])
            u = User.objects.get(username=formulario.cleaned_data["nombreUsuario"])
            u.set_password(formulario.cleaned_data["password"])
            u.save()
            messages.success(request, "Cuenta creada correctamente")
            return redirect(to="index")
        data["form"] = formulario
    return render(request, 'core/formularioDueñoEst.html',data)



def index(request):
    return render(request, 'core/index.html')

def tipoCuentas(request):
    return render(request, 'core/tipoCuentas.html')

def listadoEst(request):
    return render(request, 'core/listadoEst.html')

def perfil(request):
    user = User.objects.get(username=request.user)
    print(user.username)
    print(user.is_staff)
    if(user.is_staff):
        usuario = DuenoEstacionamiento.objects.get(nombreUsuario=user.username)
        estacionamiento = Estacionamiento.objects.filter(dueno_id=usuario.idDueno)
    else:
        usuario = ClienteArrendador.objects.get(nombreUsuario=user.username)
        estacionamiento = Estacionamiento.objects.filter(dueno_id=usuario.idArrendador)
    
    datos ={
       'usuario' : usuario,
       'estacionamiento': estacionamiento
    }
    return render(request, 'core/perfil.html',datos)



def registro (request):
    data = {
        'form' : CustomerUserCreationForm
    }
    if request.method == 'POST':
        formulario = CustomerUserCreationForm(data=request.POST)
        if formulario.is_valid():
            print(formulario.cleaned_data["username"])
            formulario.save()
            messages.success(request, "Te has registrado correctamente")
            user = authenticate(
                username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="index")
        data["form"] = formulario
    return render (request, 'registration/registro.html', data)