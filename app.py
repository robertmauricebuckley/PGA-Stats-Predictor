import dash  
import dash_core_components as dcc 
import dash_html_components as html 
import dash_bootstrap_components as dbc
import plotly.graph_objs as go 
from dash.dependencies import Input, Output, State
import pandas as pd
# import pdpbox.pdp 
import pickle 

#############Initiate the app
external_stylesheets = [
    dbc.themes.LUX, # Bootswatch theme
    'https://use.fontawesome.com/releases/v5.9.0/css/all.css', # for social media icons
]
app = dash.Dash(__name__, external_stylesheets = external_stylesheets)  
app.config.suppress_callback_exceptions = True
server = app.server 
app.title='PGA Stats Predictor'



app.layout = html.Div(children=[
    html.H1('Stat Interactions'),
    html.Div([
        html.H6('Choose a Stat'),
        dcc.Graph(id='pdp'),
        dcc.Dropdown(
            id='stat-choice',
            options=[
                {'label': 'Total Drives', 'value': 'Total_Driving_-_(TOTAL)'},
                {'label': 'Driving Distance Rank', 'value': 'Total_Driving_-_(DISTANCE_RANK)'},
                {'label': 'Driving Distance Average', 'value': 'Driving_Distance_-_(AVG.)'},
                {'label': 'Year', 'value': 'Year'}
            ],
            multi=True,
            value="MTL"
        ),
        # html.H6('Choose a Second Stat to compare to the first'),
        # dcc.Slider(
        #     id="year",
        #     min=2008,
        #     max=2017,
        #     step=1,
        #     marks={i:str(i) for i in range(2008, 2018)},
        #     value=2008
        # ),
        # html.H6(id='output-message', childern='output will go here'),
    ]),
    html.Br(),
    html.A(html.I(className='fab fa-github-square mr-1'), href='https://github.com/robertworkbuckley/PGA-Stats-Predictor')
])

############ Interactive Callbacks
# @app.callback(Output('pdp', 'figure'),
#             [Input('stat-choice', 'value')
#             ])
# def display_results(stat):
#     file = open()
########## Execute the app
if __name__ == '__main__':
    app.run_server()