# Bibliotecas
from shiny import App, render, ui
import pandas as pd
from shinywidgets import render_plotly, output_widget, render_widget
import plotly.express as px
from itables.shiny import DT

# Dados
dados = pd.read_json(
    path_or_buf = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados?formato=json"
    )
dados["data"] = pd.to_datetime(dados.data, format = "%d/%m/%Y")

# Interface do Usuário
app_ui = ui.page_navbar(
    ui.nav_panel(
        "Gráficos",
        ui.layout_columns(
            ui.card(ui.output_plot("grafico1")),
            ui.card(output_widget("grafico2"))
            )
        ),
    ui.nav_panel(
        "Tabelas",
        ui.layout_columns(
            ui.card(ui.output_data_frame("tabela1")),
            ui.card(ui.output_data_frame("tabela2"))
            ),
        ui.card(ui.HTML(DT(dados)))
    ),
    title = "Visualizações de dados"
)

# Servidor
def server(input, output, session):
    @render.plot
    def grafico1():
        return dados.query("data >= @pd.to_datetime('2000-01-01')").set_index("data").plot()
    
    @render_plotly
    def grafico2():
        return px.line(dados.query("data >= @pd.to_datetime('2000-01-01')"), x = "data", y = "valor")
    
    @render.data_frame
    def tabela1():
        return dados.tail()
    
    @render.data_frame
    def tabela2():
        return render.DataGrid(
            data = dados,
            filters = True,
            editable = True
        )


# Shiny Dashboard
app = App(app_ui, server)
