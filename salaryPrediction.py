import streamlit as st
import pickle
import numpy as np

countries = ['India','United States','United Kingdom','Germany','Canada',
'Brazil','France','Spain','Australia','Netherlands','Poland','Italy','Russian Federation',
'Sweden','Turkey','Israel','Pakistan','Switzerland','Mexico','Ireland','Norway',
'Ukraine','Romania','South Africa','Czech Republic','Austria','Belgium','Iran','Portugal','Denmark','others']

education = ['Less than a Bachelors','Bachelor’s Degress', 'Master’s Degree',
       'Post Graduation']

def importModel():
    with open('DecisionTreeRegressor.pkl', 'rb') as modelFile:
        model = pickle.load(modelFile)
    return model

model = importModel()
regressorModel = model["model"]
countryEncoder = model["countryEncoder"]
educationEncoder = model["educationEncoder"]

def displaySalaryPrediction():
    st.title("Salary Predictor")
    st.write('''### Data is required for salary prediction''')
    st.text("\n\n\n\n")
    st.write('Select Country:earth_asia:')
    country = st.selectbox("",countries)
    st.text("\n\n\n\n\n\n\n\n\n")
    st.write('Education Level:scroll:')
    educationLevel = st.selectbox("",education)
    st.text("\n\n\n\n\n\n\n\n\n")
    st.write("Years of Coding:computer:")
    experience = st.slider("",0, 50, 1)
    SalButton = st.button("Predict My Salary")

    if SalButton :
        st.balloons()
        inputArry = np.array([[country, educationLevel, experience]])
        inputArry[:,0] = countryEncoder.transform(inputArry[:,0])
        inputArry[:,1] = educationEncoder.transform(inputArry[:,1])
        inputArry = inputArry.astype(float)

        salary = regressorModel.predict(inputArry)
        st.subheader(f"Your approximate Salary is : ${salary[0]:.2f}")