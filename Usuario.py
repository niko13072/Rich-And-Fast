import Cliente
import Administrador


class Usuario():
   
     Cargo:str
     Documento:int
     Edad:int
     Sexo:str
     Nombre:str
     Cliente:Cliente
     Administrador:Administrador


     def __init__(self, id:int,contrasena:str):
             self.Id=id
             self.Contraseña=contrasena
             

                
     def VerificarUsuario(self):
         print("el usuario es valido")

     def ActualizarDatos(self):
         print("datos actualizados")

     def Registrar(self):
         print("Usuario Creado")

         return

list = []

list.append(Usuario('numeroMesa', 3))
list.append(Usuario('pedido', str.Hamburguesa))

for obj in list:
    print( obj.Usuario, sep = ' ')

        









    
