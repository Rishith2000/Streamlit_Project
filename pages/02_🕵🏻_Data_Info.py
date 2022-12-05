import streamlit as st
import altair as alt

st.subheader('Data Info')

data=st.session_state['data']
@st.cache
def head(data):
    return data.head() 
@st.cache
def Tail(data):
    return data.tail()
if(st.checkbox('Show Shape')):
    st.write(f"Dataset contains {data.shape[0]} rows and {data.shape[1]} columns")
if(st.checkbox('Show Summary of Dataset')):
    st.write(data.describe())
if(st.checkbox("Show Data")):
    r=st.radio('Select your option',['Head','Tail','All'])
    if(r=='Head'):
        st.dataframe(head(data))
    elif(r=='Tail'):
        st.dataframe(Tail(data))
    else:
       st.dataframe(data)
if(st.checkbox("Show Columns")):
    st.write(data.columns)


