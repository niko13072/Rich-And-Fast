from Usuario import Usuario


class Administrador(Usuario):
 
    def __init__(self,id,password,documento,email:str):
        super().__init__(id,password,documento)
        self.Email = email
    
    def AdministrarRestaurante(self):
        print("Restaurante Administrado")
    
    def PagarNomina(self):
        print("Nomina Pagada")

    def ActualizarProductos(self):
        print("Producto Actualizado")

    def ActualizarPrecios(self):
        print("precio actualizado")
    
    
    


    
    


