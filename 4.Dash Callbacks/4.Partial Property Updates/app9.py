from dash import Dash, html, dcc, Input, Output, Patch, callback
from plotly import graph_objects as go
app = Dash()
x = ['Product A', 'Product D', 'Product E', 'Product F']
y = [20, 14, 23, 8]
fig = go.Figure(data=[go.Bar(x=x, y=y)])

app.layout = html.Div([
    html.Button('Update products', id='additional-products', n_clicks=0),
    dcc.Graph(figure=fig, id='extend-example')
])
@callback(
    Output('extend-example', 'figure'),
    Input('additional-products', 'n_clicks'),
    prevent_initial_call=True
)
def add_data_to_fig(n_clicks):
    if n_clicks % 2 == 1:
        patched_figure = Patch()
        patched_figure.data[0].x.insert(1, "Product B")
        patched_figure.data[0].y.insert(1, 10)
        return patched_figure
    else:
        return fig

if __name__ == "__main__":
    app.run(debug=True)