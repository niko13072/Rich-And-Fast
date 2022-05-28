class Ubicacion():

    def __init__(self, direccion:str, ciudad:str,pais:str):
        self.Direccion = direccion
        self.Ciudad = ciudad
        self.Pais = pais
    
    def UbicarRestaurante(self):
        print("Ubicación del restaurante")

if __name__=='__main__':
    Ubicacion1=Ubicacion('kr25 #29 35','Manicales')
    print(Ubicacion1)