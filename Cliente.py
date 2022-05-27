from Usuario import Usuario


class Cliente(Usuario):

    CodigoQr:str
    Telefono:int

    def __init__(self,numeroMesa:str, nombre:str, id:str):
        super().__init__()
        self.NumeroMesa = numeroMesa
       
    def EscanearCodigo(self):
         print("escaneo codigo")
    
    def RealizarPedido(self):
         print("Su pedido es")
    
    def SeleccionarProducto(self):
         print("productos seleccionados")
