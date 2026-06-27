from dao.libro_dao import LibroDAO
from models.libro import Libro

def ver_todo(libro_dao):
    try:
        libros = libro_dao.obtener_libros()
        print("\n=== Libros en la biblioteca ===")
        if len(libros) == 0:
            print("No hay libros registrados")
        else :
            for libro in libros:
                print(f"ID: {libro.id} - {libro.titulo} - {libro.autor} - {libro.disponible}") 
        
        print("\n Conexión exitosa a la base de datos")
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")

def insertar_libro(libro_dao):
    try:
        print("---------------------------------------")
        print("Inserción de un nuevo libro")
        titulo = input("Escribe título del libro: ")
        autor = int(input("Escribe el id del autor: "))
        isbn = input("Escribe el ISBN del libro: ")
        disponible = True
        
        # Colocamos None en el ID ya que pgAdmin incrementa el id_libro automáticamente
        nuevoLibro = Libro(None, titulo, autor, isbn, disponible)
        libro_dao.insertar(nuevoLibro)
    except Exception as e:
        print(f"Error al insertar libro : {e}")

def actualizar_libro(libro_dao):
    try:
        ver_todo(libro_dao)
        id = int(input("Escribe el id del libro a editar: "))
        print("Actualiza los datos de este libro")
        titulo = input("Escribe el nuevo títuo del libro: ")
        autor = int(input("Escribe el nuevo id del autor: "))
        isbn = input("Escribe el nuevo isbn del libro: ")
        
        # Validación limpia de disponibilidad
        resp = input("¿Está disponible? (s/n): ").strip().lower()
        disponible = True if resp == 's' else False
        
        libro = Libro(id, titulo, autor, isbn, disponible)
        libro_dao.actualizar(libro)
    except Exception as e:
        print(f"Error al actualizar libro: {e}")

def eliminar_libro(libro_dao):
    try:
        ver_todo(libro_dao)
        id = int(input("Escribe el id del libro a eliminar: "))
        libro_dao.eliminar(id)
        print("Libros disponibles")
        ver_todo(libro_dao)
    except Exception as e:
        print(f"Error al eliminar libro: {e}")


def main():
    libro_dao = LibroDAO()
    
    # --- PRIMERA PARTE: Búsqueda inicial por ID del 1 al 4 ---
    print("=== Biblioteca universitaria === ")
    print("1. Ver todos los libros")
    print("2. Insertar nuevo libro")
    print("3. Actualizar un libro existente")
    print("4. Eliminar un libro exstente")

    try:
        # El número ingresado se usará directamente para buscar por ID en la BD
        id_buscado = int(input("Escribe una opcion (1-4): "))
        
        if 1 <= id_buscado <= 4:
            print(f"\nBuscando en pgAdmin el libro con ID: {id_buscado}...")
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
        else:
            print("El ID ingresado no está dentro del rango inicial (1-4).")
    except ValueError:
        print("Por favor, introduce un número válido.")

    # --- SEGUNDA PARTE: Menú de control interactivo continuo (1-5) ---
    while True:
        print("\n==================================")
        print("=== ¿Qué deseas hacer ahora? ===")
        print("==================================")
        print("1. Ver todos los libros")
        print("2. Insertar nuevo libro")
        print("3. Actualizar un libro existente")
        print("4. Eliminar un libro existente")
        print("5. Salir del programa")
        
        try:
            opcion = int(input("Escribe una opcion (1-5): "))
            
            match opcion:
                case 1: ver_todo(libro_dao)
                case 2: insertar_libro(libro_dao)
                case 3: actualizar_libro(libro_dao)
                case 4: eliminar_libro(libro_dao)
                case 5: 
                    print("Cerrando el sistema de biblioteca...")
                    break
                case _: 
                    print("Opción inválida. Elige un número del 1 al 5.")
        except ValueError:
            print("Entrada incorrecta. Por favor escribe un número entero.")

if __name__ == "__main__":
    main()