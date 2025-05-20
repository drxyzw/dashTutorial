from dash import Dash, html, dcc, Input, Output, Patch, callback
from plotly import graph_objects as go

app = Dash()
x = ['Product A', 'Product B', 'Product C']
y = [20, 14, 13]
fig = go.Figure(data=[go.Bar(x=x, y=y)])
app.layout = html.Div([
    html.Button('Update products', id='add-product-d-e'),
    dcc.Graph(figure=fig, id='prepend-append-example-graph')
])
@callback(
    Output('prepend-append-example-graph', 'figure'),
    Input('add-product-d-e', 'n_clicks'),
    prevent_initial_call=True
)
def add_data_to_fig(n_clicks):
    if n_clicks % 2 == 1:
        pathced_figure = Patch()
        pathced_figure['data'][0]['x'].prepend('Product D')
        pathced_figure['data'][0]['y'].prepend(34)
        pathced_figure['data'][0]['x'].append('Product E')
        pathced_figure['data'][0]['y'].append(44)
        return pathced_figure
    else:
        return fig

if __name__ == "__main__":
    app.run(debug=True)
