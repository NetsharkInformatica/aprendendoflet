import flet as ft



def main(page: ft.Page):
    page.bgcolor=ft.colors.BLACK


    layout=ft.Container(
        width=900,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=300,color=ft.colors.CYAN),
        content=ft.ResponsiveRow(
            controls=[
                #parei em 1030
            ]
        )
    )


    page.update()

    page.add(layout)


if __name__=="__main__":
    ft.app(target=main)