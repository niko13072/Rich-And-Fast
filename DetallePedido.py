
import Producto

class DetallePedido():


    def __init__(self,CantidadProducto=int,ValorUnitario=float,producto=Producto):
        self.CantidadProducto = CantidadProducto
        self.ValorUnitario = ValorUnitario
        self.Producto=producto

    def CalcularPrecio(self):
        print("Precio")
        

