import streamlit as st
from Application import applicationPage

st.title("Welcome To StackOverFlow Survey Project")
img = Image.open("stackoverflow-logo.png")
st.image(img)
clicked = st.button("Find More..")
if clicked:
    applicationPage()