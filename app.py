import flet as ft

from ui.main_window import main_window
from dao.libro_dao import LibroDAO
from dao.usuario_dao import UsuarioDAO
from models.libro import Libro
from models.usuario import Usuario

# =====================================================================
#                          MÓDULO DE LIBROS
# =====================================================================

def ver_todo_libros(libro_dao):
    try:
        libros = libro_dao.obtener_libros()
        print("\n=== Libros en la biblioteca ===")
        if len(libros) == 0:
            print("No hay libros registrados")
        else:
            for libro in libros:
                print(f"ID: {libro.id} - {libro.titulo} - {libro.autor} - {libro.disponible}") 
        print("\n Conexión exitosa a la base de datos")
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")

def insertar_libro(libro_dao):
    try:
        print("\n---------------------------------------")
        print("Inserción de un nuevo libro")
        titulo = input("Escribe título del libro: ")
        autor = int(input("Escribe el id del autor: "))
        isbn = input("Escribe el ISBN del libro: ")
        disponible = True
        
        nuevoLibro = Libro(None, titulo, autor, isbn, disponible)
        libro_dao.insertar(nuevoLibro)
        print("¡Libro insertado con éxito!")
    except Exception as e:
        print(f"Error al insertar libro : {e}")

def actualizar_libro(libro_dao):
    try:
        ver_todo_libros(libro_dao)
        id = int(input("\nEscribe el id del libro a editar: "))
        print("Actualiza los datos de este libro")
        titulo = input("Escribe el nuevo título del libro: ")
        autor = int(input("Escribe el nuevo id del autor: "))
        isbn = input("Escribe el nuevo isbn del libro: ")
        
        resp = input("¿Está disponible? (s/n): ").strip().lower()
        disponible = True if resp == 's' else False
        
        libro = Libro(id, titulo, autor, isbn, disponible)
        libro_dao.actualizar(libro)
        print("¡Libro updated con éxito!")
    except Exception as e:
        print(f"Error al actualizar libro: {e}")

def eliminar_libro(libro_dao):
    try:
        ver_todo_libros(libro_dao)
        id = int(input("\nEscribe el id del libro a eliminar: "))
        libro_dao.eliminar(id)
        print("\nLibros disponibles actualizados:")
        ver_todo_libros(libro_dao)
    except Exception as e:
        print(f"Error al eliminar libro: {e}")

def menu_libros():
    libro_dao = LibroDAO()
    while True:
        print("\n==================================")
        print("=== Administración de Libros ===")
        print("==================================")
        print("1. Ver todos los libros")
        print("2. Insertar nuevo libro")
        print("3. Actualizar un libro existente")
        print("4. Eliminar un libro existente")
        print("5. Volver al menú principal")
        
        try:
            opcion = int(input("Escribe una opcion (1-5): "))
            match opcion:
                case 1: ver_todo_libros(libro_dao)
                case 2: insertar_libro(libro_dao)
                case 3: actualizar_libro(libro_dao)
                case 4: eliminar_libro(libro_dao)
                case 5: break
                case _: print("Opción inválida.")
        except ValueError:
            print("Por favor escribe un número entero.")


# =====================================================================
#                          MÓDULO DE USUARIOS
# =====================================================================

def ver_todo_usuarios(usuario_dao):
    try:
        usuarios = usuario_dao.unlock_usuarios() if hasattr(usuario_dao, 'unlock_usuarios') else usuario_dao.obtener_usuarios()
        print("\n=== Usuarios en la biblioteca ===")
        if len(usuarios) == 0:
            print("No hay usuarios registrados")
        else:
            for u in usuarios:
                estado = "Activo" if u.activo else "Inactivo"
                print(f"ID: {u.id} | Nombre: {u.nombre} | Matrícula: {u.matricula} | ID Carrera: {u.carrera} | Correo: {u.correo} | Estado: {estado}")
    except Exception as e:
        print(f"Error al conectar con usuarios: {e}")

def insertar_usuario(usuario_dao):
    try:
        print("\n---------------------------------------")
        print("Inserción de un nuevo usuario")
        
        nombre = input("Escribe el nombre del usuario: ")
        matricula = input("Escribe la matrícula del usuario: ")
        carrera = int(input("Escribe el ID numérico de la carrera: "))
        correo = input("Escribe el correo del usuario: ")
        activo = True  
        
        nuevo_usuario = Usuario(None, nombre, matricula, carrera, correo, activo)
        usuario_dao.insertar(nuevo_usuario)
        print("¡Usuario registrado con éxito!")
    except Exception as e:
        print(f"Error al insertar usuario: {e}")

def actualizar_usuario(usuario_dao):
    try:
        ver_todo_usuarios(usuario_dao)
        id = int(input("\nEscribe el ID del usuario a editar: "))
        nombre = input("Escribe el nuevo nombre: ")
        matricula = input("Escribe la nueva matrícula: ")
        carrera = int(input("Escribe el nuevo ID numérico de la carrera: "))
        correo = input("Escribe el nuevo correo: ")
        
        resp = input("¿Está activo? (s/n): ").strip().lower()
        activo = True if resp == 's' else False
        
        usuario = Usuario(id, nombre, matricula, carrera, correo, activo)
        usuario_dao.actualizar(usuario)
        print("¡Usuario actualizado con éxito!")
    except Exception as e:
        print(f"Error al actualizar usuario: {e}")

def eliminar_usuario(usuario_dao):
    try:
        ver_todo_usuarios(usuario_dao)
        id = int(input("\nEscribe el ID del usuario a eliminar: "))
        usuario_dao.eliminar(id)
        print("\nUsuarios actualizados:")
        ver_todo_usuarios(usuario_dao)
    except Exception as e:
        print(f"Error al eliminar usuario: {e}")

def menu_usuarios():
    usuario_dao = UsuarioDAO()
    while True:
        print("\n==================================")
        print("=== Administración de Usuarios ===")
        print("==================================")
        print("1. Ver todos los usuarios")
        print("2. Insertar nuevo usuario")
        print("3. Actualizar un usuario existente")
        print("4. Eliminar un usuario existente")
        print("5. Volver al menú principal")
        
        try:
            opcion = int(input("Escribe una opcion (1-5): "))
            match opcion:
                case 1: ver_todo_usuarios(usuario_dao)
                case 2: insertar_usuario(usuario_dao)
                case 3: actualizar_usuario(usuario_dao)
                case 4: eliminar_usuario(usuario_dao)
                case 5: break
                case _: print("Opción inválida.")
        except ValueError:
            print("Por favor escribe un número entero.")


# =====================================================================
#                          FLUJO PRINCIPAL
# =====================================================================

if __name__ == "__main__":
    ft.run(main_window)