import pandas as pd
import streamlit as st
from plots.plots_main import create_folium_map, pm25_avg, trends_all
from streamlit_folium import st_folium
from utils import t, select_lang


st.set_page_config(page_title="Air Quality Dashboard", layout="wide")

select_lang()

# lang_toggle()
# translations = {
#     "tab1_title": {
#         "en": "PM2.5 Monitors Map",
#         "es": "Mapa de monitores de PM2.5"
#     },
#     "tab2_title": {
#         "en": "Air Quality Trends",
#         "es": "Tendencias de la calidad del aire"
#     },
#     "tab1_header": {
#         "en": "PM2.5 Monitors & Asthma Prevalence Map",
#         "es": "Mapa de los monitores de PM2.5 y la prevalencia de asma"
#     }
# }


@st.cache_data(ttl=0)
def load_data(url):
    df = pd.read_csv(url)
    return df

# load datasets
df = load_data('data/clarity.csv')
df_merged = load_data('data/clarity_asthma_merged.csv')
df_og = load_data('data/risesouthcity_april_daily.csv')
tracts_path = 'data/sf_sanbruno_census_tracts.geojson'

# build diff tabs
tab1, tab2 = st.tabs([t("PM2.5 Monitors & Asthma Prevalence Map"), t("Air Quality Trends")])

with tab1:
    st.title(t("PM2.5 Monitors & Asthma Prevalence Map"))

    st.markdown(t("### Welcome to Rise South City's air pollution dashboard."))
    st.markdown(t(
    "This interactive map shows average **PM2.5 air quality readings** from monitors across San Bruno and South San Francisco in 2024 (Oct-Dec) and 2025 (Jan-Mar), overlaid with asthma prevalence rates at the census tract level. "
    "\n\nUse the layer toggles to view different types of monitoring sites (schools, homes, parks, offices) and explore how air pollution intersects with asthma rates in different census tracts. "
    "\n\nThe **colored markers** represent PM2.5 pollution levels for 2025: green (low), orange (moderate), and red (high). Census tract outlines and asthma prevalence choropleths provide additional insight into how air quality may affect local residents’ health. "
    "\n\nYou can also search for specific census tracts using their GEOID to quickly navigate the map. To translate your address into a census tract GEOID, you can use the US Census Bureau's Geocoder website: https://geocoding.geo.census.gov/geocoder/"
    "\n\n**Note:** Data source descriptions and methodology details are available on a separate page. Please review the datasets to understand how the data was collected, key assumptions, and limitations."
    ))

    folium_map = create_folium_map(df_merged)
    st_folium(folium_map, use_container_width=True, height=650)
    st.caption(t("Sources: Rise South City Clarity Monitors (2024-2025), San Mateo County Health Asthma Reporting (2022)"))




with tab2:

    st.title(t("Air Quality Over Time"))


    averages = pm25_avg(df_og)
    st.plotly_chart(averages)
    st.caption(t("Source: Rise South City Clarity Monitors (2024-2025)"))


    figgy = trends_all(df_og)
    st.plotly_chart(figgy)
    st.caption(t("Source: Rise South City Clarity Monitors (2024-2025)"))



