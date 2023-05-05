from django.urls import path
from.views import formularioCliente, index,registro, tipoCuentas, formularioDueñoEst, perfil,listadoEst

urlpatterns = [
    path('', index, name="index"),
    path('registro',registro, name="registro"),
    path('tipoCuentas',tipoCuentas, name="tipoCuentas"),
    path('formularioCliente',formularioCliente, name="formularioCliente"),
    path('formularioDueñoEst',formularioDueñoEst, name="formularioDueñoEst"),
    path('perfil',perfil, name="perfil"),
    path('listadoEst',listadoEst, name="listadoEst")


    ]