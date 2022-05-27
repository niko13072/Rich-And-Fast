import Pedido

class Factura(Pedido):

    def __init__(self, Cambio:float, Pago:float, Peido:Pedido):
        self.Cambio = Cambio
        self.Pago = Pago
        self.Pedido = Pedido
        
    def ComprobarVenta(self):
        print("Venta realizada con exito")


list = [] 

list.append(pedido())


    
        