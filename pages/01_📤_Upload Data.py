import streamlit as st
import pandas as pd 


st.subheader('Upload Data')
st.write('Hi, Here you can upload your ***CSV file* **')
st.write('By default This app contains iris dataset')
st.write("[Click here](https://www.kaggle.com/datasets/uciml/iris) to know more about iris dataset")



uploaded_file = st.file_uploader('Choose a file')
if uploaded_file  is not None:
    
    df=pd.read_csv(uploaded_file)
    st.success('The Dataset Uploaded successfully')
else:
    df=pd.read_csv('iris.csv')




st.session_state['data']=df
