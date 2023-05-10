from zeep import Client

class Controller:
    wsdl= 'http://localhost:8080/Soap/aireAcondicionado?wsdl'
    cliente = Client(wsdl)

    def sumar(self):
        resultado = self.cliente.service.sumar(3,4)
        return resultado
    
    def mostrarLibros(self):
        resultado = self.cliente.service.consultarLibros()
        return resultado
