from dash import Dash, dcc, html, Input, Output, callback

app = Dash()

app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ", my_input := dcc.Input(value='initial value', type='text')
    ]),
    html.Br(),
    my_output := html.Div(),
])

@callback(
    Output(my_output, component_property='children'),
    Input(my_input, component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}'

if __name__ == '__main__':
    app.run(debug=True)
