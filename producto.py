class Producto():
    def __init__(self,nombre,precio_base,stock):
        self.nombre=nombre
        self.precio_base=precio_base
        self.stock=stock
    
    def aplicar_descuento(self,porcentaje):
        self.precio_base*=(1-porcentaje)
        print (f"el nuevo precio del producto {self.nombre} es: {self.precio_base}")
    
    
    def actualizar_stock(self,cantidad):
        if (self.stock+cantidad)<0:
            print("no hay suficiente stock")
        else:
           self.stock+=cantidad
           print(f"el nuuevo stock de {self.nombre} es {self.stock}")

class Categoria(): 
    def __init__(self,nombre_categoria):
        self.nombre_categoria= nombre_categoria
        self.lista=[]

    def agregar_producto(self,producto):
        self.lista.append(producto)
        print(f"El producto {producto.nombre} se agrego a la lista")

    def valor_total_categoria(self):
        suma=0
        for m in self.lista:
            suma+=m.precio_base*m.stock
        print(f"El precio total {self.nombre_categoria} es {suma} pesos")