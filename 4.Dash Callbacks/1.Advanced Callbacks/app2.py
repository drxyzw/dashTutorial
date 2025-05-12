from dash import Dash, dcc, html, Input, Output, callback, no_update
from dash.exceptions import PreventUpdate

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.P('Enter a composite number ot see its prime factors'),
    dcc.Input(id="num", type="number", debounce=True, min=2, step=1),
    html.P(id="err", style={'color': 'red'}),
    html.P(id='out')
])

@callback(
    Output('out', 'children'),
    Output('err', 'children'),
    Input('num', 'value')
)
def show_factors(num):
    if num is None:
        raise PreventUpdate
    
    factors = prime_factors(num)
    if len(factors) == 1:
        return no_update, '{} is prime!'.format(num)
    return '{} is {}'.format(num, ' * '.join(str(n) for n in factors)), ''

def prime_factors(num):
    n, i, out = num, 2, []
    while i * i <= n:
        if n % i == 0:
            out.append(i)
            n = int(n/i)
        else:
            i += (1 if i==2 else 2) # if i is 2 then next is 3, if i > 2, then next prime number candidate is i+2
    out.append(n)
    return out

if __name__ == '__main__':
    app.run(debug=True)