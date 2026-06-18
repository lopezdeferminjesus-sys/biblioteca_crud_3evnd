class Carrera:

    #Constructor
    def __init__(self, id, carrera):
        self.id = id
        self.carrera = carrera

    def mostrar_info(self):
        return f"{self.id} - {self.carrera}"