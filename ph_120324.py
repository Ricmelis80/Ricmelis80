import streamlit as st
import pandas as pd
import datetime
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go

# reading the data from excel file
columns_id = ['datetime','pH']
df = pd.read_csv('test120324.txt', names=columns_id,header=None)
st.set_page_config(layout="wide")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)
#image = Image.open('sensor1.jpg')

col1, col2,col3 = st.columns([0.1,0.1,0.5])
#with col1:
#    st.image(image,width=300)

html_title = """
    <style>
    .title-test {
    font-weight:bold;
    padding:5px;
    border-radius:6px;
    }
    </style>
    <center><h1 class="title-test"> PH IoT Sensor </h1></center>"""
with col2:
    st.markdown(html_title, unsafe_allow_html=True)
    
df["Time_Course"] = df["datetime"]
result = df.groupby(by = df["Time_Course"])["pH"].sum().reset_index()

with col3:
    fig1 = px.line(result, x = "Time_Course", y = "pH", title="pH Change Over Time in examined sample IDXX..",
                   template="gridon")
    st.plotly_chart(fig1,use_container_width=True)

st.divider()
        
view1, dwn1= st.columns([0.20,0.20])
with view1:
    expander = st.expander("pH")
    data = result
    expander.write(data)
with dwn1:
    st.download_button("Get Data", data = result.to_csv().encode("utf-8"),
                       file_name="test120324.csv", mime="text/csv")
st.divider()
