import Pedido
import Caja

class Factura():

    Pago:float
    Cambio:float

    def __init__(self, pedido:Pedido,caja:Caja):
        self.Pedido = pedido
        self.Caja= caja
        
    def ComprobarVenta(self):
        print("Venta realizada con exito")
        return

list = []

list.append(Factura('detallePedido', str.Hamburguesa, str.perro))
list.append(Factura('numeroMesa', 3))

for obj in list:
    print( obj.Factura, sep = ' ')

if __name__=='__main__':
    Factura1= Factura('Pedido','caja')
    print(Factura1)





    
        