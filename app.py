import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables
beers=['Beer 1', 'Beer 2', 'Beer 3', 'Beer 4]
ibu_values=[35, 65, 80, 70]
abv_values=[5.9, 4.1, 10.2, 3.3]
color1='darkgreen'
color2='blue'
mytitle='Beer Comparison'
tabtitle='beer!'
myheading='Beer Company'
label1='IBU'
label2='ABV'
githubLink='https://github.com/kzhong678/flying-dog-beers'
originalGithublink='https://github.com/austinlasseter/flying-dog-beers'

########### Set up the chart
bitterness = go.Bar(
    x=beers,
    y=ibu_values,
    name=label1,
    marker={'color':color1}
)
alcohol = go.Bar(
    x=beers,
    y=abv_values,
    name=label2,
    marker={'color':color2}
)

beer_data = [bitterness, alcohol]
beer_layout = go.Layout(
    barmode='group',
    title = mytitle
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='flyingdog',
        figure=beer_fig
    ),
    html.A('The code for this project can be found here.', href=githubLink),
    html.Br(),
    html.A('This code was forked from this repo', href=originalGithublink),
    ]
)

if __name__ == '__main__':
    app.run_server()
