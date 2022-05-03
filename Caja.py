from DetallePedido import DetallePedido
from MedioDePago import MedioDePago
from Usuario import Usuario

class Caja(DetallePedido,Usuario,MedioDePago):
    def __init__(self, Cambio=float,Pago=float):
        self.Cambio = Cambio
        self.Pago = Pago


    def CalcularCambio(self):
        print("su cambio es")
    
    def GenerarFactura(self):
        print("Factura")