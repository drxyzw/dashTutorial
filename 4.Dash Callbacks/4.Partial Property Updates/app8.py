from dash import Dash, html, Input, Output, Patch, dash_table, no_update, callback
import plotly.express as px
app = Dash()
df = px.data.iris()
app.layout = html.Div([
    html.Button('Add Rows', id='add-data-rows'),
    dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{'name': i, 'id': i} for i in df.columns],
        page_size=10,
        id='df-table'
    )
])

@callback(
    Output('df-table', 'data'),
    Input('add-data-rows', 'n_clicks'),
    prevent_initial_call=True,
)
def add_data_to_fig(n_clicks):
    if n_clicks < 10:
        patched_table = Patch()
        patched_table.extend(df.to_dict('records'))
        return patched_table
    else:
        return no_update
    
if __name__ == "__main__":
    app.run(debug=True)