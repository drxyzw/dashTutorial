from dash import Dash, dcc, Input, Output, callback, html
app = Dash(__name__, suppress_callback_exceptions=True)
server = app.server
app.layout = html.Div([
    dcc.Location(id='url'),
    html.Div(id="layout-div"),
    html.Div(id="content"),
])

@callback(Output('content', 'children'), Input('url', 'pathname'))
def display_page(pathname):
    return html.Div([
        dcc.Input(id="input", value='hello world'),
        html.Div(id='output')
    ])

@callback(Output('output', 'children'), Input('input', 'value'), prevent_initial_call=True)
def update_output(value):
    print('>>> update_output')
    return value

# this will executed because 1) app.layout already contains layout-div, and 2) display_page() is triggered after (1)
@callback(Output('layout-div', 'children'), Input('input', 'value'), prevent_initial_call=True)
def update_layout_div(value):
    print('>>> update?layout_div')
    return value

if __name__ == '__main__':
    app.run(debug=True)
