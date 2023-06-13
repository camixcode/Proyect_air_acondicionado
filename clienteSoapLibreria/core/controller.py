from zeep import Client
from .libro import Libro
from .producto import Producto
# SDK de Mercado Pago
import mercadopago






class Controller:
    wsdl= 'http://localhost:8080/Soap/aireAcondicionado?wsdl'
    cliente = Client(wsdl)

# WSDL RUTA QUE SE ENTREGA 
    wsdl2= 'http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL'
    cliente2 = Client(wsdl2)

# Metodos que tiene el WebService

    def buscarPaises(self):
        # Metodo de web service tiene que llamarse igual 
        paises = self.cliente2.service.FullCountryInfoAllCountries()
        return paises
    
    def sumar(self):
        resultado = self.cliente.service.sumar(3,4)
        return resultado
    
    def mostrarLibros(self):
        resultado = self.cliente.service.consultarLibros()
        return resultado
    
    def mostrarUnLibro(self):
        libro = self.cliente.service.consultarunLibro(id)
        return libro
    
    def buscarUnLibro(self, cod):
        libro = self.cliente.service.consultarunLibro(cod)
        return libro
    
    def descontarStock(self,cod,stock):
        resultado = self.cliente.service.actualizarStock(cod,stock)
        return resultado
    
    # def buscarTodo(self):
    #     listaLibro =[]
    #     lista = self.cliente.service.consultarLibros()
    #     for i in range (len(lista)):
    #         libro = Libro(lista[i]['id_producto'],
    #                       lista[i]['nombre'],
    #                       lista[i]['precio'],
    #                       lista[i]['stock'],
    #                       lista[i]['autor'],
    #                       lista[i]['vigencia']
    #                       )
    #         listaLibro.append(libro)
    #     return listaLibro
    

    # Web service Bodega


    def mostrarProductos(self):
        resultado = self.cliente.service.consultarProductos()
        return resultado
    

    def buscarUnProducto(self, cod):
        producto = self.cliente.service.consultarUnProducto(cod)
        return producto
    
    def descontarStockProducto(self,cod,stock):
        resultado = self.cliente.service.actualizarStockProducto(cod,stock)
        return resultado
    

     # Web service Anwo


    def mostrarProductosAnwo(self):
        resultado = self.cliente.service.consultarProductosAnwo()
        return resultado
    

    def buscarUnProductoAnwo(self, cod):
        producto = self.cliente.service.consultarUnProductoAnwo(cod)
        return producto
    
    def descontarStockProductoAnwo(self,cod,stock):
        resultado = self.cliente.service.actualizarStockProductoAnwo(cod,stock)
        return resultado
    
    def pagar(self,total):
        # Agrega credenciales
        sdk = mercadopago.SDK("TEST-8089418270941450-052521-0d2b104ed9c05b1dd8dbdd973340f776-1381512793")

        # Crea un ítem en la preferencia
        preference_data = {
            "items": [
                {
                    "title": "aireAcondionado",
                    "quantity": 1,
                    "unit_price": total
                },

            ],
                "back_urls": {
                            "success": "http://127.0.0.1:8000/productos",
                            "failure": "http://127.0.0.1:8000/productos",
                            "pending": "http://127.0.0.1:8000/productos"
                            },
                "auto_return": "approved"

        }

        preference_response = sdk.preference().create(preference_data)
        #preference = preference_response["response"]
        return preference_response

