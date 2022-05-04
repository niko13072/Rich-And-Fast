class Factura():

    def __init__(self, Cambio=float, Pago=float):
        self.Cambio = Cambio
        self.Pago = Pago

    def ComprobarVenta(self):
        print("Venta realizada con exito")
        