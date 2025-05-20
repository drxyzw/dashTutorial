from dash import Dash, html, dcc, Input, Output, Patch, callback
from plotly import graph_objects as go

app = Dash()
x = ['Product A', 'Product B', 'Product C']
y = [20, 14, 13]
fig = go.Figure(data=[go.Bar(x=x, y=y)])
app.layout = html.Div([
    dcc.Graph(figure=fig, id='increment-example-graph')
])
@callback(
    Output('increment-example-graph', 'figure'),
    Input('increment-example-graph', 'clickData'),
    prevent_initial_call=True
)
def check_selected_data(click_data):
    selected_product = click_data['points'][0]['label']
    pathced_figure = Patch()
    index = x.index(selected_product)
    pathced_figure.data[0].y[index] += 1
    return pathced_figure

if __name__ == "__main__":
    app.run(debug=True)
