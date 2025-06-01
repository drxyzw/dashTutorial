from dash import Dash, Input, Output, html, dcc, callback
import plotly.express as px
import plotly.graph_objects as go

app = Dash()
app.layout = html.Div([
    html.Button('Draw Graph', id='draw'),
    html.Button('Reset Graph', id='reset'),
    dcc.Graph(id='graph', figure=go.Figure())
])
@callback(
    Output('graph', 'figure', allow_duplicate=True),
    Input('draw', 'n_clicks'),
    prevent_initial_call=True,
)
def draw_graph(b):
    df = px.data.iris()
    return px.scatter(df, x = df.columns[0], y = df.columns[1])

@callback(
    Output('graph', 'figure'),
    Input('reset', 'n_clicks'),
    prevent_initial_call=True
)
def reset_graph(b):
    return go.Figure()

if __name__ == "__main__":
    app.run(debug=True)
