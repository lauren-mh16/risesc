import pandas as pd
import streamlit as st
from plots.plots_main import trends_placeholder, create_map
from streamlit_folium import st_folium

st.set_page_config(page_title="Air Quality Dashboard", layout="wide")

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

# Load your datasets
df = load_data('data/clarity.csv')
df_merged = load_data('data/clarity_asthma_merged.csv')


# Optional: organize with columns
col1, col2 = st.columns(2)

with col2:
    st.title("Air Quality through Time")
    fig = trends_placeholder(df)
    # Optionally include the day plot too:
    # fig_day = pm25_day_plot(df)
    # st.plotly_chart(fig_day)
    st.plotly_chart(fig)

with col1:
    st.title("PM2.5 Monitors Map")
    folium_map = create_map(df_merged)
    st_folium(folium_map, width=800, height=600)
