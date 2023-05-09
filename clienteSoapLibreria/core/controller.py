from zeep import Client

class Controller:
    wsdl= 'http://localhost:8080/Soap/SoapTest?wsdl'
    cliente = Client(wsdl)

    def sumar(self):
        resultado = self.cliente.servicio.sumar(3,4)
        return resultado
