import streamlit as st
import pandas as pd
from PIL import Image
image = Image.open('download.jpg')

st.header('HandBook')
st.image(image)

st.write('This application will help you in visualizing and generating pandas profiling profile of data with few clicks without coading and help you in identifying the best model for your dataset.')



