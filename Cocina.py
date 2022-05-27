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


        
        