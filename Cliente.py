from Usuario import Usuario
import Pedido


class Cliente(Usuario):

    CodigoQr:str
    Telefono:int


    def __init__(self,numeroMesa:str, pedido:Pedido):
        super().__init__(id)
        self.NumeroMesa = numeroMesa
        self.Pedido = pedido
      
       
    def EscanearCodigo(self):
         print("escaneo codigo") 
    
    def RealizarPedido(self):
         print("Su pedido es")
    
    def SeleccionarProducto(self):
         print("productos seleccionados")
