## creating plots

import plotly.express as px
import pandas as pd

def pm25_day_plot(df):

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
        },
        hover_name="Name",
        hover_data={
            "pm_conc_mean": ":.2f",
            "pm_conc_std": ":.2f"
        }
    )
    return fig

def pm25_month_plot(df):
    df['month_cat'] = pd.Categorical(
        df["month"],
        categories=[11, 12, 1, 2, 3],
        ordered=True
    )
    graph = df.groupby(["Name", "month_cat"]).agg({
        "pm_conc": ["mean", "median", "std"],
        "asthma_rate": "first",
    }).reset_index()

    graph.columns = ['_'.join(col).strip('_') for col in graph.columns.values]
    graph = graph.dropna()

    fig = px.scatter(graph, x='pm_conc_mean', y='asthma_rate_first', color='month_cat', size='pm_conc_std')
    return fig

## asthma and PM2.5 mapping
import pandas as pd
import folium
from streamlit_folium import st_folium
import streamlit as st

## READ FILES -- update!
def load_data():
  df_merged = pd.read_csv('data/pm25_asthma_clean.csv')
  return df_merged

# Define functions
def pm25_2025_color(pm25_2025):
    if pm25_2025 < 6:
        return 'green'
    elif 6 <= pm25_2025 < 9:
        return 'orange'
    else:
        return 'red'

def site_type_icon(name):
    name_lower = name.lower()
    if 'school' in name_lower:
        return 'graduation-cap'
    elif 'home' in name_lower:
        return 'home'
    elif 'park' in name_lower or 'playlot' in name_lower:
        return 'leaf'
    elif 'office' in name_lower:
        return 'building'
    else:
        return 'map-marker'

def create_map(df):
    center_lat = df['Latitude'].mean()
    center_lon = df['Longitude'].mean()
    m = folium.Map(location=[center_lat, center_lon], zoom_start=12)

    for _, row in df.iterrows():
        popup_text = (
            f"<b>{row['Name']}</b><br>"
            f"PM2.5 (2024): {row['PM25_2024']:.2f} µg/m³<br>"
            f"PM2.5 (2025): {row['PM25_2025']:.2f} µg/m³<br>"
            f"Census Tract: {row['Census_Tract']}<br>"
            f"Asthma Rate: {row['asthma_rate']} per 1000 (Year: {int(row['year'])})<br>"
            f"Upper CI: {row['Rate Upper Confidence Interval']}"
        )

        color = pm25_2025_color(row['PM25_2025'])
        icon_type = site_type_icon(row['Name'])

        folium.Marker(
            location=(row['Latitude'], row['Longitude']),
            popup=folium.Popup(popup_text, max_width=300),
            icon=folium.Icon(color=color, icon=icon_type, prefix='fa')
        ).add_to(m)

    legend_html = """
    <div style="position: fixed;
         bottom: 50px; left: 50px; width: 280px; height: auto;
         border:2px solid grey; z-index:9999; font-size:16px;
         background-color: white; padding: 15px;">
    <b>Legend</b><br><br>
    <b>PM2.5 (2025) Color:</b><br>
    <span style="color:green; font-size:18px;">■</span> Low (<6 µg/m³)<br>
    <span style="color:orange; font-size:18px;">■</span> Moderate (6–9 µg/m³)<br>
    <span style="color:red; font-size:18px;">■</span> High (>9 µg/m³)<br><br>
    <b>Site Type Icons:</b><br>
    <span style="font-size:18px;">🎓</span> School<br>
    <span style="font-size:18px;">🏠</span> Home<br>
    <span style="font-size:18px;">🌳</span> Park / Playlot<br>
    <span style="font-size:18px;">🏢</span> Office<br>
    <span style="font-size:18px;">📍</span> Other
    </div>
    """
    m.get_root().html.add_child(folium.Element(legend_html))
    return m

