from Pedido import Pedido

class Cocina(Pedido):

    def __init__(self,TiempoPreparacion=float,PedidoListo=bool,PedidoCancelado=bool):
        self.TiempoPreparacion = TiempoPreparacion
        self.PedidoListo = PedidoListo
        self.PedidoCancelado = PedidoCancelado
    
    def PrepararPedido(self):
        print("Cocinando Pedido")
    
    def ConfirmarPedido(self):
        print("Pedido Listo")


        
        