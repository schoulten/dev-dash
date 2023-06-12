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
            ui.panel_main()
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
