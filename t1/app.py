import dash
from dash import html

app = dash.Dash(__name__)

def get_layout():
    return html.Div([
        html.H1('Title'),
        html.P('Content'),
        html.Div([
            html.Li('Item')
        ])
    ])

app.layout = get_layout()

if __name__ == "__main__":
    app.run_server(debug=True)
