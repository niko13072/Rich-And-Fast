from Usuario import Usuario

class Reservas():
    NumReserva:int

    def __init__(self, fecha:str, hora:float, nombreReserva:str, usuario:Usuario):
       self.Fecha = fecha
       self.Hora = hora
       self.NombreReserva = nombreReserva
       self.Usuario = usuario

    def EnviarNotificacion(self):
        print("Notificacion reserva")

    def CrearReserva(self):
        print("Crear la reserva")
        
if __name__=='__main__':
    Reserva1=Reservas(10,2,'Cumpleaños','Karen')
    print(Reserva1)