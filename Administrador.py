from Usuario import Usuario


class Administrador(Usuario):

    def __init__(self, Email=str):
        self.Email = Email

    def ActualizarProductos(self):
        print("Producto Actualizado")

    def ActualizarPrecios(self):
        print("precio actualizado")
    
    
    


    
    


