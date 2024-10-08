# Bibliotecas
from shiny import App, render, ui
from plotnine.data import economics
import plotnine as p9

# Dados


# Interface do Usuário
app_ui = ui.page_navbar(
    ui.nav_panel(
        "Visualizações",
        ui.layout_sidebar(
            ui.sidebar(
                ui.input_select(
                    id = "variavel",
                    label = ui.strong("Selecione uma variável:"),
                    choices = economics.columns[1:].to_list()
                ),
                widht = 200
            ),
            ui.layout_columns(
                ui.card(ui.output_plot("grafico")),
                ui.card(ui.output_data_frame("tabela")),
                col_widths = [8, 4]
            )
        )
    ),
    title = "Inputs e Outputs"
)

# Servidor
def server(input, output, session):
    @render.plot
    def grafico():
        return (
            p9.ggplot(economics) +
            p9.aes(x = "date", y = "unemploy") +
            p9.geom_point() +
            p9.geom_smooth()
        )
    
    @render.data_frame
    def tabela():
        return economics.filter(items = ["date", "unemploy"])

# Shiny Dashboard
app = App(app_ui, server)
