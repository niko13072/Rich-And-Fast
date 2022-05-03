from Pedido import Pedido

class Factura(Pedido, cliente):

    def __init__(self, Cambio=float, Pago=float):
        self.Cambio = Cambio
        self.Pago = Pago

    def ComprobarVenta(self):
        print("comprobar venta")
        