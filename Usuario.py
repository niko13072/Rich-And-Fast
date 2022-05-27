class Usuario():
   
     Cargo:str
     Documento:int
     Edad:int
     Sexo:str


     def __init__(self, id:int,contrasena:str):
             self.Id=id
             self.Contraseña=contrasena

                
     def VerificarUsuario(self):
         print("el usuario es valido")

     def ActualizarDatos(self):
         print("datos actualizados")

     def Registrar(self):
         print("Usuario Creado")
        









    
