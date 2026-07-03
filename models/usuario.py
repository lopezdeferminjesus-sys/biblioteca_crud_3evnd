# Clase usuario

from models.libro import Libro

class Usuario:
    
    # Método constructor mejorado
    def __init__(self, id, matricula, nombre, carrera, correo, activo=True):
        self.id = id
        self.matricula = matricula
        self.nombre = nombre
        self.carrera = carrera  # Recuerda que este ahora es un ID entero
        self.correo = correo
        self.activo = activo

    # Mostrar en la pantalla la información de un usuario
    def mostrar_info(self):
        estado = "Activo" if self.activo else "Inactivo"
        return f"{self.nombre} - Carrera ID: {self.carrera} (Matrícula: {self.matricula}) - Correo: {self.correo} : {estado}"

    def activar(self):
        if not self.activo:
            self.activo = True
            print(f"El usuario {self.nombre} ha sido activado")
            return True
        else:
            print(f"El usuario {self.nombre} ya se encuentra activo")
            return False

    def desactivar(self):
        if self.activo:
            self.activo = False
            print(f"El usuario {self.nombre} ha sido desactivado")
            return True
        else:
            print(f"El usuario {self.nombre} ya se encuentra desactivado")
            return False