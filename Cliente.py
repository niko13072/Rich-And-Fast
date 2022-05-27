from ast import Str
from Usuario import Usuario


class Cliente(Usuario):

    CodigoQr:Str
    Telefono:int

        def __init__(self,numeroMesa):
            super().__init__()
            self.NumeroMesa = numeroMesa
       
        def EscanearCodigo(self):
         print("escaneo codigo")
    
        def RealizarPedido(self):
         print("Su pedido es")
    
        def SeleccionarProducto(self):
         print("productos seleccionados")

        