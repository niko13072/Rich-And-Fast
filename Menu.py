import Producto

class Menu():

    Categoria:str

    def __init__(self,producto:Producto):
        self.Producto = producto

    def MostrarProducto(self): 
        print(f"Nombre: ", self.NombreProducto, "Precio: " ,self.Precio, "Descripcion: ", self.Descripcion)

    def ModificarMenu(self):
        return (self.Nombre,self.Categoria)

   



    




    