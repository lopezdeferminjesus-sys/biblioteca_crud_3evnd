# DAO: Data Access Object
from database.conexion import Conexion
from models.libro import Libro

class LibroDAO:

    # Obtener todos los libros ordenados por ID
    def obtener_libros(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT id_libro, titulo, autor, isbn, disponible FROM libro ORDER BY id_libro")
        registros = cursor.fetchall()

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
            
        cursor.close()
        conexion.close()
        return libros
    
    # Insertar un nuevo libro
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

    # Actualizar un libro existente
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

    # Eliminar un libro por ID
    def eliminar(self, id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

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