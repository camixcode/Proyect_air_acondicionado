from django.http import JsonResponse
from django.shortcuts import render
from .controller import Controller
from .libro import Libro
from .forms import CustomerUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect,render
from .Carrito import Carrito
from .producto import Producto
import webbrowser

from urllib.parse import urlparse

carrito={
    'nombre':'',
    'total':0
}

productosCarrito=[]

cantidad =[]
#Para recorrer los productos segun categoria hay que insertar en la lista al agregar un producto 
listaAnwo=[]
listaBodega=[]

# Create your views here.
def agregar_producto(request, producto_id):
    controller = Controller()
    producto = controller.buscarUnProducto(producto_id)
    p_producto = producto.precio_bruto
    carrito['total'] = carrito['total'] + producto.precio_bruto
    productosCarrito.append(producto)
    cant_pro={
        'id':producto.id_producto,
        'nombre':producto.nombre,
        'cant':1,
        'precio':producto.precio_bruto,
        'categoria':producto.categoria,

    }
    cantidad.append(cant_pro)
    listaBodega.append(cant_pro['id'])
    print(carrito['total'])
    return redirect("productos")


def agregar_producto_anwo(request, producto_id):
    controller = Controller()
    producto = controller.buscarUnProductoAnwo(producto_id)
    p_producto = producto.precio_bruto
    carrito['total'] = carrito['total'] + producto.precio_bruto
    productosCarrito.append(producto)
    cant_pro={
        'id':producto.id_producto,
        'nombre':producto.nombre,
        'cant':1,
        'precio':producto.precio_bruto,
        'categoria':producto.categoria,

    }
    cantidad.append(cant_pro)
    listaAnwo.append(cant_pro['id'])
    print(carrito['total'])
    return redirect("productos")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    controller = Controller()
    producto = controller.buscarUnProducto(producto_id)
    carrito.eliminar(producto)
    return redirect("productos")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    controller = Controller()
    producto = controller.buscarUnProductoAnwo(producto_id)
    carrito.restar(producto)
    return redirect("productos") 

def limpiar_carrito(request):
    productosCarrito.clear()
    cantidad.clear()
    carrito['total']=0
    return redirect("productos") 



def home(request):
     variable = {
          'productos': '',
          'det_libro': '',
          # 'lista':'',
          'mensaje':'',
          'preference_id':'',
          'paises':'',
     }

     controller = Controller()
     
     # det_libro = controller.mostrarUnLibro()
     try:
          paises = controller.buscarPaises()
          print(paises)
          variable['paises'] = controller.buscarPaises()
          # lista = controller.buscarTodo()
          listaProductos = controller.mostrarProductos()
          variable['productos']=listaProductos
          preferencias = controller.pagar()
          variable['preference_id']=preferencias["response"]["id"]
          # variable['lista']=lista
          # variable['det_libro']=det_libro
          variable['mensaje']='Con datos'

     except:
          variable['mensaje']='sin datos'

     return render(request,'core/home.html',variable)

def buscarLibro(request):
     controller = Controller()
     codigo = request.POST.get('codigo')
     libro = controller.buscarUnLibro(codigo)
     return JsonResponse({
          'codigo' : libro.id_producto,
          'nombre' : libro.nombre,
          'stock' : libro.stock,
          'precio': libro.precio,
          'autor' : libro.autor,
          'vigencia' : libro.vigencia
     })

def actualizarLibro(request):
     controller = Controller()
     codigo = request.POST.get('codigo_oculto')
     stock = request.POST.get('stock')
     resultado = controller.descontarStock(codigo,stock)
     return JsonResponse({
          'mensaje': resultado
     })

def buscarProducto(request):
     controller = Controller()
     codigo = request.POST.get('codigo')
     producto = controller.buscarUnProducto(codigo)
     return JsonResponse({
          'codigo' : producto.id_producto,
          'nombre' : producto.nombre,
          'stock' : producto.stock,
          'precio_bruto': producto.precio_bruto,
          'fecha_entrega' : producto.fecha_entrega,
          'categoria' : producto.categoria
     })

def actualizarStockProducto(request):
     controller = Controller()
     codigo = request.POST.get('codigo_oculto')
     stock = request.POST.get('stock')
     resultado = controller.descontarStockProducto(codigo,stock)
     return JsonResponse({
          'mensaje': resultado
     })

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
            return redirect(to="productos")
        data["form"] = formulario
    return render (request, 'registration/registro.html', data)


    

def productos(request):
#     instanciar variables para retornar
    variable = {
         'productos':'',
         'mensaje' : '',
         'productos_aw':'',
         'pais':'',
         'total':carrito['total'],
         'productos_carrito':cantidad,

    }
    controler = Controller()

    try:
         listaProductos = controler.mostrarProductos()
         listaProductosAw = controler.mostrarProductosAnwo()
         
         variable['productos'] = listaProductos + listaProductosAw
         
         variable['mensaje'] = 'Busqueda exitosa'
         url = ""
         url = str(request)
         aprovado="status=approved"
         if(aprovado in url):
             print("Estado Aprobado")
             descuentoStock=[]
             descuentoStock=cantidad
             print(descuentoStock)
             con=0
             for des in descuentoStock:
                 detalle={}
                 detalle=descuentoStock[con]
                 print(detalle['id'])
                 print(detalle['cant'])
                 con=+1
                 if(detalle['categoria']=="Bodega"):
                     print(detalle['categoria'])
                     controler.descontarStockProducto(detalle['id'],detalle['cant'])
                 elif(detalle['categoria']=="Anwo"):
                     print(detalle['categoria'])
                     controler.descontarStockProductoAnwo(detalle['id'],detalle['cant'])
                    
             productosCarrito.clear()

             cantidad.clear()
             carrito['total']=0


            #  print(cant_pro['id'])
            #  print(cant_pro['cant'])
             return redirect(to="productos")
         else:
             print("No hay pago")
             print(productosCarrito)
             print(cantidad)
         print("la url es : " , url)

         preferencias = controler.pagar(variable['total'])
         
         variable['preference_id']=preferencias["response"]["id"]
         
    except:
         variable['mensaje'] = 'Error productos no encontrados'
         
    return render(request, 'core/productos.html',variable)

def historialVenta(request):
     variable = {
          'preference_id':'',
     }

     controller = Controller()
     
     try:
          preferencias = controller.pagar()
          variable['preference_id']=preferencias["response"]["id"]
     except:
          variable['mensaje']='sin datos'

     return render(request,'core/historialVenta.html',variable)

def inicio(request):
    return render(request, 'core/inicio.html')

def adminServicios(request):
    return render(request, 'core/adminServicios.html')

def servicios(request):
    return render(request, 'core/servicios.html')

def adminProvInst(request):
    return render(request, 'core/adminProvInst.html')


def adminRoles (request):
    return render (request, 'core/adminRoles.html')

def cuentasUsuarios (request):
    return render (request, 'core/cuentasUsuarios.html')

def seguimientoCompra (request):
    return render (request, 'core/seguimientoCompra.html')

def estadoServicio (request):
    return render (request, 'core/estadoServicio.html')

def adminSolicitudServicios (request):
    return render (request, 'core/adminSolicitudServicios.html')