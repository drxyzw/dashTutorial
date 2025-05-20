from dash import Dash, html, dcc, Input, Output, Patch, callback, dash_table
from plotly import graph_objects as go

app = Dash()
x = ['Product A', 'Product B', 'Product C']
y = [20, 14, 13]
table_data = [{'Product': x_value, 'Value': y_value} for x_value, y_value in zip(x, y)]
additional_products_x = ['Product D', 'Product E', 'Product F']
additional_products_y = [10, 4, 7]
fig = go.Figure(data=[go.Bar(x=x, y=y)])
app.layout = html.Div([
    html.Button('Update products', id='add-additional-products'),
    dcc.Graph(figure=fig, id='multiple-outputs-fig'),
    dash_table.DataTable(data=table_data, id='multiple-outputs-table')
])
@callback(
    Output('multiple-outputs-fig', 'figure'),
    Output('multiple-outputs-table', 'data'),
    Input('add-additional-products', 'n_clicks'),
    prevent_initial_call=True
)
def add_data_to_fig(n_clicks):
    if n_clicks % 2 == 1:
        pathced_figure = Patch()
        pathced_table = Patch()

        additional_products_table_data = [{'Product': x_value, 'Value': y_value}
                      for x_value, y_value in zip(additional_products_x, additional_products_y)]
        pathced_table.extend(additional_products_table_data)


        pathced_figure['data'][0]['x'].extend(additional_products_x)
        pathced_figure['data'][0]['y'].extend(additional_products_y)

        return pathced_figure, pathced_table
    else:
        return fig, table_data

if __name__ == "__main__":
    app.run(debug=True)
