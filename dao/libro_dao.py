# DAD: Data access objet 
# Es una clase que se encarga de acceder 
# a la base de datos y realizar las operaciones 

from database.conexion import Conexion
from models.libro import Libro

class libroDAD:

    # Select * from libros
    def obtener_libros(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM libros")
        # Obtiene los rresultados 
        registros = cursor.fetchall()


        # Crear una lista de clase Libro
        libros = []
        for registro in registros:
            libro = Libros(
                id=registro[0],
                titulo=registro[1],
                autor=registro[2],
                isbn=registro[3],
                disponible=registro[4] 
            )
            libros.append(libro)
        # Cerrar la conexion
        cursor.close()
        conexion.close()
        return  libros