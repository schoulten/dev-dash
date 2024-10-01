# Bibliotecas
from shiny import App, ui


# Interface do Usuário
app_ui = ui.page_navbar(
    ui.nav_panel(
        "Página 1",
        ui.layout_sidebar(
            ui.sidebar(
                ui.markdown(
                    """
                    Uma frase com **negrito** e *itálico*, além de um [link](https://analisemacro.com.br/).
                    - Item 1
                    - Item 2
                    - Item 3

                    ![](https://aluno.analisemacro.com.br/wp-content/uploads/dlm_uploads/2023/05/logo_am_45.png)
                    """
                ),
                bg = "#d3d3d3"
            ),
            "Painel principal"
        )
        ),
    ui.nav_panel("Página 2", "Conteúdo da Página 2"),
    ui.nav_control(ui.a("Análise Macro", href = "https://analisemacro.com.br/")),
    ui.nav_menu(
        "Saiba mais",
        ui.nav_control(ui.a("Site", href = "https://analisemacro.com.br/")),
        ui.nav_control(ui.a("Blog", href = "https://analisemacro.com.br/blog/"))
    ),
    title = ui.row(
        ui.column(4, ui.img(src = "https://aluno.analisemacro.com.br/wp-content/uploads/dlm_uploads/2023/05/logo_am_45.png")),
        ui.column(8, "Análise Macro")
    ),
    bg = "gray",
    inverse = True,
    window_title = "Análise Macro"
)


# Servidor
def server(input, output, session):
    ...


# Dashboard Shiny
app = App(app_ui, server)
