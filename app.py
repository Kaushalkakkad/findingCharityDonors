from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('finding_donors_pred.pkl', 'rb'))


@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    workclass_Federalgov = 0
    workclass_Private = 0
    workclass_Selfempinc = 0
    workclass_Withoutpay = 0
    education_level_10th = 0
    education_level_12th = 0
    education_level_Bachelors = 0
    education_level_Doctorate = 0
    marital_status_Divorced = 0
    marital_status_MarriedAFspouse = 0
    marital_status_Marriedspouseabsent = 0
    marital_status_Nevermarried = 0
    occupation_ArmedForces = 0
    occupation_Execmanagerial = 0
    occupation_Sales = 0
    occupation_Techsupport = 0
    relationship_Husband = 0
    relationship_Wife = 0
    relationship_Unmarried = 0
    sex_Female = 0
    sex_Male = 0
    nativecountry_England = 0
    nativecountry_France = 0
    nativecountry_India = 0
    nativecountry_UnitedStates = 0

    if request.method == 'POST':
        age = int(request.form['age'])
        educationnum = float(request.form['edunum'])
        capitalgain = float(request.form['gain'])
        capitalloss = float(request.form['loss'])
        hoursperweek = int(request.form['hours'])
        workclass = request.form['workclass']
        education_level = request.form['education_level']
        marital_status = request.form['status']
        occupation = request.form['occupation']
        race = 'White'
        sex = request.form['gender']
        nativecountry = request.form['contry']
        if (workclass == 'Federal-gov'):
            workclass_Federalgov = 1
        elif (workclass == 'Private'):
            workclass_Private = 1
        elif (workclass == 'self-emp'):
            workclass_Selfempinc = 1
        else:
            workclass_Withoutpay = 1
        if (education_level == '10th'):
            education_level_10th = 1
        elif (education_level == '12th'):
            education_level_12th = 1
        elif (education_level == 'Bachelors'):
            education_level_Bachelors = 1
        else:
            education_level_Doctorate = 1
        if (marital_status == 'Married_spouse'):
            marital_status_MarriedAFspouse = 1
        elif (marital_status == 'Married'):
            marital_status_Marriedspouseabsent = 1
        else:
            marital_status_Nevermarried = 1
        if (sex == 'Male'):
            sex_Male = 1
        else:
            sex_Female = 1
        if (nativecountry == 'eng'):
            nativecountry_England = 1
        elif (nativecountry == 'US'):
            nativecountry_UnitedStates = 1
        elif (nativecountry == 'india'):
            nativecountry_India = 1
        else:
            nativecountry_France = 1
        prediction = model.predict([[age, educationnum, capitalgain, capitalloss, hoursperweek, workclass_Federalgov,
                                     workclass_Private, workclass_Selfempinc, workclass_Withoutpay,
                                     education_level_10th, education_level_12th, education_level_Bachelors,
                                     education_level_Doctorate, marital_status_Divorced, marital_status_MarriedAFspouse,
                                     marital_status_Marriedspouseabsent, marital_status_Nevermarried,
                                     occupation_ArmedForces, occupation_Execmanagerial, occupation_Sales,
                                     occupation_Techsupport, relationship_Husband, relationship_Wife,
                                     relationship_Unmarried, sex_Female, sex_Male, nativecountry_England,
                                     nativecountry_France, nativecountry_India, nativecountry_UnitedStates]])
        output = round(prediction[0], 2)
        if output == 0:
            return render_template('index.html', prediction_texts="Can not be donor")
        else:
            return render_template('index.html', prediction_text="Can be donor".format(output))
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run()
