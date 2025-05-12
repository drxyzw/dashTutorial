from dash import Dash, dcc, html, Input, Output, State, callback
import time
app = Dash()

app.layout = html.Div([
    html.Div(dcc.Input(id='input-on-submit-text', type='text')),
    html.Button('Submit', id='submit-button', n_clicks=0),
    html.Div(id='container-output-text',
             children='Enter a value and press submit')
])

@callback(
    Output('container-output-text', 'children'),
    Input('submit-button', 'n_clicks'),
    State('input-on-submit-text', 'value'),
    prevent_initial_call=True,
    running=[(Output('submit-button', 'disabled'), True, False)]
)
def update_ouptut(n_clicks, value):
    time.sleep(5),
    return 'The input value "{}" and the button has been cclicked {} times'.format(
        value,
        n_clicks
    )

if __name__ == '__main__':
    app.run(debug=True)