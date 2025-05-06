import pandas as pd
import streamlit as st
from plots.plots_main import trends_placeholder, create_folium_map
from streamlit_folium import st_folium

st.set_page_config(page_title="Air Quality Dashboard", layout="wide")

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

# Load your datasets
df = load_data('data/clarity.csv')
df_merged = load_data('data/clarity_asthma_merged.csv')
tracts_path = 'data/sf_sanbruno_census_tracts.geojson'

# Build plots
trends = trends_placeholder(df)

# Optional: organize with tabs
tab1, tab2 = st.tabs(["Map", "Trends"])

with tab2:
    st.title("Air Quality Through Time")
    st.plotly_chart(trends)

with tab1:
    st.title("PM2.5 Monitors Map")
    folium_map = create_folium_map(df_merged)
    st_folium(folium_map, use_container_width=True, height=650)
    
    legend_html = """
    <div style="border:1px solid grey; padding:10px; background-color: white; font-size:14px;">
    <b>Legend</b><br><br>
    <b>PM2.5 (2025) Color:</b><br>
    <span style="color:green; font-size:16px;">■</span> Low (&lt;6 µg/m³)<br>
    <span style="color:orange; font-size:16px;">■</span> Moderate (6–9 µg/m³)<br>
    <span style="color:red; font-size:16px;">■</span> High (&gt;9 µg/m³)<br><br>
    <b>Site Type Icons:</b><br>
    🎓 School<br>
    🏠 Home<br>
    🍃 Park / Playlot<br>
    🏢 Office<br>
    📍 Other
    </div>
    """
    st.markdown(legend_html, unsafe_allow_html=True)

    
