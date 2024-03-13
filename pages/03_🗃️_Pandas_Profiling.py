import streamlit as st
from streamlit_pandas_profiling import st_profile_report
from ydata_profiling import ProfileReport

st.subheader('Pandas Profiling')
if 'data' not in st.session_state:
    st.warning('Upload a CSV file in Upload Data page')
else:
    data=st.session_state['data']
    def report(data):
        
        pr = ProfileReport(data, explorative=True)
        return pr

    pr=report(data)
#pr.to_file('Analysis.html')

    st_profile_report(pr)
