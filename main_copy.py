import pandas as pd
import streamlit as st
from plots.plots_main import trends_placeholder, create_map
from streamlit_folium import st_folium

st.set_page_config(page_title="Air Quality Dashboard", layout="wide")

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

# load datasets
df = load_data('data/clarity.csv')
df_merged = load_data('data/clarity_asthma_merged.csv')

# build diff tabs
tab1, tab2 = st.tabs(["Map", "Trends"])

with tab1:
    st.title("PM2.5 Monitors Map")
    st.markdown("### Hello testing an intro- Welcome to Rise Souty City's air pollution dashboard. "
                "[something about how air pollution is important to monitor?")
    st.markdown("---")

    folium_map = create_map(df_merged)
    st_folium(folium_map, width=800, height=600)


with tab2:
    trends = trends_placeholder(df)
    st.title("Air Quality Through Time")
    st.plotly_chart(trends)

