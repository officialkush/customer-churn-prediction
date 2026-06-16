from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np
app=Flask(__name__)

model=pickle.load(open('saved.sav','rb'))
ct=pickle.load(open('encoder.sav','rb'))

@app.route("/")
def home():
    return render_template ('index.html')

@app.route("/predict",methods=["POST"])
def predict():
    CustomerID = int(request.form["CustomerID"])
    Age = int(request.form["Age"])
    Gender = request.form["Gender"]
    Tenure = int(request.form["Tenure"])
    UsageFrequency = int(request.form["UsageFrequency"])
    SupportCalls = int(request.form["SupportCalls"])
    PaymentDelay = int(request.form["PaymentDelay"])
    SubscriptionType = request.form["SubscriptionType"]
    ContractLength = request.form["ContractLength"]
    TotalSpend = float(request.form["TotalSpend"])
    LastInteraction = int(request.form["LastInteraction"])

    input_data=[[
        CustomerID,
        Age,
        Gender,
        Tenure,
        UsageFrequency,
        SupportCalls,
        PaymentDelay,
        SubscriptionType,
        ContractLength,
        TotalSpend,
        LastInteraction


    ]]

    final_input=ct.transform(input_data)
    predict=model.predict(final_input)[0]
    result = "Churn" if predict == 1 else "Will stay"


    return render_template(
        "index.html",
        prediction_text=result
       
   )
if __name__=="__main__":
    app.run(debug=True)