from mimetypes import init


class Restaurante():

    cantidadMesas:int
    cantidadEmpleados:int

    def __init__(self,nombreRestaurante:str):
        self.NombreRestaurante = nombreRestaurante
        
    

    def GenerarVentas(self):
        print("las ventas fueron")
