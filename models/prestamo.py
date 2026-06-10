class Prestamo:

    #onstructor
    def __init__(self, id, id_usuario, id_libro ,fecha_prestamo ,fecha_devolucion,):
        self.id = id
        self.id_usuario = id_usuario
        self.id_libro = id_libro
        self.feche_prestamo = fecha_prestamo
        self.fecha_devolucion = id_devolucion
        self.devuelto = False

    def registrar_devolucion(self):
        self.devuelto = True
        print(f"El pretamo con ID {self.id} ha sido marcado como devuelto")