import Usuario

class Caja():
    dineroCaja:float
    medioDePago:float
       
    def __init__(self, usuario:Usuario):
        self.Usuario = usuario

    def CalcularCambio(self):
        print("su cambio es")
    
    def GenerarFactura(self):
        print("Factura")
        return

list = []

list.append(Usuario())
list.append(Usuario('calificacion', 10) )
list.append(Usuario('Cliente:cliente', 2) )

for obj in list:
    print(obj.calificacion, obj.comentario, obj.Cliente:cliente, sep =' ')