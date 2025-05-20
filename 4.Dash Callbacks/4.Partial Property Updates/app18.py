from dash import Dash, dash_table, html, Input, Output, Patch, callback
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/solar.csv")
app = Dash()
app.layout = html.Div([
    html.Button('Delete first row', id='delete-button'),
    html.Button('Reload data', id='reload-button'),
    dash_table.DataTable(
        df.to_dict('records'),
        [{'name': i, 'id': i} for i in df.columns],
        id='table-example-for-delete'
    )
])

# Returning all the records
@callback(
    Output('table-example-for-delete', 'data'),
    Input('reload-button', 'n_clicks')
)
def reload_data(n_clicks):
    return df.to_dict('records')

# delete rows at index 0
@callback(
    Output('table-example-for-delete', 'data', allow_duplicate=True),
    Input('delete-button', 'n_clicks'),
    prevent_initial_call = True
)
def delete_records(n_clicks):
    patched_table = Patch()
    del patched_table[0]
    return patched_table

if __name__ == "__main__":
    app.run(debug=True)