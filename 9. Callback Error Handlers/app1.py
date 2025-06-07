from dash import Dash, html, dcc, Input, Output, callback
def custom_error_handler(err):
    print(f'The app raised the following exception: {err}')

app = Dash(on_error=custom_error_handler)
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


if __name__ == '__main__':
    # app.run(debug=True)
    # app.run(debug=False)
    app.run(debug=False)