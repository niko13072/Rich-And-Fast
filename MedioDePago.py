class MedioDePago():

    Efectivo:bool


    def __init__(self, tarjeta:bool):
        self.Tarjeta = tarjeta

    def PagarFactura(self):
        print("Confirmar el pago")
        
if __name__=='__main__':
    MedioDePago1=MedioDePago(158528466645)
    print(MedioDePago1)
