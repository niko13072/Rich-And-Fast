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

list.append(Caja('id',1005813642))
list.append(Caja('constraseña', 1020) )


for obj in list:
    print( obj.Caja, sep =' ')

if __name__=='__main__':
    