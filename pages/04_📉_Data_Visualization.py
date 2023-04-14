import streamlit as st
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt


def histogram(data):
    b = [" "]
    b.extend(data.columns)
    a = st.selectbox('Select a variable', b)
    if a != " ":
        hist = alt.Chart(data).mark_bar().encode(x=a, y='count()')
        st.altair_chart(hist)


def bar_chart(data):
    b = [" "]
    b.extend(data.columns)
    x = st.selectbox('Select x-axis', b, key=123)
    y = st.selectbox('Select y-axis :', b, key=124)
    if x != " " and y != " ":
        hist = alt.Chart(data).mark_bar().encode(x=x, y=y)
        st.altair_chart(hist)


def line_chart(data):
    b = [" "]
    b.extend(data.columns)
    x = st.selectbox('Select x-axis', b, key=1)
    y = st.selectbox('Select y-axis :', b, key=2)
    if x != " " and y != " ":
        hist = alt.Chart(data).mark_line().encode(x=x, y=y)
        st.altair_chart(hist)


def area_chart(data):
    b = [" "]
    b.extend(data.columns)
    x = st.selectbox('Select x-axis', b, key=3)
    y = st.selectbox('Select y-axis :', b, key=4)
    if x != " " and y != " ":
        hist = alt.Chart(data).mark_area().encode(x=x, y=y)
        st.altair_chart(hist)


def scatter_plot(data):
    b = [" "]
    b.extend(data.columns)
    x = st.selectbox('Select 1st Variable', b)
    y = st.selectbox('Select 2nd Variable :', b)
    if x != " " and y != " ":
        hist = alt.Chart(data).mark_circle().encode(x=x, y=y)
        st.altair_chart(hist)


def heatmap(data):
    fig, ax = plt.subplots()
    sns.heatmap(data.corr(), ax=ax)
    st.pyplot(fig)


st.subheader('Data Visualization')

if 'data' not in st.session_state:
    st.warning('Upload a CSV file in Upload Data page')
else:
    data = st.session_state['data']
    chart_type = st.selectbox('Select chart type', ['Histogram', 'Bar Chart', 'Line Chart', 'Area Chart', 'Scatter Plot', 'Heatmap'])

    if chart_type == 'Histogram':
        histogram(data)
    elif chart_type == 'Bar Chart':
        bar_chart(data)
    elif chart_type == 'Line Chart':
       


        
