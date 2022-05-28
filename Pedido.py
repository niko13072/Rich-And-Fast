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
        
list = []

list.append(Pedido('pedido', str.Perro, str.hamburguesa))
list.append(Pedido('caja', 6000))

list.append(Pedido('cantidadProducto', 3))
list.append(Pedido('valorUnitario', 8000))
list.append(Pedido('producto', str.perro))   

for obj in list:
    print( obj.Pedido, sep = ' ')
        