from dash import Dash, dcc, html, Input, Output, Patch, callback
import plotly.express as px
app = Dash()

df = px.data.gapminder()
df = df.loc[df.year == 2002].reset_index()

fig = px.scatter(x=df.lifeExp, y=df.gdpPercap, hover_name=df.country)
fig.update_traces(marker=dict(color="blue"))

app.layout = html.Div([
    html.H4("Updating Point Colors"),
    dcc.Dropdown(id="dropdown", options=df.country.unique(), multi=True),
    dcc.Graph(id="graph-update-example", figure=fig)
])

@callback(Output('graph-update-example', 'figure'), Input('dropdown', 'value'),
          prevent_initial_call=True)
def update_markers(countries):
    country_count = list(df[df.country.isin(countries)].index)
    patched_figure = Patch()
    update_markers = [
        "red" if i in country_count else "blue" for i in range(len(df) + 1)
    ]
    patched_figure.data[0].marker.color = update_markers
    return patched_figure

if __name__ == '__main__':
    app.run(debug=True)