from numpy import array
import Producto
import Pedido

class Cocina():

    Producto:Producto

    def __init__(self,tiempoPreparacion:float,pedido:Pedido):
        self.TiempoPreparacion = tiempoPreparacion
        self.Pedido=pedido
       

    
    def PrepararPedido(self):
        print("Cocinando Pedido")
    
    def ConfirmarPedido(self):
        if self.Pedido == True:
            print("Pedido confirmado")
        else:
            print("Corregir pedido")

list = []

list.append(Cocina('nombreProducto', str.Hamburguesa))
list.append(Cocina('precio', 8000))

list.append(Cocina('detallePedido', str.Hamburguesa, str.perro))
list.append(Cocina('numeroMesa', 3))

for obj in list:
    print( obj.Cocina, sep =' ')

if __name__=='__main__':
    cocina1 = Cocina(15,'2 pizzas')
    print(cocina1)
        
        