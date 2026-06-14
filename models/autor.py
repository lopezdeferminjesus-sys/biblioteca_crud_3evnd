class Autor:

    #Constructor
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def mostrar_info(self):
        return f"{self.id} - {self.nombre}"