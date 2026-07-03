# DAO: Data Access Object
# Es una clase que se encarga de acceder
# a la base de datos y realizar las operaciones

from database.conexion import Conexion
from models.libro import Libro

class LibroDAO:

    # Select * from libro ordenado por id_libro
    def obtener_libros(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        # Ejecuta la consulta seleccionando explícitamente id_libro
        cursor.execute("SELECT id_libro, titulo, autor, isbn, disponible FROM libro ORDER BY id_libro")
        registros = cursor.fetchall()

        # Crear una lista de clase Libro
        libros = []
        for registro in registros:
            libro = Libro(
                id=registro[0],  # El id_libro de la BD se guarda en el atributo id del objeto
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
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO libro(titulo, autor, isbn, disponible)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(sql, (
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

        sql = """
                UPDATE libro
                SET titulo = %s, autor = %s,
                isbn = %s, disponible = %s
                WHERE id_libro = %s
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

    # Delete
    def eliminar(self, id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        # Se incluye la coma (id,) para pasarlo correctamente como una tupla válida a execute
        cursor.execute("DELETE FROM libro WHERE id_libro = %s", (id,))
        
        conexion.commit()
        cursor.close()
        conexion.close()

    # Obtener último ID
    def obtener_ultimo_id(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT id_libro FROM libro ORDER BY id_libro DESC")
        resultado = cursor.fetchone()
        
        cursor.close()
        conexion.close()
        return resultado[0] if resultado else None