from django.http import JsonResponse
from django.shortcuts import render
from .controller import Controller
from .libro import Libro

# Create your views here.
def home(request):
     variable = {
          'productos': '',
          'det_libro': '',
          # 'lista':'',
          'mensaje':''
     }

     controller = Controller()
     
     # det_libro = controller.mostrarUnLibro()
     try:
          # lista = controller.buscarTodo()
          listaProductos = controller.mostrarProductos()
          variable['productos']=listaProductos
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