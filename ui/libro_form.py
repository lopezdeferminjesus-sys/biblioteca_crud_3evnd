import flet as ft

def libro_form():
    titulo_input = TextField(
        label="Titulo del Lbro: ",
        width = 400
    )

    autor_input = ft.TextFiel(
        label="Autor: ",
        width = 400
    )

    isbn_input = ft.TextFiel(
        label="ISBN: ",
        width = 400
    )
    
    mensaje = ft.Text(
        "",
        color = ft.Colors.GREEN
    )

    return ft.Container(
        padding = 30,
        content = ft.Column(
            controls = [
                ft.Text(
                    "Insertar nuevo libro",
                    size = 24,
                    weight = ft.FontWeight.BOLD
                ),
                ft.Text(
                    "Capture los datos básicos del libro",
                    size = 14,
                    weight = ft.Colors.BLUE_GREY_600
                ),
                titulo_input,
                autor_input,
                isbn_input,

                ft.ElevetedButton(
                    "Guardar",
                    icon = ft.Icon.SAVE,
                ),

                mensaje 
            ],
            spacing = 15
        )
    )