import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import requests
import pandas
import plotly.express as px
from dash.dependencies import Input, Output, State


URL = "http://localhost:8000/greenspace"
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

px.set_mapbox_access_token(os.environ["MAPBOX_TOKEN"])

app.layout = html.Div([
    html.H1('Green Nearby'),
    dcc.Input(id="input-address", type="text", value=''),
    html.Button(id='submit-button-state', type='submit', n_clicks=0, children='Submit'),
    html.Div(id="out-input"),

    dcc.Graph(
        id='greenspace_map',

    )
])

@app.callback(
    Output("greenspace_map", "figure"),
    [Input('submit-button-state', 'n_clicks')],
    [State("input-address", "value")]
)
def address_render(n_clicks, address):
    print(address)
    print(n_clicks)
    if not address:
        address = "139 Tremont St, Boston, MA 02111"
    payload = {
        "name": address
    }
    response = requests.request("POST", URL, json=payload)
    df = pandas.read_json(response.text)
    fig = px.scatter_mapbox(df, text="name", lat="lat", lon="long", zoom=14)
    fig.update_layout(transition_duration=500)

    return fig
    

if __name__ == '__main__':
    app.run_server(debug=True)
