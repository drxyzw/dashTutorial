from dash import Dash, html, Input, Output, callback, dcc, dash_table
import plotly.express as px
import pandas as pd
import io

app = Dash()

app.layout = html.Div([
    dcc.Graph(id="graph"),
    dash_table.DataTable(id='table'),
    # html.Table(id="table"),
    dcc.Dropdown(id='dropdown', options=[1, 2, 3, 4, 5], value=2),

    dcc.Store(id='intermediate-value')
])

def slow_processing_dummy(value):
    return pd.DataFrame({'index': [1,2,3], 'value': [value, value*2, value*(-2)]})

@callback(Output('intermediate-value', 'data'), Input('dropdown', 'value'))
def clean_data(value):
    cleaned_df = slow_processing_dummy(value)
    return cleaned_df.to_json(date_format='iso', orient='split')

@callback(Output('graph', 'figure'), Input('intermediate-value', 'data'))
def update_grapg(jsonnified_cleaned_data):
    dff = pd.read_json(io.StringIO(jsonnified_cleaned_data), orient='split')
    figure = px.line(dff, x='index', y='value')
    return figure

@callback(Output('table', 'data'), Input('intermediate-value', 'data'))
def update_table(jsonified_cleaned_data):
    dff = pd.read_json(io.StringIO(jsonified_cleaned_data), orient='split')
    df_dict = dff.to_dict('records')
    return df_dict

if __name__ == "__main__":
    app.run(debug=True)
