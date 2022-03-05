# import
# dcc = dash core components - the interactive elements such as drop downs
import petl as ptl
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd

# setup
app =  dash.Dash(__name__, title='Dash App')
server = app.server

# initialize
app = dash.Dash()

# layout
app.layout = html.Div([
    html.P('wooohoooo it is working')
])

# callbacks
app.callback (
    # output
    # input
    # state
)

# running
if __name__ == '__main__':
    app.run_server(debug=True)