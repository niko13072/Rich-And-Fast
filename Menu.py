import Producto

class Menu():

    Categoria:str

    def __init__(self,producto:Producto):
        self.Producto = producto

    def MostrarProducto(self): 
        print(f"Nombre: ", self.NombreProducto, "Precio: " ,self.Precio, "Descripcion: ", self.Descripcion)

    def ModificarMenu(self):
        return (self.Nombre,self.Categoria)

   
list = []

list.append(Menu('nombreProducto',str.Hamburguesa))
list.append(Menu('precio', 8000))

for obj in list:
    print( obj.Menu, sep = ' ')

if __name__=='__main__':
    Menu1=Menu('hamburguesa')
    print(Menu1)


    




    