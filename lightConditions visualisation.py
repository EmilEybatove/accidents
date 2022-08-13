import pandas as pd
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

df = pd.read_csv("6 Аварии/transformation.csv")

pxFig = px.scatter_mapbox(df, lat="coordW", lon="coordL", title="Освещение", color="isLight", zoom=8, height=800,
                                  mapbox_style="open-street-map")

fig = go.Figure(pxFig)

fig.update_layout(height=800)
fig.update_layout(showlegend=True)

app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=False, use_reloader=False, port=8099)
