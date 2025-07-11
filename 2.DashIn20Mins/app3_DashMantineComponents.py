from dash import Dash, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# app with style sheet
app = Dash()

app.layout = dmc.Container([
    dmc.Title("My First App with Data, a Graph, and Controls", color = "blue", size = "h3"),
    dmc.RadioGroup(
        [dmc.Radio(x, value=x) for x in ['pop', 'lifeExp', 'gdpPercap']],
        value='lifeExp', 
        size="sm",
        id='my-dmc-radio-item'
        ),
    dmc.Grid([
        dmc.Col([
            dash_table.DataTable(data=df.to_dict('records'), page_size=12, style_table={'overflowX': 'auto'})
        ], span=6),
        dmc.Col([
            dcc.Graph(figure={}, id='graph-placeholder')
        ], span=6)
    ]),
], fluid=True)

@callback( # preprocessor/annotattion of the update_graph function
    Output(component_id='graph-placeholder', component_property='figure'),
    Input(component_id='my-dmc-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig

if __name__ == "__main__":
    app.run(debug=True)
