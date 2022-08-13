import pandas as pd
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html

df = pd.read_csv("6 Аварии/transformation.csv")

fig = go.Figure()

clear = df.loc[df["isClear"] == 1]
cloudy = df.loc[df["isCloudy"] == 1]
precipitation = df.loc[df["isClear"] + df["isCloudy"] == 0]

fig.add_trace(go.Scattermapbox(
    lat=list(clear["coordW"]),
    lon=list(clear["coordL"]),
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=4,
        color="red"
    ),
    subplot='mapbox1',
    name="clear"
))

fig.add_trace(go.Scattermapbox(
    lat=list(cloudy["coordW"]),
    lon=list(cloudy["coordL"]),
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=4,
        color="green"
    ),
    subplot='mapbox1',
    name="cloudy"
))

fig.add_trace(go.Scattermapbox(
    lat=list(precipitation["coordW"]),
    lon=list(precipitation["coordL"]),
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=4,
        color="blue"
    ),
    subplot='mapbox1',
    name="precipitation"
))

fig.update_layout(
    hovermode='closest',
    mapbox1=dict(
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
fig.update_layout(showlegend=True)

app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=False, use_reloader=False, port=8090)
