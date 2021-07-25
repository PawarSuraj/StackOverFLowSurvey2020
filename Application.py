import streamlit as st
from PIL import Image
from salaryPrediction import displaySalaryPrediction
from explorePage import displayExplorePage

st.title("StackOverFlow Survey Project")
img = Image.open("stackoverflow-logo.png")
st.image(img)
st.text("\n\n\n\n\n\n\n")
st.sidebar.write("*StackOverFlow is a community where coding professionals asks their quries and share their solutions as well.*:sunglasses:")
st.sidebar.write("Explore Your Options :mag:")
page = st.sidebar.selectbox("",("Home","Predict","Explore"))
if page == "Predict":
    displaySalaryPrediction()
if page == "Explore":
    displayExplorePage()