"""
    This program defines a backend of sorts for the web app to fetch data requests and calculations 
    from.

    The assumption made is that the majority of the calculations will be done regardless of the 
    amount of requests being made, meaning we only have to access data and not calculate ourselves.
"""

from flask import Flask, jsonify
import pandas as pd
import numpy as np

app = Flask(__name__)


@app.route('/data', methods=['GET'])
def get_risk(country_name):
    # load dataframe #
    df = pd.read_csv('risk_eval.csv')

    # convert to JSON #
    arr = np.array(df)
    return jsonify(arr.tolist())


@app.route('/data', methods=['GET'])
def get_grade(country_name):
    # load dataframe #
    df = pd.read_csv('grade_eval.csv')
    grade_dict = df.to_dict()

    # get grade #
    try:
        grade = grade_dict[country_name]
    except:
        return "Invalid Fetch Request :: country name not found"

    # convert to JSON #
    return jsonify({ country_name : grade })


# run as script #
if __name__ == '__main__':
    app.run()