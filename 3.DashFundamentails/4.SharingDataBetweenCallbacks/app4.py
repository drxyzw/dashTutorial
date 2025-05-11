from dash import Dash, dcc, html, Input, Output, callback

import datetime
from flask_caching import Cache
import pandas as pd
import time
import uuid
import io

external_stylesheets = [
    # Dash CSS
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    # Loading screen CSS
    'https://codepen.io/chriddyp/pen/brPBPO.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)
cache = Cache(app.server, config={
    'CACHE_TYPE': 'FileSystemCache',
    'CACHE_DIR': './cache',
    # should be max number of concurrent users
    # higher number uses more space
    'CACHE_THRESHOLD': 200
})

def get_dataframe(session_id):
    @cache.memoize()
    def query_and_serialize_data(session_id):
        # heavy and user/session-unique data processing is done here
        now = datetime.datetime.now()

        # simulate a heavy routine 
        time.sleep(3)
        df = pd.DataFrame({
            'time': [
                str(now - datetime.timedelta(seconds=15)),
                str(now - datetime.timedelta(seconds=10)),
                str(now - datetime.timedelta(seconds=5)),
                str(now)
            ],
            'values': ['a', 'b', 'a', 'c']
        })
        return df.to_json()
    return pd.read_json(io.StringIO(query_and_serialize_data(session_id)))

def server_layout():
    session_id = str(uuid.uuid4())

    return html.Div([
        dcc.Store(data=session_id, id='session-id'),
        html.Button('Get data', id='get-data-button'),
        html.Div(id='output-1'),
        html.Div(id='output-2'),
    ])

app.layout = server_layout

@callback(Output('output-1', 'children'),
          Input('get-data-button', 'n_clicks'),
          Input('session-id', 'data'))
def display_value_1(value, session_id):
    df = get_dataframe(session_id)
    return html.Div([
        'Output 1 - Button has been clicked {} times'.format(value),
        html.Pre(df.to_csv())
    ])

@callback(Output('output-2', 'children'),
          Input('get-data-button', 'n_clicks'),
          Input('session-id', 'data'))
def display_value_2(value, session_id):
    df = get_dataframe(session_id)
    return html.Div([
        'Output 2 - Button has been clicked {} times'.format(value),
        html.Pre(df.to_csv())
    ])

if __name__ == '__main__':
    app.run(debug=True)
