# import
import petl as ptl
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import plotly.express as ex
import pandas as pd

# setup
app =  dash.Dash(__name__, title='Dash Deployment')
server = app.server

# initialize
app = dash.Dash()

# layout
app.layout = html.Div([
    html.H1('Sales Data, 2010-2020', className='header'),
])

# callbacks


# running
if __name__ == '__main__':
    app.run_server(debug=True)