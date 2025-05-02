import pandas as pd
import streamlit as st
from plots import pm25_day_plot, pm25_month_plot, create_map
from streamlit_folium import st_folium

st.set_page_config(page_title="Air Quality Dashboard", layout="wide")

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

# Load your datasets
df = load_data('data/clarity.csv')
df_merged = load_data('data/clarity_asthma_merged.csv')

# Build plots
fig_month = pm25_month_plot(df)

# Optional: organize with tabs
tab1, tab2 = st.tabs(["Air Quality Plots", "PM2.5 Map"])

with tab1:
    st.title("Air Quality Plots")
    # Optionally include the day plot too:
    # fig_day = pm25_day_plot(df)
    # st.plotly_chart(fig_day)
    st.plotly_chart(fig_month)

with tab2:
    st.title("PM2.5 and Asthma Rate Map (2025 Focus)")
    folium_map = create_map(df_merged)
    st_folium(folium_map, width=800, height=600)
