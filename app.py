import flask
from flask import Flask,render_template,request
import numpy as np
import pandas as pd
import pickle
import sklearn
from sklearn.linear_model import LinearRegression

with open("SLR_MODEL.pkl","rb") as f:
    m = pickle.load(f)

app = Flask(__name__)


@app.route('/')
def initial_fun():
    return render_template("index.html")

@app.route("/predict",methods = ['GET','POST'])
def fun3():
    a = [float(i) for i in request.form.values()] # 17
    b = [np.array(a)] # [[17]]
    sol = m.predict(b)[0]  # a = [12] -> a[0] -> 12
    return render_template("index.html" , prediction_text = sol)


if __name__ == "__main__":
    app.run(debug=True)

