from Usuario import Usuario


class Administrador(Usuario):
 
    def __init__(self,id,contrasena,email:str):
        super().__init__(id,contrasena)
        self.Email = email
    
    def AdministrarRestaurante(self):
        print("Restaurante Administrado")
    
    def PagarNomina(self):
        print("Nomina Pagada")

    def ActualizarProductos(self):
        print("Producto Actualizado")

    def ActualizarPrecios(self):
        print("precio actualizado")
    


