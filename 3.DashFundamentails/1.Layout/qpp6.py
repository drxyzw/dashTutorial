from dash import Dash, html, dcc
app = Dash()

app.layout = html.Div([
    html.Div(children=[
        html.Label('Dropdown'),
        dcc.Dropdown(['New York City', 'Montreal', 'San Francisco'], 'Montreal'),

        html.Br(),
        html.Label('Multi-Select Dropdown'),
        dcc.Dropdown(['New York City', 'Montreal', 'San Francisco'],
                     ['Montreal', 'San Francisco'],
                     multi=True),

        html.Br(),
        html.Label('Radio Items'),
        dcc.RadioItems(['New York City', 'Montreal', 'San Francisco'], 'Montreal'),
    ], style={'padding': 10, 'flex': 1}),
    html.Div(children=[
        html.Label('Checkboxes'),
        dcc.Checklist(['New York City', 'Montreal', 'San Francisco'],
                     ['Montreal', 'San Francisco']),
        html.Br(),
        html.Label('Slider'),
        dcc.Slider(
            min=0,
            max=9,
            marks={i: f'Label {i}' if i==1 else str(i) for i in range(1,6)},
            value=5,
        ),
    ], style={'padding': 10, 'flex': 1})
], style={'display': 'flex', 'flexDirection': 'row'})

if __name__ == '__main__':
    app.run(debug=True)
