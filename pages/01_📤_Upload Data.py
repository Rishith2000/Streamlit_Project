import streamlit as st
import pandas as pd 


st.subheader('Upload Data')

st.write('Here you can upload your **CSV file**')

st.write("[Click here](https://github.com/UR26/CSV) for sample **CSV** files")



uploaded_file = st.file_uploader('Choose a file')
if uploaded_file  is not None:
    
    df=pd.read_csv(uploaded_file)
    st.success('The Dataset Uploaded successfully')
    st.session_state['data']=df
#else:
#    df=pd.read_csv('iris.csv')





