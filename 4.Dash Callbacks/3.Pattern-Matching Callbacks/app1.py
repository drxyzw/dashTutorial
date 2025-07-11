from dash import Dash, dcc, html, Input, Output, ALL, Patch, callback
app = Dash()
app.layout = html.Div([
    html.Button('Add Filter', id='add-filter-btn', n_clicks=0),
    html.Div(id='dropdown-container-div', children=[]),
    html.Div(id='dropdown-container-output-div')
])

@callback(
    Output('dropdown-container-div', 'children'), Input('add-filter-btn', 'n_clicks')
)
def display_dropdowns(n_clicks):
    patched_childern = Patch()
    new_dropdown = dcc.Dropdown(
        ['NYC', 'MTL', 'LA', 'TOKYO'],
        id={'type': 'city-filter-dropdown', 'index': n_clicks},
    )
    patched_childern.append(new_dropdown)
    return patched_childern

@callback(
    Output('dropdown-container-output-div', 'children'),
    Input({'type': 'city-filter-dropdown', 'index': ALL}, 'value'),
)
def display_output(values):
    return html.Div(
        [html.Div(f'Dropdown {i + 1} = {value}') for (i, value) in enumerate(values)]
    )

if __name__ == "__main__":
    app.run(debug=True)