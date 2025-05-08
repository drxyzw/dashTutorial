from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# app with style sheet
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(external_stylesheets=external_stylesheets)

app.layout = [html.Div(className='row', children="My First App with Data, a Graph, and Controls",
                       style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}),

              html.Div(className='row', children=[
                  dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'],
                                value='lifeExp', 
                                inline=True,
                                id='controls-and-radio-item')
              ]),
              html.Div(className='ror', children=[
                  html.Div(className='six columns', children=[
                      dash_table.DataTable(data=df.to_dict('records'), page_size=6),
                  ]),
                  html.Div(className='six columns', children=[
                      dcc.Graph(figure={}, id='controls-and-graph')
                  ])
              ])
]

@callback( # preprocessor/annotattion of the update_graph function
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig

if __name__ == "__main__":
    app.run(debug=True)
