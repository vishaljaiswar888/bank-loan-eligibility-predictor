from flask import Flask,render_template
import os
from flask import request
import numpy as np
import pickle


app = Flask(__name__)

model1 = pickle.load(open('modelNB.pkl','rb'))
model3 = pickle.load(open('modelLR.pkl','rb'))


@app.route("/", methods=["GET", "POST"])
def home():
    #Gender	Married	Dependents	Education	Self_Employed	
    # ApplicantIncome	CoapplicantIncome	LoanAmount	Loan_Amount_Term	Credit_History	Property_Area
    if request.method == "POST":

        if request.form.get('genderid')=='Male':
            Gender = 1
        else:
            Gender = 0

        if request.form.get('marriedid')=='Yes':
            Married = 1
        else:
            Married = 0

        Dependents = request.form.get("dependentsid")

        if request.form.get('eduid')=='Graduate':
            Education = 1
        else:
            Education = 0

        if request.form.get('seid')=='Yes':
            Self_Employed = 1
        else:
            Self_Employed = 0

        ApplicantIncome = request.form.get("aiid")

        CoapplicantIncome =  request.form.get("caiid")

        LoanAmount =  request.form.get("laid")

        Loan_Amount_Term = request.form.get("latid")

        if request.form.get('chid')==1:
            Credit_History = 1
        else:
            Credit_History = 0

        
        if request.form.get('paid') == 'Rural':
            Property_Area = 0
        elif request.form.get('paid') == 'Semiurban':
            Property_Area = 1
        else:
            Property_Area = 2

        val = np.array([Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area], dtype='float32')

        y_pred = model1.predict(val.reshape(1, -1))
        print(y_pred)

        if (y_pred[0]==1):
            return render_template("prediction.html", loan_status={"loan":y_pred[0]})
        else:
            return render_template("prediction.html", loan_status={"loan":y_pred[0]})

    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)