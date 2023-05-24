from django.urls import path
from .views import historialVenta, home,buscarLibro,actualizarLibro,buscarProducto,actualizarStockProducto, productos, registro

urlpatterns = [
    path('', home, name='home'),
    path('post/ajax/buscar/',buscarLibro, name='post_buscar'),
    path('post/ajax/actualizar/',actualizarLibro, name='post_actualizar'),
    path('post/ajax/buscar_producto/',buscarProducto, name='post_buscar_producto'),
    path('post/ajax/actualizar_producto/',actualizarStockProducto, name='post_actualizar_producto'),
    path('registro',registro, name="registro"),
    path('productos',productos, name="productos"),
    path('historialVenta',historialVenta, name="historialVenta"),



]