
import Producto

class DetallePedido():


    def __init__(self,cantidadProducto:int,valorUnitario:float,producto:Producto):
        self.CantidadProducto = cantidadProducto
        self.ValorUnitario = valorUnitario
        self.Producto=producto

    def CalcularPrecio(self):
        print("Precio")
        

