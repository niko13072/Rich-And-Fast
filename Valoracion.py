import Cliente

class Valoracion():

    comentario:str
    calificacion:int

    def __init__(self,cliente:Cliente):
        self.Cliente = cliente
    
    def UbicarRestaurante(self):
        return

list = []

list.append(Cliente())
list.append(Cliente('calificacion', 10) )
list.append(Cliente('Cliente:cliente', 2) )

for obj in list:
    print(obj.calificacion, obj.comentario, obj.Cliente:cliente, sep =' ')

    
