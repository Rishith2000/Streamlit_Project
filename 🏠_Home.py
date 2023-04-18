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
        background-image: url("https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.freecodecamp.org%2Fnews%2Fcontent%2Fimages%2F2022%2F09%2Fjonatan-pie-3l3RwQdHRHg-unsplash.jpg&tbnid=dfIZQWgO5XfgyM&vet=12ahUKEwj6kdW8zbT-AhULn4kEHeVgAGkQMygfegUIARC9Ag..i&imgrefurl=https%3A%2F%2Fwww.freecodecamp.org%2Fnews%2Fhtml-background-image-how-to-add-wallpaper-images-to-your-website%2F&docid=MdcI3Z9gtYMS6M&w=1920&h=1282&q=jpg%20background&ved=2ahUKEwj6kdW8zbT-AhULn4kEHeVgAGkQMygfegUIARC9Ag");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)
