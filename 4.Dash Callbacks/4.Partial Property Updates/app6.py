from dash import Dash, html, dcc, Input, Output, Patch, callback
app = Dash()
import plotly.express as px
import random
x_values = [2019, 2020, 2021, 2022, 2023]
y_values = [random.randrange(1, 30, 1) for i in range(len(x_values))]
fig = px.bar(x=x_values, y=y_values)

app.layout = html.Div([
    html.Button('Prepend', id='prepend-new-val', n_clicks=0),
    dcc.Graph(figure=fig, id='prepend-example-graph')
])

@callback(
    Output('prepend-example-graph', 'figure'),
    Input('prepend-new-val', 'n_clicks')
)
def add_data_to_fig(n_clicks):
    random_value = random.randrange(1, 30, 1)
    patched_figure = Patch()
    patched_figure.data[0].x.prepend(2019 - n_clicks)
    patched_figure.data[0].y.prepend(random_value)
    return patched_figure

if __name__ == "__main__":
    app.run(debug=True)