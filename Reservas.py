from Usuario import Usuario

class Reservas():
    NumReserva:int

    def __init__(self, Fecha:str, Hora:float, NombreReserva:str, usuario:Usuario):
       self.Fecha = Fecha
       self.Hora = Hora
       self.NombreReserva = NombreReserva
       self.Usuario = usuario

    def EnviarNotificacion(self):
        print("Notificacion reserva")

    def CrearReserva(self):
        print("Crear la reserva")
        
if __name__=='__main__':
    Reserva1=Reservas(10,2,'Cumpleaños','Karen')
    print(Reserva1)