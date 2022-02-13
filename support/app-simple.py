import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import pandas as pd

########### Define your variables ######

tabtitle = 'Old McDonald'
sourceurl = 'https://plot.ly/python/choropleth-maps/'
githublink = 'https://github.com/austinlasseter/agriculture-exports-map'
# here's the list of possible columns to choose from.
list_of_columns =['total exports', 'beef', 'pork', 'poultry',
       'dairy', 'fruits fresh', 'fruits proc', 'total fruits', 'veggies fresh',
       'veggies proc', 'total veggies', 'corn', 'wheat', 'cotton']


########## Set up the chart

import pandas as pd
df = pd.read_csv('assets/usa-2011-agriculture.csv')

data=go.Choropleth(
    locations=df['code'], # Spatial coordinates
    locationmode = 'USA-states', # set of locations match entries in `locations`
    z = df['corn'], # Data to be color-coded
    colorscale = ['lightgrey','blue'],
    colorbar_title = 'some title',
)
fig = go.Figure([data])
fig.update_layout(
        title_text = 'my title',
        geo_scope='usa',
        width=1200,
        height=800
    )


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1('2011 Agricultural Exports, by State'),
    html.Div([
        html.Div([
                html.H6('Select a variable for analysis:'),
        ], className='two columns'),
        html.Div([dcc.Graph(figure=fig, id='fig1'),
            ], className='ten columns'),
    ], className='twelve columns'),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)



############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)
