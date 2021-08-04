import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np
# best practice is to use https://flask.palletsprojects.com/en/2.0.x/api/#flask.json.jsonify

import json


from flask import Flask, render_template


app = Flask(__name__)


@app.route('/fetchGraphJsonData')
def create_plot():
    # http://127.0.0.1:5000/fetchGraphJsonData

    N = 40
    x = np.linspace(0, 1, N)
    y = np.random.randn(N)
    df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe


    data = [
        go.Bar(
            x=df['x'], # assign x as the dataframe column 'x'
            y=df['y']
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run()