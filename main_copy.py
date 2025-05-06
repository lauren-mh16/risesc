import pandas as pd
import streamlit as st
from plots.plots_main import trends_placeholder, create_folium_map
from streamlit_folium import st_folium

st.set_page_config(page_title="Air Quality Dashboard", layout="wide")

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

# load datasets
df = load_data('data/clarity.csv')
df_merged = load_data('data/clarity_asthma_merged.csv')
tracts_path = 'data/sf_sanbruno_census_tracts.geojson'

# build diff tabs
tab1, tab2 = st.tabs(["PM2.5 Monitors Map", "Air Quality Trends"])

with tab1:
    st.title("PM2.5 Monitors Map")

    st.markdown("### Welcome to Rise South City's air pollution dashboard.")
    st.markdown(
    "This interactive map shows average **PM2.5 air quality readings** from monitors across San Bruno and South San Francisco in 2024 and 2025, overlaid with asthma prevalence rates at the census tract level. "
    "Use the layer toggles to view different types of monitoring sites (schools, homes, parks, offices) and explore how air pollution intersects with asthma rates in different census tracts. "
    "The **colored markers** represent PM2.5 pollution levels for 2025: green (low), orange (moderate), and red (high). Census tract outlines and asthma prevalence choropleths provide additional insight into how air quality may affect local residents’ health. "
    "You can also search for specific census tracts using their GEOID to quickly navigate the map."
    "\n\n**Note:** Data source descriptions and methodology details are available on a separate page. Please review the datasets to understand how the data was collected, key assumptions, and limitations."
)


    folium_map = create_folium_map(df_merged)
    st_folium(folium_map, use_container_width=True, height=650)


with tab2:
    trends = trends_placeholder(df)
    st.title("Air Quality Through Time")
    st.plotly_chart(trends)


