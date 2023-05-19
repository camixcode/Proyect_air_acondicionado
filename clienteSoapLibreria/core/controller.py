from zeep import Client
from .libro import Libro

class Controller:
    wsdl= 'http://localhost:8080/Soap/aireAcondicionado?wsdl'
    cliente = Client(wsdl)

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
    
    def buscarTodo(self):
        listaLibro =[]
        lista = self.cliente.service.consultarLibros()
        for i in range (len(lista)):
            libro = Libro(lista[i]['id_producto'],
                          lista[i]['nombre'],
                          lista[i]['precio'],
                          lista[i]['stock'],
                          lista[i]['autor'],
                          lista[i]['vigencia']
                          )
            listaLibro.append(libro)
        return listaLibro

