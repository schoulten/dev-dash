# Bibliotecas
from shiny import ui, render, App, reactive
from bcb import currency
import pandas as pd
import shinyswatch as ssw
import plotnine as p9

# Interface do Usuário
app_ui = ui.page_navbar(
    ui.nav_panel(
        "📊",
        ui.layout_sidebar(
            ui.sidebar(
                ui.input_select(
                    id = "moeda",
                    label = "Moeda:",
                    choices = currency.get_currency_list().symbol.sort_values().to_list(),
                    selected = "AUD"
                ),
                ui.input_date_range(
                    id = "periodo",
                    label = "Data inicial e final:",
                    start = (pd.to_datetime("today") - pd.offsets.MonthBegin(24)).strftime("%Y-%m-%d"),
                    end = pd.to_datetime("today").strftime("%Y-%m-%d"),
                    max = pd.to_datetime("today").strftime("%Y-%m-%d"),
                    language = "pt-BR",
                    separator = " - "
                ),
                ui.input_radio_buttons(
                    id = "tipo",
                    label = "Tipo de taxa:",
                    choices = {"bid": "Compra", "ask": "Venda"}
                ),
                width = 275
            ),
            ui.card(
                ui.card_header("Taxa de câmbio"),
                ui.output_plot("grafico"),
                ui.card_footer("Dados: BCB | Elaboração: Análise Macro")
                )
        )
    ),
    title = "Câmbio App",
    theme = ssw.theme.cyborg
)

# Servidor
def server(input, output, session):

    @reactive.calc
    def coleta_dados():
        dados = currency.get(
            symbols = input.moeda(),
            start = input.periodo()[0],
            end = input.periodo()[1],
            side = "both"
            )[input.moeda()].reset_index()
        return dados

    @render.plot
    def grafico():
        return (
            p9.ggplot(coleta_dados()) +
            p9.aes(x = "Date", y = input.tipo()) +
            p9.geom_line() +
            p9.labs(
                y = input.moeda().upper() + " / BRL",
                x = ""
            )
        )

# Dashboard Shiny
app = App(app_ui, server)
