import flet as ft

def main_window(page: ft.page):
    #ferinir configureacion de la pagina principal
    page.title = "Sistema de Gestión de Biblioteca"
    page.window_width = 1100
    page.window_height = 700
    page.padding = 0
    page.bgcolor = ft.Colors.BLUE_GREY_50
    
    #Widget etiqueta o Text
    titulo = ft.Text(
        "Sistema de Gestión de Biblioteca",
        size = 24,
        weight = ft.Weight.BOLD
    )

    subtitulo = ft.Text(
        "Seleccione una opción del menú",
        size =16,
        color = ft.Color.BLUE_GREY_600
    )

    #CONTENEDOR CENTRAL
    contenido = ft.Container(
        content = ft.Column(
            controls = [
                titulo,
                subtitulo
            ],
            spacing = 10
        ),
        padding = 30,
        expand = True
    )

    #menu lateral
    menu_lateral = ft.Container(
        width = 220,
        bgcolor = ft.Color.BLUE_GREY_900,
        padding = 20
        content = ft.Column(
            control = [
                ft.text(
                    "Biblioteca",
                    size = 20,
                    weight = ft.FontWeigh.BOLD,
                    color = ft.Colors.WITHE
                ),
                ft.Text(
                    "Sistema de Gestión",
                    size = 12,
                    color = ft.Colors.BLUE_GREY_100
                ),
                ft.Divider(color = ft.Colors.BLUE_GLEY_700)
                #BOTON
                ft.ElevatedButton(
                    text = "Libros",
                    icon = ft.Icons.BOOK,
                    width = 180
                ),
                ft.ElevatedButton(
                    text = "Usuarios",
                    icon = ft.Icons.PERSON,
                    width = 180
                ),
                ft.ElevatedButton(
                    text = "Préstamos",
                    icon = ft.Icons.SWAP_HORIZ,
                    width = 180
                ),
                ft.ElevatedButton(
                    text = "Devoluciones",
                    icon = ft.Icons.KEYBOARD_RETURN,
                    width = 180
                ),
            ],
            spacing = 15
        )
    )

    #Definición del layout de la pagina
    layout = ft.Row(
        controls = [
            manu_lateral,
            contenido
        ],
        expand = True
    )

    # Agegar el layout a la pagina
    page.add(layout)