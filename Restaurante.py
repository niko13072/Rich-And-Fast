from mimetypes import init
from tkinter import Menu


class Restaurante():

    cantidadMesas:int
    cantidadEmpleados:int
    Valoracion:Valoracion
    Administrador:Administrador
    Reserva:Reserva

    def __init__(self,nombreRestaurante:str, cocina:cocina, ubicacion:ubicacion, menu:menu, caja:caja ):
        self.NombreRestaurante = nombreRestaurante
        self.Cocina = cocina
        self.Ubicacion = Ubicacion 
        self.Menu = Menu
        self.Caja = Caja
    

    def GenerarVentas(self):
        print("las ventas fueron")
        return

list = []

list.append(Restaurante('cliente',str.Valeria))

list.append(Restaurante('producto',str.Hamburguesa))

list.append(Restaurante('fecha', str.12enero))
list.append(Restaurante('hora',str.3pm))
list.append(Restaurante('nombreReserva',str.Valeria))
list.append(Restaurante('usuario',str.Valeria1205))

for obj in list:
    print(obj.Restaurante, sep ='')

