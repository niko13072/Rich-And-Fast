from Usuario import Usuario
from Valoracion import Valoracion


class Cliente(Usuario,Valoracion):

    def __init__(self,NumeroMesa=int,CodigoQr=str,Telefono=int):
        self.NumeroMesa = NumeroMesa
        self.CodigoQr = CodigoQr
        self.Telefono = Telefono
    
    def EscanearCodigo(self):
        print("escaneo codigo")
    
    def RealizarPedido(self):
        print("Su pedido es")
    
    def SeleccionarProducto(self):
        print("productos seleccionados")

        