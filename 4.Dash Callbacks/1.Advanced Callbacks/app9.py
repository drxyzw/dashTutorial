import base64
from dash import Dash, html, Input, Output, dcc, callback, State
import os
app = Dash()
app.layout = html.Div([
    html.H1('No Output Example'),
    dcc.Upload(
        id='upload-data-to-server',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderwidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
    ),
])

@callback(
    Input('upload-data-to-server', "contents"),
    State('upload-data-to-server', 'filename'),
    running=[(Output("upload-data-to-server", "disabled"), True, False)]
)
def update_output_div(contents, filename):
    if contents is not None:
        _, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        directory = './uploaded_files'
        if not os.path.isdir(directory):
            os.mkdir(directory)
        with open(f'{directory}/{filename}', 'wb') as f:
            f.write(decoded)

if __name__ == "__main__":
    app.run(debug=True)