import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css'
]

# Create Dash app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# Expose Flask instance
server = app.server

# Alternative version, using flask server directly (add import flask in imports)
# server = flask.Flask(__name__)
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets, server=server)

# Assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(
    df, 
    x="Fruit", y="Amount", color="City", barmode="group"
)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python. Customized right here!
    '''),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# Only for running on development mode
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8080)