import streamlit as st
import pandas as pd
import numpy as np

#Title of the Application
st.title("Hello Zahid!")

#Display Simple text
st.write("This is a Simple text")

#Create a DataFrame
df=pd.DataFrame({
    'Name':["Zahid","Tayab","Arosh"],
    'Age':[22,21,19]
})

#Display the DataFrame
st.write("This is the DataFrame")
st.write(df)


#Create LineChart
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=["A","B","C"]
)
st.line_chart(chart_data)

