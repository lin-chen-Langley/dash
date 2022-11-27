import dash
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MORPH])

def get_c1():
    return html.Div(dbc.Button('Click', color='warning', id='button'))

def get_c2():
    return html.Div(html.Label('Place Holder', id='output', className='output-style'))

def get_layout():
    return html.Div([
        dbc.Container([
        dbc.Row(
            [
                dbc.Col(get_c1(), width=3),
                dbc.Col(get_c2(), width=3),
            ]
        )
        ])
    ])

app.layout = get_layout()

@app.callback(
    Output("output", "children"),
    Input("button", "n_clicks"),
)
def update_click(n):
    number = n if n is not None else 0
    return str(number)

if __name__ == "__main__":
    app.run_server(debug=True)
