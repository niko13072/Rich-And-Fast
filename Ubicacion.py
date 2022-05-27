class Ubicacion():

    Pais:str

    def __init__(self, Direccion=str, Ciudad=str):
        self.Direccion = Direccion
        self.Ciudad = Ciudad
        self.Pais = Pais
    
    def UbicarRestaurante(self):
        print("Ubicación del restaurante")
