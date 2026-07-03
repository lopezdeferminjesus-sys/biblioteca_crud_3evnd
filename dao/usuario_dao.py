from database.conexion import Conexion
from models.usuario import Usuario

class UsuarioDAO:

    def obtener_usuarios(self):
        conexion = Conexion.obtain_conexion() if hasattr(Conexion, 'obtain_conexion') else Conexion.obtener_conexion()
        cursor = conexion.cursor()
        try:
            # Aquí ya usamos "id" y añadimos "correo" tal como está en tu pgAdmin
            cursor.execute("SELECT id, matricula, nombre, carrera, correo, activo FROM usuario ORDER BY id")
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(
                    id=registro[0],
                    matricula=registro[1],
                    nombre=registro[2],
                    carrera=registro[3],
                    correo=registro[4],
                    activo=registro[5]
                )
                usuarios.append(usuario)
            return usuarios
        finally:
            cursor.close()
            conexion.close()
    
    def insertar(self, usuario):
        conexion = Conexion.obtain_conexion() if hasattr(Conexion, 'obtain_conexion') else Conexion.obtener_conexion()
        cursor = conexion.cursor()
        try:
            sql = "INSERT INTO usuario(matricula, nombre, carrera, correo, activo) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (usuario.matricula, usuario.nombre, usuario.carrera, usuario.correo, usuario.activo))
            conexion.commit()
        finally:
            cursor.close()
            conexion.close()

    def actualizar(self, usuario):
        conexion = Conexion.obtain_conexion() if hasattr(Conexion, 'obtain_conexion') else Conexion.obtener_conexion()
        cursor = conexion.cursor()
        try:
            sql = "UPDATE usuario SET matricula = %s, nombre = %s, carrera = %s, correo = %s, activo = %s WHERE id = %s"
            cursor.execute(sql, (usuario.matricula, usuario.nombre, usuario.carrera, usuario.correo, usuario.activo, usuario.id))
            conexion.commit()
        finally:
            cursor.close()
            conexion.close()

    def eliminar(self, id_usuario):
        conexion = Conexion.obtain_conexion() if hasattr(Conexion, 'obtain_conexion') else Conexion.obtener_conexion()
        cursor = conexion.cursor()
        try:
            cursor.execute("DELETE FROM usuario WHERE id = %s", (id_usuario,))
            conexion.commit()
        finally:
            cursor.close()
            conexion.close()