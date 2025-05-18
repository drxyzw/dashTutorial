from dash import Dash, dcc, html, Input, Output, State, MATCH, ALL, ctx, callback
app = Dash()
app.layout = html.Div([
    html.Div('Dash To-Do list'),
    dcc.Input(id='new-item'),
    html.Button('Add', id='add'),
    html.Button('Clear Done', id='clear-done'),
    html.Div(id='list-container'),
    html.Div(id='totals')
])

style_todo = {'display': 'inline', 'margin': '10px'}
style_done = {'textDecoration': 'line-through', 'color': '#888'}
style_done.update(style_todo)

@callback(
    [
        Output('list-container', 'children'),
        Output('new-item', 'value'),
    ],
    [
        Input('add', 'n_clicks'),
        Input('new-item', 'value'),
        Input('clear-done', 'n_clicks'),
    ],
    [
        State('new-item', 'value'),
        State({'index': ALL}, 'children'),
        State({'index': ALL, 'type': 'done'}, 'value')
    ]
)
def edit_list(add, add2, clear, new_item, items, items_done):
    triggered = [t['prop_id'] for t in ctx.triggered]
    adding = len([1 for i in triggered if i in ('add.n_clicks', 'new-items.n_submit')])
    clearning = len([1 for i in triggered if i == 'clear-done.n_clicks'])
    new_spec = [
        (text, done) for text, done in zip(items, items_done) if not (clearning and done)
    ]
    if adding:
        new_spec.append((new_item, [])) # TODO item in the form of tuple (item name, status)
    new_list = [
        html.Div([
            dcc.Checklist(
                id={'index': i, "type": "done"},
                options=[{'label': '', 'value': 'done'}],
                value=done,
                style={'display': 'inline'},
                labelStyle={'display': 'inline'}
            ),
            html.Div(text, id={'index': i}, style=style_done if done else style_todo)
        ], style={'clear': 'both'}) for i, (text, done) in enumerate(new_spec)
    ]
    return [new_list, '' if adding else new_item]

# updating item style
@callback(
    Output({'index': MATCH}, 'style'),
    Input({'index': MATCH, 'type': 'done'}, 'value'),
)
def mark_done(done):
    return style_done if done else style_todo

# update total
@callback(
    Output('totals', 'children'),
    Input({'index': ALL, "type": 'done'}, 'value')
)
def show_totals(done):
    count_all = len(done)
    count_done = len([d for d in done if d])
    result = f'{count_done} of {count_all} items completed'
    if count_all:
        result += f' - {int(100 * count_done / count_all)}%'
    return result

if __name__ == "__main__":
    app.run(debug=True)

