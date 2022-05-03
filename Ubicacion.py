import string

class Ubicacion:

    def __init__(self, Direccion=string, Ciudad=string, Pais=string):
        self.Direccion = Direccion
        self.Ciudad = Ciudad
        self.Pais = Pais
    
    def UbicarRestaurante(self):
        print("Ubicación del restaurante")
