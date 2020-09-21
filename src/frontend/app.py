import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import requests
import pandas
import plotly.express as px
from dash.dependencies import Input, Output


URL = "http://api/greenspace"
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

px.set_mapbox_access_token(os.environ["MAPBOX_TOKEN"])

payload = {
 "name": "710 Centre St, Jamaica Plain, MA 02130"
}
response = requests.request("POST", URL, json=payload)
df = pandas.read_json(response.text)
fig = px.scatter_mapbox(df, text="name", lat="lat", lon="long", zoom=14)

app.layout = html.Div(children=[
    html.H1(children='Green Nearby'),

    dcc.Input(id="input-address", type="text"),
    html.Div(id="out-input"),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

@app.callback(
    Output("out-input", "children"),
    [Input("input-address", "value")],
)
def address_render(address):
   return address 
    

server = app.server


if __name__ == '__main__':
    app.run_server(debug=True)
