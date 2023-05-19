from django.urls import path
from .views import home,buscarLibro,actualizarLibro

urlpatterns = [
    path('', home, name='home'),
    path('post/ajax/buscar/',buscarLibro, name='post_buscar'),
    path('post/ajax/actualizar/',actualizarLibro, name='post_actualizar'),


]