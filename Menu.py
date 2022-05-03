from Producto import Producto


class Menu(Producto):

    def __init__(self, Nombre, Categoria):
        self.Nombre = Nombre
        self.Categoria = Categoria
        

    def MostrarProducto(self): 
        print(f"Nombre: ", self.NombreProducto, "Precio: " ,self.Precio, "Descripcion: ", self.Descripcion)

    def ModificarMenu(self):
        return (self.Nombre,self.Categoria)

    print("1")



    




    