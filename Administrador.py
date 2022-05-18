from Usuario import Usuario


class Administrador(Usuario):
 
    def __init__(self,Id,password,Cargo,Nombre,Documento,Edad,Sexo,Email=str):
        super().__init__(Id,password,Cargo,Nombre,Documento,Edad,Sexo)
        self.Email = Email

    def ActualizarProductos(self):
        print("Producto Actualizado")

    def ActualizarPrecios(self):
        print("precio actualizado")
    
    
    


    
    


