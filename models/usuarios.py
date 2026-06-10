# Clase usuario

from libro import Libro

class Usuario:
    
    def __init__ (self, matricula, nombre, carrera):
        self,id = id
        self.matricula = matricula
        self.nombre = nombre
        self.carrera = carrera
        self.activo = True

    def actividad(self):
        self.activo = True
        print(f"El usuario {self.nombre} ha sido activado")

    def desactivar(self):
        self.activo = True
        print(f"El usuario {self.nombre} ha sido desactivado")


        