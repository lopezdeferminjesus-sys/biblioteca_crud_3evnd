import flet as ft
from dao.libro_dao import LibroDAO
from models.libro import Libro

def libro_form(regresar):
    libro_dao = LibroDAO()
    
    # Variable de control: guarda el ID del libro que se está editando.
    # Si es None, significa que estamos creando un libro nuevo.
    libro_en_edicion_id = None

    # Campos de entrada
    titulo_input = ft.TextField(
        label="Título del Libro",
        width=350,
        hint_text="Ej. Cien años de soledad"
    )

    autor_input = ft.TextField(
        label="ID del Autor (Numérico)",
        width=350,
        hint_text="Ej. 1"
    )

    isbn_input = ft.TextField(
        label="ISBN",
        width=350,
        hint_text="Ej. 978-3-16-148410-0"
    )
    
    mensaje = ft.Text(
        "",
        weight=ft.FontWeight.BOLD
    )

    # Botón principal (cambiará de texto y color dinámicamente)
    boton_guardar = ft.ElevatedButton(
        "Guardar",
        icon=ft.Icons.SAVE,
        bgcolor=ft.Colors.BLUE_900,
        color=ft.Colors.WHITE,
        on_click=lambda e: procesar_formulario(e)
    )

    # Botón de cancelar (oculto por defecto, solo se muestra al editar)
    boton_cancelar_edicion = ft.OutlinedButton(
        "Cancelar Edición",
        icon=ft.Icons.CANCEL,
        visible=False,
        on_click=lambda e: salir_modo_edicion(e.page)
    )

    # Contenedor para listar los libros dinámicamente
    lista_libros_column = ft.Column(spacing=10, scroll=ft.ScrollMode.AUTO, height=300)

    # Carga y pinta la lista de libros con botones de editar y eliminar
    def actualizar_lista_visual():
        lista_libros_column.controls.clear()
        try:
            libros = libro_dao.obtener_libros()
            if not libros:
                lista_libros_column.controls.append(
                    ft.Text("No hay libros registrados.", color=ft.Colors.BLUE_GREY_400, italic=True)
                )
            else:
                for lib in libros:
                    fila_libro = ft.Container(
                        padding=10,
                        border_radius=8,
                        bgcolor=ft.Colors.WHITE,
                        border=ft.Border.all(1, ft.Colors.BLUE_GREY_100),
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Column(
                                    controls=[
                                        ft.Text(f"{lib.titulo}", size=14, weight=ft.FontWeight.BOLD),
                                        ft.Text(f"Autor ID: {lib.autor} | ISBN: {lib.isbn}", size=12, color=ft.Colors.BLUE_GREY_500),
                                    ],
                                    spacing=2
                                ),
                                # Fila de botones de acción
                                ft.Row(
                                    controls=[
                                        # Corregido: Se utiliza ft.Icons.EDIT que es compatible en cualquier versión
                                        ft.IconButton(
                                            icon=ft.Icons.EDIT,
                                            icon_color=ft.Colors.BLUE_700,
                                            tooltip="Editar Libro",
                                            on_click=lambda e, lib_editar=lib: entrar_modo_edicion(lib_editar, e.page)
                                        ),
                                        ft.IconButton(
                                            icon=ft.Icons.DELETE_OUTLINE,
                                            icon_color=ft.Colors.RED_ACCENT,
                                            tooltip="Eliminar Libro",
                                            on_click=lambda e, id_eliminar=lib.id, titulo_eliminar=lib.titulo: eliminar_libro_click(id_eliminar, titulo_eliminar)
                                        )
                                    ],
                                    spacing=5
                                )
                            ]
                        )
                    )
                    lista_libros_column.controls.append(fila_libro)
        except Exception as ex:
            lista_libros_column.controls.append(
                ft.Text(f"Error al cargar libros: {ex}", color=ft.Colors.RED)
            )
        
        try:
            lista_libros_column.page.update()
        except Exception:
            pass

    # Activa el modo edición cargando los datos en los inputs
    def entrar_modo_edicion(libro, page):
        nonlocal libro_en_edicion_id
        libro_en_edicion_id = libro.id
        
        # Llenar inputs con los datos actuales
        titulo_input.value = libro.titulo
        autor_input.value = str(libro.autor)
        isbn_input.value = libro.isbn
        
        # Modificar botones
        boton_guardar.text = "Actualizar"
        boton_guardar.icon = ft.Icons.EDIT
        boton_guardar.bgcolor = ft.Colors.ORANGE_800
        boton_cancelar_edicion.visible = True
        
        mensaje.value = f"Editando: '{libro.titulo}'"
        mensaje.color = ft.Colors.ORANGE_800
        page.update()

    # Sale del modo edición limpiando los campos
    def salir_modo_edicion(page):
        nonlocal libro_en_edicion_id
        libro_en_edicion_id = None
        
        titulo_input.value = ""
        autor_input.value = ""
        isbn_input.value = ""
        
        boton_guardar.text = "Guardar"
        boton_guardar.icon = ft.Icons.SAVE
        boton_guardar.bgcolor = ft.Colors.BLUE_900
        boton_cancelar_edicion.visible = False
        
        mensaje.value = ""
        page.update()

    # Ejecuta el guardado (Inserta si es nuevo, Actualiza si está en modo edición)
    def procesar_formulario(e):
        nonlocal libro_en_edicion_id
        
        titulo = titulo_input.value.strip()
        autor_raw = autor_input.value.strip()
        isbn = isbn_input.value.strip()

        if titulo == "" or autor_raw == "" or isbn == "":
            mensaje.value = "Todos los campos son obligatorios."
            mensaje.color = ft.Colors.RED
            e.page.update()
            return

        try:
            autor_id = int(autor_raw)
        except ValueError:
            mensaje.value = "El ID del Autor debe ser un número entero."
            mensaje.color = ft.Colors.RED
            e.page.update()
            return

        try:
            if libro_en_edicion_id is None:
                # MODO INSERTAR
                nuevo_libro = Libro(id=None, titulo=titulo, autor=autor_id, isbn=isbn, disponible=True)
                libro_dao.insertar(nuevo_libro)
                mensaje.value = f"¡Libro '{titulo}' guardado con éxito!"
                mensaje.color = ft.Colors.GREEN
            else:
                # MODO EDITAR
                libro_editado = Libro(id=libro_en_edicion_id, titulo=titulo, autor=autor_id, isbn=isbn, disponible=True)
                libro_dao.actualizar(libro_editado)
                mensaje.value = f"¡Libro '{titulo}' actualizado con éxito!"
                mensaje.color = ft.Colors.GREEN
            
            # Limpiar campos y reestablecer estado
            salir_modo_edicion(e.page)
            actualizar_lista_visual()
            
        except Exception as ex:
            mensaje.value = f"Error en la operación: {ex}"
            mensaje.color = ft.Colors.RED
            
        e.page.update()

    # Eliminar libro de la base de datos
    def eliminar_libro_click(id_libro, titulo_libro):
        try:
            # Si estamos editando el mismo libro que se va a eliminar, cancelamos la edición primero
            if libro_en_edicion_id == id_libro:
                salir_modo_edicion(lista_libros_column.page)
                
            libro_dao.eliminar(id_libro)
            mensaje.value = f"¡Libro '{titulo_libro}' eliminado!"
            mensaje.color = ft.Colors.ORANGE_800
            actualizar_lista_visual()
        except Exception as ex:
            mensaje.value = f"Error al eliminar: {ex}"
            mensaje.color = ft.Colors.RED
            lista_libros_column.page.update()

    # Cargar la lista al inicializar la interfaz
    actualizar_lista_visual()

    return ft.Container(
        padding=20,
        expand=True,
        content=ft.Row(
            spacing=30,
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.START,
            controls=[
                # COLUMNA IZQUIERDA: FORMULARIO (Inserción y Edición)
                ft.Column(
                    width=400,
                    spacing=15,
                    controls=[
                        ft.Text("Formulario de Libros", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_GREY_800),
                        ft.Text("Edite o registre libros asociados a un Autor ID existente.", size=13, color=ft.Colors.BLUE_GREY_600),
                        titulo_input,
                        autor_input,
                        isbn_input,
                        ft.Row(
                            controls=[
                                boton_guardar,
                                boton_cancelar_edicion,
                                ft.OutlinedButton(
                                    "Regresar",
                                    icon=ft.Icons.ARROW_BACK,
                                    on_click=lambda e: regresar()
                                ),
                            ],
                            spacing=10
                        ),
                        mensaje
                    ]
                ),
                
                ft.VerticalDivider(width=1, color=ft.Colors.BLUE_GREY_100),
                
                # COLUMNA DERECHA: MONITOREO, EDICIÓN Y ELIMINACIÓN
                ft.Column(
                    expand=True,
                    spacing=15,
                    controls=[
                        ft.Text("Inventario de Libros ", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_GREY_800),
                        ft.Container(
                            content=lista_libros_column,
                            expand=True
                        )
                    ]
                )
            ]
        )
    )