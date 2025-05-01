import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="Asthma vs Demographics", layout="wide")
st.title("hello")

def load_data():
    return pd.read_csv('data/demo.csv')

df = load_data()

demographic_vars = ['Smoking Prevalence', 'Obesity Prevalence', 'COPD Prevalence', 'Lack of Health Care Access Prevalence',
                    'Percent Population Within Half a Mile to Parks', 'Population Below Poverty Level', 'Housing Stress']
selected_var = st.selectbox(
    "Choose a variable to visualize",
    options=demographic_vars
)

df_graph = df.groupby(["Name"]).agg({
    "pm_conc": "mean",
    "asthma_rate": "first",
    selected_var: "first"

}).reset_index()


fig = px.scatter(
    df_graph, x = selected_var, y = 'asthma_rate', size = 'pm_conc'
)
fig.update_traces(marker=dict(size=20, opacity=0.6))

st.plotly_chart(fig)
