import streamlit as st
import pandas as pd
from plots import pm25_day_plot

st.title("PM2.5 Scatter by Day testing")

@st.cache_data
def load_data():
    return pd.read_csv('data/clarity.csv')

df = load_data()

fig = pm25_day_plot(df)
st.plotly_chart(fig)