class Menu():

    def __init__(self, Nombre=str, Categoria=str):
        self.Nombre = Nombre
        self.Categoria = Categoria
        

    def MostrarProducto(self): 
        print(f"Nombre: ", self.NombreProducto, "Precio: " ,self.Precio, "Descripcion: ", self.Descripcion)

    def ModificarMenu(self):
        return (self.Nombre,self.Categoria)

   



    




    