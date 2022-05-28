import Cliente


class Valoracion():

    comentario:str
    calificacion:int

    def __init__(self,cliente:Cliente):
        self.Cliente = cliente
    
    def UbicarRestaurante(self):
        return

list = []

list.append(Valoracion('numeroMesa',3))
list.append(Valoracion('nombre',str.Angelica,))
list.append(Valoracion('Pedido',2,'hamburguesas'))




for obj in list:
    print(obj.Valoracion, sep ='')

if __name__=='__main__':
    Valoracion1=Valoracion('Angelika')
    print(Valoracion1)
    


    
