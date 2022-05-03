from Pedido import Pedido

class DetallePedido(Pedido):

    #constructor
    def __init__(self,CantidadProducto=int,ValorUnitario=float):
        self.CantidadProducto = CantidadProducto
        self.ValorUnitario = ValorUnitario

    def CalcularPrecio(self):
        print("Precio")
        

