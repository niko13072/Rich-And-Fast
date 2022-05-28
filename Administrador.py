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
    
if __name__=='__main__':
    administrador1 = Administrador('100581364','contrasena','richandfast@gmail.com')
    

