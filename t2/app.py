import dash
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

def get_c1():
    return html.Div(html.Button('Click', id='button'))

def get_c2():
    return html.Div(html.Label('Place Holder', id='output'))

def get_layout():
    return html.Div([
        get_c1(),
        get_c2()
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
