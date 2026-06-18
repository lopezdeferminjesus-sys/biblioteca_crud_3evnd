# DAO: Data Access Object
# Es una clase que se encarga de acceder 
# a la base de datos y realizar las operaciones

from database.conexion import Conexion
from models.libro import Libro

class LibroDAO:

    # Select * from libros
    def obtener_libros(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        # Ejecuta la consulta
        cursor.execute("SELECT * FROM libro")
        # Obtiene los resultados
        registros = cursor.fetchall()

        # Crear una lista de clase Libro
        libros = []
        for registro in registros:
            libro = Libro(
                id=registro[0],
                titulo=registro[1],
                autor=registro[2],
                isbn=registro[3],
                disponible=registro[4]
            )
            libros.append(libro)
        # Cerrar la conexión   
        cursor.close()
        conexion.close()
        return libros
    
    # Insert
    def insertar(self, libro):
        conexion= Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO libro(titulo, autor, isbn, disponible)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(sql,(
            libro.titulo, 
            libro.autor,
            libro.isbn,
            libro.disponible
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    # Update
    def actualizar(self, libro):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql= """
                UPDATE libro
                SET titulo = %s, autor=%x,
                isbn=%s, disponible=%s
                WHERE id = %s
        """

        cursor.execute(sql, (
            libro.titulo, 
            libro.autor, 
            libro.isbn,
            libro.disponible,
            libro.id
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar(self, id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("DELETE FROM libro WHERE id = %s",
            (id))
        conexion.commit()
        cursor.close()
        conexion.close()