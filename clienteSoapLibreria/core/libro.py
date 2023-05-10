class Libro:
    id_producto=0
    nombre=''
    precio=''
    stock=''
    autor=''
    vigencia=''
    
    def __init__(self,id_producto,nombre,precio,stock,autor,vigencia):
        self.id_producto= id_producto
        self.nombre=nombre
        self.precio = precio
        self.stock = stock
        self.autor = autor
        self.vigencia = vigencia

    
    def libroArr(self):
        return{
            'codigo':self.id_producto,
            'nombre': self.nombre,
            'precio': self.precio,
            'stock': self.stock,
            'autor':self.autor,
            'vigencia':self.vigencia
        }
    
    def __str__(self):
        return'codigo '+self.id_producto + 'nombre '+ self.nombre+'precio'+ self.precio+ 'stock'+ self.stock+ 'autor'+self.autor+'vigencia'+self.vigencia