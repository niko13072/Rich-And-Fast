
import Producto

class DetallePedido():


    def __init__(self,cantidadProducto:int,valorUnitario:float,producto:Producto):
        self.CantidadProducto = cantidadProducto
        self.ValorUnitario = valorUnitario
        self.Producto=producto

    def CalcularPrecio(self):
        print("Precio")
        return

list = []

list.append(DetallePedido('nombreProducto', str.Hamburguesa))
list.append(DetallePedido('precio', 8000))

for obj in list:
    print( obj.DetallePedido, sep = ' ')

if __name__=='__main__':
    DetallePedido1 = DetallePedido(3,15000,'Hamburguesa')
    print(DetallePedido1)
    