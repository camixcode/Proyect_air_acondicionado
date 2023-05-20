from django.http import JsonResponse
from django.shortcuts import render
from .controller import Controller
from .libro import Libro

# Create your views here.
def home(request):
     variable = {
          'libros': '',
          'det_libro': '',
          'lista':'',
          'mensaje':''
     }

     controller = Controller()
     listaLibros = controller.mostrarLibros()
     # det_libro = controller.mostrarUnLibro()
     try:
          lista = controller.buscarTodo()

          variable['libros']=listaLibros
          variable['lista']=lista
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