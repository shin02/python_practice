
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.graph_objs as go

df = pd.read_csv("time-series.csv")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Graph(
        id = 'sample-line',
        figure = {
            'data':[
                go.Scatter(
                    x = df['date'],
                    y = df['MSFT'],
                    mode = 'lines',
                    opacity = 0.7,
                    marker = {
                        'size':15
                    },
                    name = 'Microsoft'
                ),
                go.Scatter(
                    x = df['date'],
                    y = df['AAPL'],
                    mode = 'lines',
                    opacity = 0.7,
                    marker = {
                        'size':15
                    },
                    name = 'Apple'
                )
            ]
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
