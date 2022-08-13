import pandas as pd
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html

df = pd.read_csv("6 Аварии/date.csv")

fig = go.Figure()
fig.add_trace(go.Scattermapbox(
    lat=list(df["coordW"]),
    lon=list(df["coordL"]),
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=5
    ),
    subplot='mapbox',
))

fig.update_layout(
    hovermode='closest',
    mapbox=dict(
        style='open-street-map',
        bearing=0,
        center=go.layout.mapbox.Center(
            lat=55.62,
            lon=37.6243
        ),
        zoom=8
    )
)

fig.update_layout(height=800)

app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=False, use_reloader=False, port=8088)
