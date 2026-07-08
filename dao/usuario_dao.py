from database.conexion import Conexion
from models.usuario import Usuario

class UsuarioDAO:

    # Obtener todos los usuarios de la tabla
    def obtener_usuarios(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        # Usamos los nombres exactos de tus columnas según la imagen f9b886.png
        cursor.execute("SELECT id, nombre, matricula, carrera, correo, activo FROM usuario ORDER BY id")
        registros = cursor.fetchall()

        usuarios = []
        for reg in registros:
            usuario = Usuario(
                id=reg[0],
                nombre=reg[1],
                matricula=reg[2],
                carrera=reg[3],  # Es un número entero (ID de la carrera)
                correo=reg[4],
                activo=reg[5]
            )
            usuarios.append(usuario)
            
        cursor.close()
        conexion.close()
        return usuarios
    
    # Insertar un nuevo usuario
    def insertar(self, usuario):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        # El campo 'id' es autoincremental y 'activo' se pone en true automáticamente si no se manda
        sql = """
        INSERT INTO usuario(nombre, matricula, carrera, correo, activo)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (
            usuario.nombre, 
            usuario.matricula,
            usuario.carrera,  # Mandamos el entero
            usuario.correo,
            usuario.activo
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    # Actualizar un usuario existente por su columna 'id'
    def actualizar(self, usuario):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        UPDATE usuario
        SET nombre = %s, matricula = %s, carrera = %s, correo = %s, activo = %s
        WHERE id = %s
        """

        cursor.execute(sql, (
            usuario.nombre, 
            usuario.matricula,
            usuario.carrera,
            usuario.correo,
            usuario.activo,
            usuario.id
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    # Eliminar un usuario por su columna 'id'
    def eliminar(self, id):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("DELETE FROM usuario WHERE id = %s", (id,))
        
        conexion.commit()
        cursor.close()
        conexion.close()