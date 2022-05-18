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
        
Id= str(input("Ingrese el ID de usuario: "))
Contraseña= str(input("Ingrese la contraseña de usuario: "))
Cargo= str(input("Ingrese el cargo del usuario: "))
Nombre= str(input("Ingrese el Nombre del usuario: "))
Documento= int(input("Ingrese el documento del usuario: "))
Edad= int(input("Ingrese la edad del usuario: "))
Sexo= str(input("Ingrese el sexo del usuario:"))

usuario1 = Usuario( Id,Cargo,Nombre,Documento,Edad,Sexo)
usuario1.Password









    
