import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

########### Define your variables ######

# here's the list of possible columns to choose from.
list_of_columns =['code', 'state', 'category', 'Rice', 'Wheat', 'Corn', 'Feeds',
'Grain Products']

mycolumn='Corn'
myheading1 = f"Grain Exports!"
mygraphtitle = '2019 Grain Exports by State'
mycolorscale = 'ylorrd' # Note: The error message will list possible color scales.
mycolorbartitle = "Millions USD"
tabtitle = 'CS519 Project'
sourceurl = 'https://plot.ly/python/choropleth-maps/'
githublink = 'https://github.com/kzhong678/cs519ScientificVisualizationProject'
rawdata = 'https://www.ers.usda.gov/data-products/state-agricultural-trade-data/'


########## Set up the chart

import pandas as pd
df = pd.read_csv('assets/grain_exports_2019.csv')
options_list=list(['Rice', 'Wheat', 'Corn', 'Feeds','Grain Products'])


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1(myheading1),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in options_list],
        value=options_list[0]
    ),
    dcc.Graph(id='display-value'),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Plot.ly Link", href=sourceurl),
    html.Br(),
    html.A("Raw Data", href=rawdata),
    ]
)
@app.callback(dash.dependencies.Output('display-value', 'figure'),
              [dash.dependencies.Input('dropdown', 'value')])
def grain_picker(grain_name):
    mycolumn = grain_name
    fig = go.Figure(data=go.Choropleth(
        locations=df['code'], # Spatial coordinates
        z = df[mycolumn].astype(float), # Data to be color-coded
        locationmode = 'USA-states', # set of locations match entries in `locations`
        colorscale = mycolorscale,
        colorbar_title = mycolorbartitle,
    ))
    fig.update_layout(
        title_text = mygraphtitle,
        geo_scope='usa',
        width=1200,
        height=800
    )
    return fig
############ Deploy
if __name__ == '__main__':
    app.run_server()
