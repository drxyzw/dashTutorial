from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# app with style sheet
external_stylesheets = [dbc.themes.CERULEAN]
app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([html.Div("My First App with Data, a Graph, and Controls",
                      className="text-primary text-center fs-3")])
    ]),
    dbc.Row([
        dcc.RadioItems(options=[{'label': x, 'value': x} for x in ['pop', 'lifeExp', 'gdpPercap']],
                      value='lifeExp', 
                      inline=True,
                      id='radio-buttons-final')
    ]),
    dbc.Row([
        dbc.Col([
            dash_table.DataTable(data=df.to_dict('records'), page_size=12, style_table={'overflowX': 'auto'})
        ], width=6),
        dbc.Col([
            dcc.Graph(figure={}, id='my-first-graph-final')
        ], width=6)
    ]),
], fluid=True)

@callback( # preprocessor/annotattion of the update_graph function
    Output(component_id='my-first-graph-final', component_property='figure'),
    Input(component_id='radio-buttons-final', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig

if __name__ == "__main__":
    app.run(debug=True)
