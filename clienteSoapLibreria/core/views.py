from django.shortcuts import render
from .controller import Controller

# Create your views here.
def home(request):
     variable = {
          'mensaje': ''
     }

     controller = Controller()
     suma = controller.mostrarLibros()


     variable['mensaje']=suma

     return render(request,'core/home.html',variable)