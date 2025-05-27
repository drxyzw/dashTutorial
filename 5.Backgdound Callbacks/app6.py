import time
import os

from dash import Dash, DiskcacheManager, CeleryManager, Input, Output, html, callback, set_props

import dash_ag_grid as dag
from plotly.express import data

if "REDIS_URL" in os.environ:
    from celery import Celery
    celery_app = Celery(
        __name__, broker=os.environ['REDIS_URL'], backend=os.environ['REDIS_URL']
    )
    backend_callback_manager = CeleryManager(celery_app)
else:
    import diskcache
    cache = diskcache.Cache("./cache")
    backend_callback_manager = DiskcacheManager(cache)

app = Dash(background_callback_manager=backend_callback_manager)

app.layout = [
    html.Button(id='button_id', children='Get data'),
    html.Button(id='cancel_button_id', children='Cancel Running Job!'),
    dag.AgGrid(
        id="ag-grid-updating",
        dashGridOptions={"pagination": True}
    )
]

@callback(
    Input('button_id', 'n_clicks'),
    background=True,
    running=[
        (Output('button_id', 'disabled'), True, False),
        (Output('cancel_button_id', 'disabled'), False, True),
    ],
    cancel=[Input('cancel_button_id', 'n_clicks')]
)
def update_progress(n_clicks):
    df = data.gapminder()
    columnDefs = [{'field': col} for col in df.columns]
    # simulate 100 rows of data being returned every 2 seconds
    rows_per_step = 100
    total_rows = len(df)
    while total_rows > 0:
        end = len(df) - total_rows + rows_per_step
        total_rows -= rows_per_step
        time.sleep(2.)
        set_props(
            "ag-grid-updating",
            {'rowData': df[:end].to_dict('records'), 'columnDefs': columnDefs},
        )

if __name__ == "__main__":
    app.run(debug=True)
