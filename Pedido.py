import DetallePedido
import Factura

class Pedido():

    Factura: Factura
    Total:float
    PedidoListo:bool
    PedidoCancelado:bool
    NumeroPedido:int
    Fecha:str

    

    def __init__(self,detallePedido:DetallePedido,numeroMesa:int):
        self.DetallePedido = detallePedido
        self.NumeroMesa = numeroMesa
    
    def ModificarMenu(self):
        return
    
    def RealizarPedido(self):
        return
        
        

    
        