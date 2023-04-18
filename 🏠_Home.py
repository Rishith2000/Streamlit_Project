import streamlit as st
import pandas as pd
from PIL import Image
image = Image.open('download.jpg')

st.header('HandBook')
st.image(image)

st.write('This application will help you in visualizing and generating pandas profiling report of data with few clicks without coding and help you in identifying the best model for your dataset.')
st.write('Pandas profiling offers report generation for the dataset with lots of features and customizations for the report generated')


st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.pexels.com/photos/1205301/pexels-photo-1205301.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940
");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)
