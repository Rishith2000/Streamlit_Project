import streamlit as st
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt
st.subheader('Data Visualization')
if 'data' not in st.session_state:
    st.warning('Upload a CSV file in Upload Data page')
else:

    data=st.session_state['data']
    b=[" "]
    b.extend(data.columns)
    if st.checkbox('histogram'):
            a= st.selectbox('Select a variable',b)
        
            if a!=" ":
                hist = alt.Chart(data).mark_bar().encode(x = a, y = 'count()')
                st.altair_chart(hist)
    if st.checkbox('Bar Chart'):
            
            x=st.selectbox('Select x-axis',b,key=123)
            y=st.selectbox('Select y-axis :',b,key=124)
            hist = alt.Chart(data).mark_bar().encode(x=x,y=y)
            if(x!=" " and y!=" "):
                st.altair_chart(hist)
        
        
        
    if st.checkbox('Line Chart'):
            
            x=st.selectbox('Select x-axis',b,key=1)
            y=st.selectbox('Select y-axis :',b,key=2)
            hist = alt.Chart(data).mark_line().encode(x=x,y=y)
        #st.line_chart(data[a])
            if(x!=" " and y!=" "):
                st.altair_chart(hist)
    if st.checkbox('Area Chart'):
            x=st.selectbox('Select x-axis',b,key=3)
            y=st.selectbox('Select y-axis :',b,key=4)
            hist = alt.Chart(data).mark_area().encode(x=x,y=y)
            if(x!=" " and y!=" "):
                st.altair_chart(hist)
    if st.checkbox('Scatter plot'):
            x=st.selectbox('Select 1st Variable',b)
            y=st.selectbox('Select 2nd Variable :',b)
            hist = alt.Chart(data).mark_circle().encode(x=x,y=y)
        #st.line_chart(data[a])
            if(x!=" " and y!=" "):
                st.altair_chart(hist)
    if st.checkbox('Heat Map'):
            fig, ax = plt.subplots()
            sns.heatmap(data.corr(), ax=ax)
            st.pyplot(fig)


        
