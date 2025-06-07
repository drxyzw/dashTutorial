from dash import Dash, html, dcc, Input, Output, callback

def update_output_error_handler(err):
    return f"There was an error processing your input. Error+ {err}. Enter anotehr value."

app = Dash(on_error=update_output_error_handler)
app.layout = html.Div([
    dcc.Input(id='input-number', type='number', value=1),
    html.Div(id='output-div')
])

@callback(
    Output('output-div', 'children'),
    Input('input-number', 'value')
)
def update_output(value):
    result = 10 / value
    return f'The result is {result}'

if __name__ == "__main__":
    app.run(debug=False)
