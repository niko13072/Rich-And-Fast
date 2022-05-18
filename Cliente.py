from ast import Str
from Usuario import Usuario


class Cliente(Usuario):

    def __init__(self,Id,Cargo,Nombre,Documento,Edad,sexo,NumeroMesa:int,CodigoQr:Str,Telefono:int):
        super().__init__(Id,Cargo,Nombre,Documento,Edad,sexo)
        self.NumeroMesa = NumeroMesa
        self.CodigoQr = CodigoQr
        self.Telefono = Telefono
    
    def EscanearCodigo(self):
        print("escaneo codigo")
    
    def RealizarPedido(self):
        print("Su pedido es")
    
    def SeleccionarProducto(self):
        print("productos seleccionados")

        