import Pedido
import Caja

class Factura():

    Pago:float

    def __init__(self, Cambio:float, Pedido:Pedido,caja:Caja):
        self.Cambio = Cambio
        self.Pedido = Pedido
        self.Caja= caja
        
    def ComprobarVenta(self):
        print("Venta realizada con exito")





    
        