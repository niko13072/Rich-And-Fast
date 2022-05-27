from Cliente import Cliente


class Valoracion():

    def __init__(self,calificacion:int,comentario:str,cliente:Cliente):
        self.Calificacion = calificacion
        self.Comentario = comentario
        self.Cliente = cliente

    def CalificarServicio(self):
        print("Comentario")

        "ANA"