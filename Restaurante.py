from mimetypes import init
from tkinter import Menu


class Restaurante():

    nombreRestaurante:str

    def _init_(self, cocina:Cocina, cantidadMesas:int, cantidadEmpleados:int, valoracion:Valoracion, administrador:Administrador, reserva:Reserva, ubicacion:Ubicacion, menu:Menu, caja:Caja ):

        self.Cocina = cocina
        self.Ubicacion = ubicacion 
        self.Menu = menu
        self.Caja = caja
        self.CantidadMesas = cantidadMesas
        self.CantidadEmpleados = cantidadEmpleados
        self.Valoracion = valoracion
        self.Administrador = administrador
        self.Reserva = reserva
    

    def GenerarVentas(self):
        print("las ventas fueron")
        return

list = []

list.append(Restaurante('cliente',str.Valeria))

list.append(Restaurante('producto',str.Hamburguesa))

list.append(Restaurante('fecha',12))
list.append(Restaurante('hora',3))
list.append(Restaurante('nombreReserva',str.Valeria))
list.append(Restaurante('usuario',str.Valeria1205))

for obj in list:
    print(obj.Restaurante, sep ='')

