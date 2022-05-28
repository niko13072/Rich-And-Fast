from numpy import array
import Producto
import Pedido

class Cocina():

    Producto:Producto

    def __init__(self,TiempoPreparacion:float,pedido:Pedido):
        self.TiempoPreparacion = TiempoPreparacion
        self.Pedido=pedido
       

    
    def PrepararPedido(self):
        print("Cocinando Pedido")
    
    def ConfirmarPedido(self):
        print("Pedido Listo")
        return

list = []

list.append(Cocina('nombreProducto', str.Hamburguesa))
list.append(Cocina('precio', 8000))

list.append(Cocina('detallePedido', str.Hamburguesa, str.perro))
list.append(Cocina('numeroMesa', 3))

for obj in list:
    print( obj.Cocina, sep =' ')


        
        