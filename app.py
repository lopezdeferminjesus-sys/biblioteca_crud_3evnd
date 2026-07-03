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
                print(f"ID: {libro.id} - {libro.titulo} - Autor ID: {libro.autor} - Disponible: {'Sí' if libro.disponible else 'No'}") 
        print("\nConexión exitosa a la base de datos")
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")

def insertar_libro(libro_dao):
    try:
        print("\n---------------------------------------")
        print("Inserción de un nuevo libro")
        titulo = input("Escribe título del libro: ").strip()
        autor = int(input("Escribe el id del autor: "))
        isbn = input("Escribe el ISBN del libro: ").strip()
        disponible = True
        
        nuevoLibro = Libro(None, titulo, autor, isbn, disponible)
        libro_dao.insertar(nuevoLibro)
        print("¡Libro insertado con éxito!")
    except ValueError:
        print("Error: El ID del autor debe ser un número entero.")
    except Exception as e:
        print(f"Error al insertar libro : {e}")

def actualizar_libro(libro_dao):
    try:
        ver_todo_libros(libro_dao)
        id = int(input("\nEscribe el id del libro a editar: "))
        print("Actualiza los datos de este libro")
        titulo = input("Escribe el nuevo título del libro: ").strip()
        autor = int(input("Escribe el nuevo id del autor: "))
        isbn = input("Escribe el nuevo isbn del libro: ").strip()
        
        resp = input("¿Está disponible? (s/n): ").strip().lower()
        disponible = True if resp == 's' else False
        
        libro = Libro(id, titulo, autor, isbn, disponible)
        libro_dao.actualizar(libro)
        print("¡Libro actualizado con éxito!")
    except ValueError:
        print("Error: Los identificadores de ID y Autor deben ser números enteros.")
    except Exception as e:
        print(f"Error al actualizar libro: {e}")

def eliminar_libro(libro_dao):
    try:
        ver_todo_libros(libro_dao)
        id = int(input("\nEscribe el id del libro a eliminar: "))
        libro_dao.eliminar(id)
        print("\nLibros disponibles actualizados:")
        ver_todo_libros(libro_dao)
    except ValueError:
        print("Error: El ID debe ser un número entero.")
    except Exception as e:
        print(f"Error al eliminar libro: {e}")

def menu_libros():
    libro_dao = LibroDAO()
    print("\n=== Menú de Libros (Búsqueda inicial) ===")
    
    try:
        id_buscado = int(input("Escribe un ID para buscar un libro de forma rápida (o cualquier otro número para omitir): "))
        print(f"\nBuscando en la base de datos el libro con ID: {id_buscado}...")
        libros_bd = libro_dao.obtener_libros()
        libro_encontrado = next((l for l in libros_bd if l.id == id_buscado), None)
        
        if libro_encontrado:
            print("\n[Libro Encontrado]:")
            print(f"ID Libro: {libro_encontrado.id}")
            print(f"Título:   {libro_encontrado.titulo}")
            print(f"Autor ID: {libro_encontrado.autor}")
            print(f"ISBN:     {libro_encontrado.isbn}")
            print(f"Estado:   {'Disponible' if libro_encontrado.disponible else 'No disponible'}")
        else:
            print(f"No existe ningún libro con el ID {id_buscado} en las tablas.")
    except ValueError:
        print("Búsqueda inicial omitida o entrada no válida.")

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
                case 5:
                    print("Volviendo al menú anterior...")
                    break
                case _:
                    print("Opción inválida. Elige un número del 1 al 5.")
        except ValueError:
            print("Entrada incorrecta. Por favor escribe un número entero.")


# =====================================================================
#                          MÓDULO DE USUARIOS
# =====================================================================

def ver_todo_usuarios(usuario_dao):
    try:
        usuarios = usuario_dao.obtener_usuarios() 
        print("\n=== Usuarios en la biblioteca ===")
        if len(usuarios) == 0:
            print("No hay usuarios registrados")
        else:
            for usuario in usuarios:
                print(f"ID: {usuario.id} - Matrícula: {usuario.matricula} - Nombre: {usuario.nombre} - Carrera: {usuario.carrera} - Activo: {'Sí' if usuario.activo else 'No'}")
    except Exception as e:
        print(f"Error al conectar con usuarios: {e}")

