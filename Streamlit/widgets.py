import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit Text Input")

name=st.text_input("Enter Your Name:")

if name:
    st.write(f"Hello,{name}. How is your AI Journey")


#Slider
age=st.slider("Select your age:",0,100,22)
st.write(f"Your age is:{age}")

#Select Box
Options=["Python","Java","C","C++"]
choice=st.selectbox("Choose your favorite language:",Options)
st.write("Your selected language is:",choice)
df=pd.DataFrame({
    'Name':["Zahid","Tayab","Arosh"],
    'Age':[22,21,19],
    'City':["Banglore","Hydrabad","Mumbai"]
})
df.to_csv("Sample.csv")
st.write(df)


#Uploded file
uploded_file=st.file_uploader("Choose a CSV file",type="csv")
if uploded_file is not None:
    df=pd.read_csv(uploded_file)
    st.write(df)
