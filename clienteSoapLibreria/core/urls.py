from django.urls import path
from .views import agregar_producto, eliminar_producto, historialVenta, home,buscarLibro,actualizarLibro,buscarProducto,actualizarStockProducto, inicio, limpiar_carrito, productos, registro , adminServicios, restar_producto, servicios

urlpatterns = [
    path('', home, name='home'),
    path('post/ajax/buscar/',buscarLibro, name='post_buscar'),
    path('post/ajax/actualizar/',actualizarLibro, name='post_actualizar'),
    path('post/ajax/buscar_producto/',buscarProducto, name='post_buscar_producto'),
    path('post/ajax/actualizar_producto/',actualizarStockProducto, name='post_actualizar_producto'),
    path('registro',registro, name="registro"),
    path('productos',productos, name="productos"),
    path('historialVenta',historialVenta, name="historialVenta"),
    path('inicio',inicio, name="inicio"),
    path('adminServicios',adminServicios, name="adminServicios"),
    path('agregar_producto/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="del"),
    path('restar/<int:producto_id>/', restar_producto, name="sub"),
    path('limpiar/', limpiar_carrito, name="cls"),
    path('servicios/', servicios, name="servicios"),



]