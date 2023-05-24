class Producto:
    id_producto=0
    nombre=''
    precio_bruto=''
    stock=''
    fecha_entrega=''
    categoria=''
    imagen = ''
    
    def __init__(self,id_producto,nombre,precio_bruto,stock,fecha_entrega,categoria,imagen):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio_bruto
        self.stock = stock
        self.fecha_entrega = fecha_entrega
        self.categoria = categoria
        self.imagen = imagen

    
    def libroArr(self):
        return{
            'codigo':self.id_producto,
            'nombre': self.nombre,
            'precio_bruto': self.precio_bruto,
            'stock': self.stock,
            'fecha_entrega':self.fecha_entrega,
            'categoria':self.categoria,
            'imagen' : self.imagen
        }
    
    def __str__(self):
        return'codigo '+self.id_producto + 'nombre '+ self.nombre+'precio_bruto'+ self.precio_bruto+ 'stock'+ self.stock+ 'fecha_entrega'+self.fecha_entrega+'categoria'+self.categoria