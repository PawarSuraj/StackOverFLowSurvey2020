import streamlit as st
import pandas as pd

st.title('Streamlit Appication')

st.header('Streamlit Header')

st.subheader('Streamlit SubHeader')

st.success("Streamlit Success")

st.info("Streamlit Information!")

st.warning("Streamlit Warning!")

st.error("Streamlit error!!")

st.exception("Streamlit Exception")

# prints the documentation for reference
# st.help(pd.DataFrame)

st.write("Streamlit Write")

st.write([i for i in range(10)])

# Working with image

# from PIL import Image

# img = Image.open("C:\\Users\matri\\Downloads\\wallhaven-lmle8q_3840x2160.png")
# st.image(img,width=500,caption="Streamlit Image")

# Working with Videos

# vidFile = open("C:\\Users\\matri\\Videos\\Call of Duty  Modern Warfare 2 Remastered\\Call of Duty  Modern Warfare 2 Remastered 2020.11.26 - 13.16.05.02.mp4","rb")
# st.video(vidFile)

# working with audio

# audioFile = open('E:\\Music\\EnGlIsH\\La Vie En Rose.mp3','rb')
# st.audio(audioFile, format="audio/mp3")


# Widgets


# CheckBox
if st.checkbox("show/Hide"):
    st.text("showing or Hiding")


# Radio Button
status = st.radio("Streamlit Radio Button",("Active","Inactive"))
if status == "Active":
    st.text("Active")
else:
    st.text("InActive")


# select Box
occupation = st.selectbox("Your Selection",("None","Selection 1","Selection 2","Selection 3"))
st.text(f"Your Selected this : {occupation}")


# Multi Select
location = st.multiselect("Residance Location",("Location 1","Location 2","Location 3","Location 4","Location 5"))
st.text(f"You selected {location} & type = {type(location)}")


# slider
rating = st.slider("Rate Streamlit : ",0,10,1)
st.write(f"you rated Streamlit with {rating}/10")


# Button
def show():
    st.write("you just clicked me")
if st.button("Streamlit Button"):
    show()


# Text Input
name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.success(f"hii {name}")


# Text Area
address = st.text_area("Enter your address:")
if st.button("save"):
    st.success(f"{address}")


# Date Input
import datetime
today = st.date_input("today is ",datetime.datetime.now())


# time
the_time = st.time_input("the time is :",datetime.time())


# Display JSON
st.write("Displaying JSON")
st.json({'name':"Suraj",'gender':"male"})


# Display Raw Code
st.text({"Display Code"})
st.code("import numpy as np")

# Display Raw Code
with st.echo():
    # Streamlit visible portion
    import pandas as pd
    df = pd.DataFrame()
    df


# Progress Bar
import time
bar = st.progress(0)
for p in range(10):
    bar.progress(p+1)


# Spinner
with st.spinner("waiting..."):
    time.sleep(5)
st.success("Finished!!!!")

# Ballons
# st.balloons()


# sidebars
st.sidebar.header("Streamlit About Section")
st.sidebar.button("StreamLit Button")


# Functions 
@st.cache
def run_multiple():
    return range(100)

st.write(run_multiple())

# Plots
st.pyplot()

# DataFrame
st.DataFrame(df)

# Tables
st.table(df)