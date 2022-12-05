import streamlit as st
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport
data=st.session_state['data']
st.subheader('Pandas Profiling')

def report(data):
        
    pr = ProfileReport(data, explorative=True)
    return pr

pr=report(data)
#pr.to_file('Analysis.html')

st_profile_report(pr)
