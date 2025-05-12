from dash import Dash, dcc, html, Input, Output, clientside_callback

app = Dash()
app.layout = html.Div([
    dcc.Store(id="notification-permission"),
    html.Button('Notify', id='notify-btn'),
    html.Div(id='notification-output')
])

clientside_callback(
    """
    function(n_clicks) {
        if (!n_clicks) {
            return window.dash_clientside.no_update;
        }

        return new Promise((resolve, reject) => {
            navigator.permissions.query({name:'notifications'}).then(result => {
                resolve(result.state);
            }).catch(err => {
                resolve('error');
            });
        });
    }
    """,
    Output('notification-permission', 'data'),
    Input('notify-btn', 'n_clicks'),
    prevent_initial_call=True
)

clientside_callback(
    """
    function(permissionState) {
        console.log(permissionState);
        if (!permissionState) {
            return '';
        }

        if (permissionState === 'granted') {
            new Notification('Dash notification', { body: 'Notification already granted!' });
            return 'Notification sent (already granted)';
        } else if (permissionState === 'prompt') {
            return new Promise((resolve, reject) => {
                Notification.requestPermission().then(res => {
                    if (res === 'granted') {
                        new Notification('Dash notification', { body: 'Notification granted!' });
                        resolve('Notification permission granted and sent');
                    } else {
                        resolve('Notification permission denied');
                    }
                });
            });
        } else {
            return 'Permission state: ' + permissionState;
        }
    }
    """,
    Output('notification-output', 'children'),
    Input('notification-permission', 'data'),
    prevent_initial_call=True
)

if __name__ == "__main__":
    app.run(debug=True)
