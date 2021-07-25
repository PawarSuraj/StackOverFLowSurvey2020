import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def selectCountry(countries, mincount):
    countryMap = {}
    for i in range(len(countries)):
        if countries.values[i] >= mincount:
            countryMap[countries.index[i]] = countries.index[i]
        else:
            countryMap[countries.index[i]] = 'others'
    return countryMap

def selectCodingYears(value):
    if value == 'More than 50 years':
        return 50
    if value == 'Less than 1 year':
        return 0.5
    return float(value)

def selectEducation(degree):
    if degree == 'Bachelor’s degree (B.A., B.S., B.Eng., etc.)':
        return 'Bachelor’s Degress'
    if degree == 'Master’s degree (M.A., M.S., M.Eng., MBA, etc.)':
        return 'Master’s Degree'
    if degree == 'Professional degree (JD, MD, etc.)' or degree == 'Other doctoral degree (Ph.D., Ed.D., etc.)':
        return 'Post Graduation'
    return 'Less than a Bachelors'

@st.cache
def readData():
    df = pd.read_csv('survey_results_public.csv')
    df = df[["Country","EdLevel","YearsCodePro","Employment","ConvertedComp"]]
    df = df.rename({"ConvertedComp":"Salary"}, axis=1)
    df = df[df['Salary'].notnull()]
    df = df.dropna()
    df.isnull().sum()
    df = df[df["Employment"] == "Employed full-time"]
    df = df.drop("Employment", axis=1)
    countryMap = selectCountry(df.Country.value_counts(),800)
    df['Country'] = df['Country'].map(countryMap)
    df = df[df['Salary'] <= 250000]
    df = df[df['Salary'] >= 10000]
    df = df[df['Country'] != 'Other']
    df['YearsCodePro'] = df['YearsCodePro'].apply(selectCodingYears)
    df['EdLevel'] = df['EdLevel'].apply(selectEducation)
    return df

df = readData()

def displayExplorePage():
    data = df["Country"].value_counts()
    fig1, ax1 = plt.subplots()
    explode = [0,0.2,0,0,0,0,0,0]
    ax1.pie(data, labels = data.index,explode = explode, autopct="%1.0f%%", shadow=False, startangle=90)
    fig1.set_facecolor('#F9E9D7')
    ax1.axis("equal")
    st.text("\n\n\n")
    st.write('''#### Participation From Each Country :two_men_holding_hands::couple::two_women_holding_hands::two_men_holding_hands:''')
    st.pyplot(fig1)

    st.write('''#### Average Developer Salary In Each Country :money_with_wings: ''')
    st.text("\n\n\n")
    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)
    
    st.write('''#### Average Developer Salary Based On Experience :office: ''')
    st.text("\n\n\n")
    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)