import string

class Reservas:

    def __init__(self, Fecha=string, Hora=float, NombreReserva=string, NumReserva=int)
       self.Fecha = Fecha
       self.Hora = Hora
       self.NombreReserva = NombreReserva
       self.NumReserva = NumReserva

    def EnviarNotificacion(self):
        print("Notificacion reserva")

    def CrearReserva(self):
        print("Crear la reserva")