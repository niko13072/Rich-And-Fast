import DetallePedido
class Pedido(DetallePedido):


    Fecha: str
    NumeroPedido: int
    pedidoCancelado: bool 
    PedidoListo: bool

    def __init__(self, Total:float, NumeroMesa:int, DetallePedido:DetallePedido):
        self.NumeroPedido = NumeroPedido
        self.Fecha = Fecha
        self.Total = Total
        self.NumeroMesa = NumeroMesa
        self.PedidoCancelado = PedidoCancelado
        self.PedidoLisro = PedidoListo
        self.DetallePedido = DetallePedido


    def ModificarPedido(self):
        print("Seleccione el producto a modificar")

    def RealizarPedido(self):
        print("RealizarPedido")
        