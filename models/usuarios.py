# Clase usuario 

from models.libro import Libro

class Usuario:
    
    def __init__ (self, id, matricula, nombre, carrera):
        self.id = id
        self.matricula = matricula
        self.nombre = nombre
        self.carrera = carrera
        self.activo = True

    def activar(self):
        self.activo = True
        print(f"El usuario {self.nombre} ha sido activado")

    def desactivar(self):
        self.activo = False
        print(f"El usuario {self.nombre} ha sido desactivado")

    def mostrar_info(self):
        estado = "Activo" if self.activo else "Inactivo"
        return f"{self.nombre} - {self.carrera} : {estado}"