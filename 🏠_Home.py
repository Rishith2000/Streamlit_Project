import streamlit as st
import pandas as pd
from PIL import Image
image = Image.open('download.jpg')

st.header('HandBook')
st.image(image)

st.write('This application will help you in visualizing and generating pandas profiling report of data with few clicks without coding and help you in identifying the best model for your dataset.')
st.write('Pandas profiling offers report generation for the dataset with lots of features and customizations for the report generated')

page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown('<style>body{background-color: #E5E5E5;}</style>',unsafe_allow_html=True)
