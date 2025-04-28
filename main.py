import pandas as pd
import plotly.express as px
import streamlit as st

st.title("testing app")

@st.cache_data
def load_data():
    df = pd.read_csv('clarity.csv')
    return df

df = load_data()

graph = df.groupby(["Name", "day"]).agg({
    "pm_conc": ["mean", "median", "std"],
    "asthma_rate": "first",
    "month_cat": "first",
    "Longitude": "first"
}).reset_index()

graph.columns = ['_'.join(col).strip('_') for col in graph.columns.values]

fig = px.scatter(
    graph,
    x='pm_conc_mean',
    y='pm_conc_std',
    color='day',
    title="PM2.5 Mean vs. Standard Deviation by Day",
    labels={
        'pm_conc_mean': 'Average PM2.5 Concentration',
        'pm_conc_std': 'Standard Deviation of PM2.5 Concentration',
        'day': 'Day of Measurement'
    }
)

st.plotly_chart(fig)