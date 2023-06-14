from django.db import models

# Create your models here.
class Servicio(models.Model):
    idServicio = models.IntegerField(primary_key=True, verbose_name='Id de servicio')
    nombreServicio = models.CharField(max_length=50,verbose_name='Nombre de la servicio')
    descripcion = models.CharField(max_length=400,verbose_name='descripcion')

    def __str__(self):
        return self.nombreServicio
    
class Proveedor(models.Model):
    idProveedor = models.IntegerField(primary_key=True, verbose_name='Id de Proveedor')
    rut = models.CharField(max_length=50,verbose_name='Rut de  Proveedor')
    nombreProveedor = models.CharField(max_length=50,verbose_name='Nombre de la Proveedor')
    descripcion = models.CharField(max_length=400,verbose_name='descripcion')
    direccion = models.CharField(max_length=400,verbose_name='direccion')
    correo = models.CharField(max_length=400,verbose_name='correo')
    especializacion = models.CharField(max_length=400,verbose_name='especializacion')
    detalle = models.CharField(max_length=400,verbose_name='detalle')


    def __str__(self):
        return self.nombreServicio
   