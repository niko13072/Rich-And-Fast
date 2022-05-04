import imp
from Pedido import Pedido

class Factura(Pedido):

    def __init__(self, Cambio=float, Pago=float):
        self.Cambio = Cambio
        self.Pago = Pago

    def ComprobarVenta(self):
        print("Venta realizada con exito")
        