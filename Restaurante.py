from mimetypes import init


class Restaurante():

    CantidadMesas:int
    CantidadEmpleados:int

    def __init__(self,NombreRestaurante=str):
        self.NombreRestaurante = NombreRestaurante
        self.CantidadMesas = CantidadMesas
        self.CantidadEmpleados = CantidadEmpleados

    def GenerarVentas(self):
        print("las ventas fueron")
