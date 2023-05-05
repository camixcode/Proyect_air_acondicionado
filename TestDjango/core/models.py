from django.db import models

# Create your models here.


class Comuna(models.Model):
    idComuna = models.AutoField(primary_key=True, verbose_name='Id de comuna')
    descripcion = models.CharField(max_length=50, null=False,blank=False, verbose_name='Nombre de comuna')
    nombre = models.CharField(max_length=50, null=False,blank=False, verbose_name='Nombre comuna')

    
    def descripcion(self):
        return self.descripcion

class Banco(models.Model):
    idBanco = models.AutoField(primary_key=True, verbose_name='Id de banco')
    descripcion = models.CharField(max_length=50, null=False,blank=False, verbose_name='Nombre del banco')
    nombre = models.CharField(max_length=50, null=False,blank=False, verbose_name='Nombre banco')

    
    def descripcion(self):
        return self.descripcion

class Region(models.Model):
    idRegion = models.AutoField(primary_key=True, verbose_name='Id de region')
    descripcion = models.CharField(max_length=50, null=False,blank=False, verbose_name='Nombre de region')
    nombre = models.CharField(max_length=50, null=False,blank=False, verbose_name='Nombre region')

    
    def descripcion(self):
        return self.descripcion

class DuenoEstacionamiento(models.Model):
    idDueno = models.AutoField(primary_key=True, verbose_name='Id de dueño')
    nombreUsuario = models.CharField(unique=True,max_length=50, null=False,blank=False, verbose_name='Nombre de usuario')
    nombre = models.CharField(max_length=50, null=True,blank=False, verbose_name='Nombre')
    rut = models.CharField(unique=True,max_length=50, null=False,blank=False, verbose_name='Rut')
    p_apellido = models.CharField(max_length=50, verbose_name='Primer apellido')
    s_apellido = models.CharField(max_length=50, verbose_name='Segundo apellido')
    telefono = models.IntegerField(verbose_name='Telefono')
    direccion = models.CharField(max_length=50, verbose_name='Direccion')
    nombreCalle = models.CharField(max_length=50, verbose_name='Nombre calle')
    comuna = models.ForeignKey(Comuna,null=False,blank=False,on_delete=models.CASCADE)
    region = models.ForeignKey(Region,null=False,blank=False,on_delete=models.CASCADE)
    cuentaBancaria = models.CharField(max_length=50, verbose_name='Cuenta bancaria')
    correo = models.CharField(max_length=50, verbose_name='Correo')
    password = models.CharField(max_length=50, verbose_name='Password')

    def nombres(self):
        return self.nombres
    

class ClienteArrendador(models.Model):
    idArrendador = models.AutoField(primary_key=True, verbose_name='Id de cliente')
    nombreUsuario = models.CharField(unique=True,max_length=50, null=False,blank=False, verbose_name='Nombre de usuario')
    nombre = models.CharField(max_length=50, null=True,blank=False, verbose_name='Nombre')
    rut = models.CharField(unique=True,max_length=50, null=False,blank=False, verbose_name='Rut')    
    p_apellido = models.CharField(max_length=50, verbose_name='Primer apellido')
    s_apellido = models.CharField(max_length=50, verbose_name='Segundo apellido')
    telefono = models.IntegerField(verbose_name='Telefono')
    direccion = models.CharField(max_length=50, verbose_name='Direccion')
    comuna = models.ForeignKey(Comuna,null=False,blank=False,on_delete=models.CASCADE)
    region = models.ForeignKey(Region,null=False,blank=False,on_delete=models.CASCADE)
    banco = models.ForeignKey(Banco,null=False,blank=False,on_delete=models.CASCADE)
    tarjetaCredito = models.CharField(max_length=50, verbose_name='Tarjeta de credito')
    correo = models.CharField(max_length=50, verbose_name='Correo')
    password = models.CharField(max_length=50, verbose_name='Password')

    def nombres(self):
        return self.nombres
  
class Vehiculo (models.Model):
    idVehiculo = models.AutoField(primary_key=True,verbose_name="Id vehiculo")
    patente = models.CharField(max_length=50,null=False,blank=False, verbose_name='Patente')
    marca = models.CharField(max_length=50,null=False,blank=False, verbose_name='Marca')
    modelo = models.CharField(max_length=50,null=False,blank=False, verbose_name='Modelo')
    anio = models.IntegerField(null=False,blank=False, verbose_name='Año')
    duenoVehiculo = models.ForeignKey(ClienteArrendador,on_delete=models.PROTECT)

    def dueño(self):
        return self.duenoVehiculo.nombres

    
class Estacionamiento(models.Model):
    idEstacionamiento = models.AutoField(primary_key=True, verbose_name='Id de estacionamiento')
    precio = models.IntegerField(null=False,blank=False,verbose_name='Precio')
    dueno = models.ForeignKey(DuenoEstacionamiento,on_delete=models.PROTECT)
    estado = models.CharField(max_length=20,null=False,blank=False,verbose_name="Estado")
    horario = models.CharField(max_length=20, null=True, blank=False,verbose_name="Horario")  
    direccionEst = models.CharField(max_length=50,null=True,blank=False, verbose_name='Direccion')
    comuna = models.ForeignKey(Comuna,on_delete=models.PROTECT)

    def direccion(self):
        return self.direccionEst
    
class Arriendo(models.Model):
    idArriendo = models.AutoField(primary_key=True,verbose_name="Id Arriendo")
    fechaInicio = models.CharField(max_length=50,null=False,blank=False,verbose_name="Fecha incio")
    fechaTermino = models.CharField(max_length=50,null=False,blank=False,verbose_name="Fecha termino")
    total = models.IntegerField(null=False,blank=False,verbose_name="Total")
    precioXhora = models.IntegerField(null=False,blank=False,verbose_name="Precio por hora")
    
    def total(self):
        return self.total