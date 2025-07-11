from dash import Dash, html, Input, Output, callback
from datetime import datetime
import time
app = Dash()
app.layout = html.Div([
    html.Button('execute callbacks', id='button_2'),
    html.Div(children='callback not executed', id='first_output_2'),
    html.Div(children='callback not executed', id='second_output_2'),
    html.Div(children='callback not executed', id='third_output_2'),
    html.Div(children='callback not executed', id='fourth_output_2'),
])

@callback(
    Output('first_output_2', 'children'),
    Output('second_output_2', 'children'),
    Input('button_2', 'n_clicks'),
    prevent_initial_call=True
)
def first_callback(n):
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    return ['in the first callback, it is ' + current_time, " in the first callback, it is " + current_time]

@callback(
    Output('third_output_2', 'children'), Input('second_output_2', 'children'), prevent_initial_call=True
)
def second_callback(n):
    time.sleep(2)
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    return 'in the second callback, it is ' + current_time

@callback(
    Output('fourth_output_2', 'children'),
    Input('first_output_2', 'children'),
    Input('third_output_2', 'children'),
    prevent_initial_call = True
)
def second_callback(n, m):
    time.sleep(2)
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    return 'in the second callback, it is ' + current_time

if __name__ == '__main__':
    app.run(debug=True)
