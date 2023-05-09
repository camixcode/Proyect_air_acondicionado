from django.shortcuts import render
from .controller import Controller

# Create your views here.
def home(request):
     variable = {
          'mensaje': ''
     }
     variable['mensaje'] = 'HOLI'
     return render(request,'core/home.html',variable)