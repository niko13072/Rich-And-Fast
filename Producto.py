class Producto(): # aqui va el numero de la clase, si depronto ella hereda de otra se coloca entre parentesis (de quien hereda)
    
    Descripcion=str

    def __init__(self, nombreProducto:str, precio:float): # aqui se definen los atributos
        self.NombreProducto = nombreProducto # aqui se coloca tambien cada uno 
        self.Precio = precio
        
    
    def CrearProducto(self):  #estas son los metodos o las funciones de las clase les puse un print por que ahi se debe mirar que hace cada clase
        print("Datos del nuevo Prodcuto")
    
    def SeleccionarProducto(self):
        print("Nombre del producto a seleccionar")
    
    def EliminarProducto():
        print("selecione el producto a eliminar")
    
    
if __name__ == '__main__':
    producto1 = Producto('Hamburguesa','Pizza')
    print(producto1)
    producto2 =Producto('Gaseosa','Jugos')
    print(producto2) 























    
