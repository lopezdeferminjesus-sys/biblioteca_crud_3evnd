# Clase Libro
class Libro:

    # Método constructor
    def __init__(self, id, titulo, autor, isbn):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    # Mostrar en la pantalla la información de un libro
    def mostrar_info(self) :
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} - {self.autor} : {estado}"


    def prestar(self):
        if self.disponible :
            self.disponible = False
            print(f"El libro {self.titulo} está prestado")
            return True
        else:
            print(f"El libro {self.titulo} no está disponible")
            return False

    def devolver(self) :
        self.disponible = True
        print(f"El libro {self.titulo} ha sido devuelto")