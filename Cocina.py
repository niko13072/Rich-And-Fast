import Pedido
import Producto

class Cocina():

    def __init__(self,TiempoPreparacion=float,):
        self.Pedido = Pedido
        self.Producto = Producto
        self.TiempoPreparacion = TiempoPreparacion
        
    
    def PrepararPedido(self):
        print("Cocinando Pedido")
    
    def ConfirmarPedido(self):
        print("Pedido Listo")


        
        