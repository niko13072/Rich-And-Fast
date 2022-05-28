from mimetypes import init
from tkinter import Menu


class Restaurante():

    cantidadMesas:int
    cantidadEmpleados:int
    valoracion:Valoracion
    vdministrador:Administrador
    reserva:Reserva

    def __init__(self,nombreRestaurante:str, cocina:Cocina, ubicacion:Ubicacion, menu:Menu, caja:caja ):
        self.NombreRestaurante = nombreRestaurante
        self.Cocina = cocina
        self.Ubicacion = ubicacion 
        self.Menu = Menu
        self.Caja = caja
    

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

