import streamlit as st
import pandas as pd
import numpy as np

#Title of the website
st.title("Hello Khan")

#Display text
st.write("This is my ML Application")

#create a DataFrame
df=pd.DataFrame({
    'First Column':[1,2,3,4,5,],
    'Second Column':[10,20,30,40,50]
})
st.write(df)

#Create Line Chart
Chart_Data=pd.DataFrame(
    np.random.randn(20,3),columns=['A','B','C']
)
st.line_chart(Chart_Data)


#Widgets
name=st.text_input("Enter your name:")
if name:
    st.write(f"Hello,{name}")

age=st.slider("Select your age:",0,100,25)
st.write(f"Your age is:{age}")

options=["Python","Java","C++","JS"]
choice=st.selectbox