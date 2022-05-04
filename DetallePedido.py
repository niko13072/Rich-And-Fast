from Producto import Producto

class DetallePedido(Producto):

    #constructor
    def __init__(self,CantidadProducto=int,ValorUnitario=float):
        self.CantidadProducto = CantidadProducto
        self.ValorUnitario = ValorUnitario

    def CalcularPrecio(self):
        print("Precio")
        

