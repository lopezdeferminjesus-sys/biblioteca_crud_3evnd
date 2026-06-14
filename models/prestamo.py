class Prestamo:

    #Constructor
    def __init__(
            self, 
            id,
            id_usuario,
            id_libro,
            fecha_prestamo,
            fecha_devolucion
        ):
        self.id = id
        self.id_usuario = id_usuario
        self.id_libro = id_libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.devuelto = False

    def registrar_devolucion(self):
        self.devuelto = True
        print(f"El préstamo con ID {self.id} ha sido marcado como devuelto")