def insertar_usuario(usuario_dao):
    try:
        print("\n---------------------------------------")
        print("Inserción de un nuevo usuario")
        matricula = input("Escribe la matrícula del usuario: ").strip()
        nombre = input("Escribe nombre del usuario: ").strip()
        carrera = input("Escribe la carrera del usuario: ").strip()
        
        nuevo_usuario = Usuario(None, matricula, nombre, carrera)
        usuario_dao.insertar(nuevo_usuario)
        print("¡Usuario registrado con éxito!")
    except Exception as e:
        print(f"Error al insertar usuario: {e}")

def actualizar_usuario(usuario_dao):
    try:
        ver_todo_usuarios(usuario_dao)
        id = int(input("\nEscribe el id del usuario a editar: "))
        matricula = input("Escribe la nueva matrícula: ").strip()
        nombre = input("Escribe el nuevo nombre: ")
        carrera = input("Escribe la nueva carrera: ").strip()
        
        resp = input("¿El usuario está activo? (s/n): ").strip().lower()
        activo = True if resp == 's' else False
        
        usuario = Usuario(id, matricula, nombre, carrera, activo)
        usuario_dao.actualizar(usuario)
        print("¡Usuario actualizado con éxito!")
    except ValueError:
        print("Error: El ID del usuario debe ser un número entero.")
    except Exception as e:
        print(f"Error al actualizar usuario: {e}")

def eliminar_usuario(usuario_dao):
    try:
        ver_todo_usuarios(usuario_dao)
        id = int(input("\nEscribe el id del usuario a eliminar: "))
        usuario_dao.eliminar(id)
        print("\nUsuarios actualizados:")
        ver_todo_usuarios(usuario_dao)
    except ValueError:
        print("Error: El ID debe ser un número entero.")
    except Exception as e:
        print(f"Error al eliminar usuario: {e}")

def menu_usuarios():
    usuario_dao = UsuarioDAO()
    print("\n=== Menú de Usuarios (Búsqueda inicial) ===")
    
    try:
        id_buscado = int(input("Escribe un ID para buscar un usuario de forma rápida (o cualquier otro número para omitir): "))
        print(f"\nBuscando en la base de datos el usuario con ID: {id_buscado}...")
        usuarios_bd = usuario_dao.obtener_usuarios()
        usuario_encontrado = next((u for u in usuarios_bd if u.id == id_buscado), None)
        
        if usuario_encontrado:
            print("\n[Usuario Encontrado]:")
            print(f"ID Usuario: {usuario_encontrado.id}")
            print(f"Matrícula:  {usuario_encontrado.matricula}")
            print(f"Nombre:     {usuario_encontrado.nombre}")
            print(f"Carrera:    {usuario_encontrado.carrera}")
            print(f"Estado:     {'Activo' if usuario_encontrado.activo else 'Inactivo'}")
        else:
            print(f"No existe ningún usuario con el ID {id_buscado} en las tablas.")
    except ValueError:
        print("Búsqueda inicial omitida o entrada no válida.")

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
                case 5:
                    print("Volviendo al menú anterior...")
                    break
                case _:
                    print("Opción inválida. Elige un número del 1 al 5.")
        except ValueError:
            print("Entrada incorrecta. Por favor escribe un número entero.")


# =====================================================================
#                          FLUJO PRINCIPAL
# =====================================================================

def main():
    while True:
        print("\n======================================")
        print("=== SISTEMA DE GESTIÓN UNIVERSITARIA ===")
        print("======================================")
        print("1. Administrar Módulo de Libros")
        print("2. Administrar Módulo de Usuarios")
        print("3. Salir completamente del sistema")
        
        try:
            opcion_principal = int(input("Selecciona un módulo (1-3): "))
            match opcion_principal:
                case 1:
                    menu_libros()
                case 2:
                    menu_usuarios()
                case 3:
                    print("\nCerrando el sistema general de biblioteca. ¡Hasta luego!")
                    break
                case _:
                    print("Opción inválida. Elige entre 1, 2 o 3.")
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

if __name__ == "__main__":
    main()