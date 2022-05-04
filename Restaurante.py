class Restaurante():

    def __init__(self,NombreRestaurante=str,CantidadMesas=int,CantidadEmpleados=int,):
        self.NombreRestaurante = NombreRestaurante
        self.CantidadMesas = CantidadMesas
        self.CantidadEmpleados = CantidadEmpleados

    def GenerarVentas(self):
        print("las ventas fueron")
