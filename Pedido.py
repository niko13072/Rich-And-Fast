


class Pedido():

    def __init__(self, NumeroPedido=int, Fecha=str, Total=float, NumeroMesa=int):
        self.NumeroPedido = NumeroPedido
        self.Fecha = Fecha
        self.Total = Total
        self.NumeroMesa = NumeroMesa

    def ModificarPedido(self):
        print("Seleccione el producto a modificar")

    def RealizarPedido(self):
        print("RealizarPedido")
        