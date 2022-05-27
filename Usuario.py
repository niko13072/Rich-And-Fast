import Cliente
import Administrador


class Usuario():
   
     Cargo:str
     Documento:int
     Edad:int
     Sexo:str
     Nombre:str


     def __init__(self, id:int,contrasena:str,cliente:Cliente,administrador:Administrador):
             self.Id=id
             self.Contraseña=contrasena
             self.Cliente=cliente
             self.Administrador=administrador

                
     def VerificarUsuario(self):
         print("el usuario es valido")

     def ActualizarDatos(self):
         print("datos actualizados")

     def Registrar(self):
         print("Usuario Creado")
        









    
