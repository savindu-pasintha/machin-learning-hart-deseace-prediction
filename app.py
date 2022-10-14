from flask import Flask, request, jsonify, make_response, render_template
import time
import pickle
import pandas as pd
import pandas as pd
import numpy as np

from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.preprocessing import MinMaxScaler

# from flask_restful import Resource, Api;
# from marshmallow import fields;
# from marshmallow_sqlalchemy import ModelSchema;

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index1.html", send_range="0.00")


# create krnw end point
@app.route("/form_to_app_py", methods=["POST"])
def post_request_function():

    age = request.form.get("age")
    sex = request.form.get("sex")
    cp = request.form.get("cp")
    trestbps = request.form.get("trestbps")
    chol = request.form.get("chol")
    fbs = request.form.get("fbs")
    restecg = request.form.get("restecg")
    thalach = request.form.get("thalach")
    exang = request.form.get("exang")
    oldpeak = request.form.get("oldpeak")
    slope = request.form.get("slope")
    ca = request.form.get("ca")
    thal = request.form.get("thal")
    model_range = "Please select data for access rating ..."

    if age:
        if sex:
            if cp:
                if trestbps:
                    if chol:
                        if fbs:
                            if restecg:
                                if thalach:
                                    if exang:
                                        if oldpeak:
                                            if slope:
                                                if ca:
                                                    if thal:
                                                        model_range = str(
                                                            # predictFunction(vote, avg, table, delivery, price)
                                                            predictFunction(
                                                                age,
                                                                sex,
                                                                cp,
                                                                trestbps,
                                                                chol,
                                                                fbs,
                                                                restecg,
                                                                thalach,
                                                                exang,
                                                                oldpeak,
                                                                slope,
                                                                ca,
                                                                thal,
                                                            )
                                                        )
                                                        time.sleep(2)

    return render_template("result.html", send_range=model_range)


def predictFunction(
    age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal
):

    Predictors = [
        "age",
        "sex",
        "cp",
        "trtbps",
        "chol",
        "fbs",
        "restecg",
        "thalachh",
        "exng",
        "oldpeak",
        "slp",
        "caa",
        "thall",
    ]

    new_samples_data = pd.DataFrame(
        data=[
            [
                age,
                sex,
                cp,
                trestbps,
                chol,
                fbs,
                restecg,
                thalach,
                exang,
                oldpeak,
                slope,
                ca,
                thal,
            ]
        ],
        columns=Predictors,
    )

    # TEST DATA
    """new_samples_data = pd.DataFrame(
        data=[[37, 1, 2, 130, 250, 0, 1, 187, 0, 3.5, 0, 0, 2]], columns=Predictors
    )
    """

    model = pickle.load(open("Risk-prediction-prf-model.pkl", "rb"))
    result = model.predict(new_samples_data)

    return result


if __name__ == "__main__":
    app.run(debug=True)
