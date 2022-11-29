import streamlit as st
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport
data=st.session_state['data']
st.cache()
def report(data):
        
    pr = ProfileReport(data, explorative=True)
    return pr
st_profile_report(report(data))
