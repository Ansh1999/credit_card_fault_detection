from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from src.pipeline import predict_pipeline


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/predict_datapoint",methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        render_template('index.html')
    else:
        obj = predict_pipeline.CustomData(
            request.form.get('LIMIT_BAL'),request.form.get('SEX'),
            request.form.get('EDUCATION'),request.form.get('MARRIAGE'),
            request.form.get('AGE'),request.form.get('PAY_1'),
            request.form.get('PAY_2'),request.form.get('PAY_3'),
            request.form.get('PAY_4'),request.form.get('PAY_5'),
            request.form.get('PAY_6'),request.form.get('BILL_AMT1'),
            request.form.get('BILL_AMT2'),request.form.get('BILL_AMT3'),
            request.form.get('BILL_AMT4'),request.form.get('BILL_AMT5'),
            request.form.get('BILL_AMT6'),request.form.get('PAY_AMT1'),
            request.form.get('PAY_AMT2'),request.form.get('PAY_AMT3'),
            request.form.get('PAY_AMT4'),request.form.get('PAY_AMT5'),
            request.form.get('PAY_AMT6')

        )

        data_frame = obj.get_as_dataframe()
        print(data_frame)

        pred = predict_pipeline.PredictPipeline()
        predicted = pred.predict(data_frame)
        print(predicted)

        return render_template('result.html',results=predicted)


app.run(debug=True,host='0.0.0.0',port=8080)