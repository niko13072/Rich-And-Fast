class Usuario():
   
        Password:str

        def __init__(self, Id:int, Cargo:str, Nombre:str, Documento:int, Edad:int, Sexo:str):
                self.Id= Id
                self.Cargo = Cargo
                self.Nombre = Nombre
                self.Documento = Documento
                self.Edad = Edad
                self.Sexo = Sexo
                self.permisos = ['ver','ordenar','pagar']
    
                def VerificarUsuario(self):
                 print("el usuario es valido")

                def ActualizarDatos(self):
                 print("datos actualizados")

                def Registrar(self):
                 print("Usuario Creado")
        









    
