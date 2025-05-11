import os
import copy
import time
from dash import Dash, dcc, html, Input, Output, callback
import numpy as np
import pandas as pd
from flask_caching import Cache

external_stylesheets = [
    # Dash CSS
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    # Loading screen CSS
    'https://codepen.io/chriddyp/pen/brPBPO.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

CACHE_CONFIG = {
    'CACHE_TYPE': 'FileSystemCache', # 'redis'
    'CACHE_DIR': './cache',
    # 'CACHE_REDIS_URL': os
}

cache = Cache()
cache.init_app(app.server, config=CACHE_CONFIG)

N = 100

df = pd.DataFrame({
    'category': (
        (['apples'] * 5 * N) +
        (['oranges'] * 10 * N) +
        (['figs'] * 20 * N) +
        (['pinapples'] * 15 * N)
    )
})
df['x'] = np.random.randn(len(df['category']))
df['y'] = np.random.randn(len(df['category']))

app.layout = html.Div([
    dcc.Dropdown(df['category'].unique(), 'apples', id='dropdown'),
    html.Div([
        html.Div(dcc.Graph(id='graph-1'), className='six columns'),
        html.Div(dcc.Graph(id='graph-2'), className='six columns'),
    ], className="row"),
    html.Div([
        html.Div(dcc.Graph(id='graph-3'), className='six columns'),
        html.Div(dcc.Graph(id='graph-4'), className='six columns'),
    ], className="row"),
    dcc.Store(id='signal')
])

# perform expensive computations in the "global store"
# these computations are cached in a globally available
# redis memory store which is available across proceses and for all time
# use file system cache here
@cache.memoize()
def global_store(value):
    # conduct heavy process
    print(f'Computing value with {value}')
    time.sleep(3)
    return df[df['category'] == value]

def generate_figure(value, figure):
    fig = copy.deepcopy(figure)
    filtered_df = global_store(value)
    fig['data'][0]['x'] = filtered_df['x']
    fig['data'][0]['y'] = filtered_df['y']
    fig['layout'] = {'margin': {'l': 20, 'r': 10, 'b': 20, 't': 10}}
    return fig

@callback(Output('signal', 'data'), Input('dropdown', 'value'))
def compute_value(value):
    global_store(value)
    return value

@callback(Output('graph-1', 'figure'), Input('signal', 'data'))
def update_graph_1(value):
    return generate_figure(value, {
        'data': [{
            'type': 'scatter',
            'mode': 'markers',
            'marker': {
                'opacity': 0.5,
                'size': 14,
                'line': {'border': 'thin darkgrey solid'}
            }
        }]
    })

@callback(Output('graph-2', 'figure'), Input('signal', 'data'))
def update_graph_2(value):
    return generate_figure(value, {
        'data': [{
            'type': 'scatter',
            'mode': 'lines',
            'line': {'shape': 'spline', 'width': 0.5}
        }]
    })

@callback(Output('graph-3', 'figure'), Input('signal', 'data'))
def update_graph_3(value):
    return generate_figure(value, {
        'data': [{
            'type': 'histogram',
        }]
    })

@callback(Output('graph-4', 'figure'), Input('signal', 'data'))
def update_graph_4(value):
    return generate_figure(value, {
        'data': [{
            'type': 'histogram2dcontour',
        }]
    })

if __name__ == "__main__":
    # app.run(debug=True, processes=6, threaded=False)
    # to avoid "Your platform does not support forking."
    app.run(debug=True)

