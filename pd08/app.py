from shiny import ui, App


# Interface do usuário ----
app_ui = ui.page_navbar(
    ui.nav(
        "Página 1",
        ui.layout_sidebar(
            ui.panel_sidebar(
                ui.markdown(
                    """
                    Um texto em **negrito** ou em *itálico*.

                    Um parágrafo com um [link](https://analisemacro.com.br/).

                    - Item 1
                    - Item 2
                    - Item 3

                    ![](https://aluno.analisemacro.com.br/wp-content/uploads/dlm_uploads/2023/05/logo_am_45.png)
                    """
                ),
            width = 3
            ),
            ui.panel_main(
                "Painel de conteúdo principal",
                ui.row(
                    ui.column(6, "Linha 1 - Coluna A", style = "background-color: red;"),
                    ui.column(6, "Linha 1 - Coluna B", style = "background-color: purple;")
                    ),
                ui.row(
                    ui.column(4, "Linha 2 - Coluna C", style = "background-color: yellow;"),
                    ui.column(4, "Linha 2 - Coluna D", style = "background-color: black;"),
                    ui.column(4, "Linha 2 - Coluna E", style = "background-color: orange;")
                    ),
                style = "background-color: gray;"
                )
        )
        ),
    ui.nav("Página 2"),
    ui.nav_control(ui.a("Análise Macro", href = "https://analisemacro.com.br/")),
    ui.nav_menu(
        "Mais",
        ui.nav_control(ui.a("Blog", href = "https://analisemacro.com.br/blog/")),
        ui.nav_control(ui.a("LinkedIn", href = "https://br.linkedin.com/company/an%C3%A1lise-macro"))
        ),
    title = ui.row(
        ui.column(3, ui.img(src = "https://aluno.analisemacro.com.br/wp-content/uploads/dlm_uploads/2023/05/logo_am_45.png")),
        ui.column(9, "Título da Dashboard")
    ),
    bg = "blue",
    inverse = True
)


# Servidor ----
def server(input, output, session):
    ...


# Dashboard Shiny App
app = App(app_ui, server)
