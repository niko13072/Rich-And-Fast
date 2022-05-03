import string


class MedioDePago:

    def __init__(self, Efectivo = bool, Tarjeta=bool):
        self.Efectivo = Efectivo
        self.Tarjeta = Tarjeta

    def PagarFactura(self):
        print("Seleccionar factura a pagar")
        

