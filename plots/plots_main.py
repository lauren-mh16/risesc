import plotly.express as px
import pandas as pd
import folium
import plotly.express as px
from folium.plugins import Search

def trends_placeholder(df):
    fig = px.scatter(df, x = "datetime", y = "pm_conc", color = "Name")
    return fig


# Helper: Color function for PM2.5
def pm25_2025_color(pm25_2025):
    if pm25_2025 < 6:
        return 'green'
    elif 6 <= pm25_2025 < 9:
        return 'orange'
    else:
        return 'red'

# Helper: Icon type based on site name
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
def site_type_emoji(name):
    name_lower = name.lower()
    if 'school' in name_lower:
        return '&#127891;'   # 🎓
    elif 'home' in name_lower:
        return '&#127968;'   # 🏠
    elif 'park' in name_lower or 'playlot' in name_lower:
        return '&#127807;'   # 🍃
    elif 'office' in name_lower:
        return '&#127970;'   # 🏢
    else:
        return '&#128205;'   # 📍

def create_folium_map(df_merged, tracts_path):
    center_lat = df_merged['Latitude'].mean()
    center_lon = df_merged['Longitude'].mean()
    m = folium.Map(location=[center_lat, center_lon], zoom_start=12)

    # Choropleth
    folium.Choropleth(
        geo_data=tracts_path,
        name='Asthma Prevalence Choropleth',
        data=df_merged,
        columns=['Census_Tract', 'asthma_rate'],
        key_on='feature.properties.GEOID',
        fill_color='YlOrRd',
        fill_opacity=0.5,
        line_opacity=0.7,
        nan_fill_color='white',
        legend_name='Asthma Prevalence (%) (Adults 18+)',
        highlight=True,
    ).add_to(m)

    # GeoJson (tract outlines)
    tracts_geojson = folium.GeoJson(
        tracts_path,
        name='Census Tracts (Outline)',
        style_function=lambda feature: {
            'fillColor': 'transparent',
            'color': 'blue',
            'weight': 1.5,
            'dashArray': '5, 5'
        },
        tooltip=folium.GeoJsonTooltip(fields=['GEOID'], aliases=['Census Tract:'])
    ).add_to(m)

    # FeatureGroups
    fg_schools = folium.FeatureGroup(name='Schools').add_to(m)
    fg_homes = folium.FeatureGroup(name='Homes').add_to(m)
    fg_parks = folium.FeatureGroup(name='Parks / Playlots').add_to(m)
    fg_offices = folium.FeatureGroup(name='Offices').add_to(m)
    fg_other = folium.FeatureGroup(name='Other').add_to(m)

    # Add markers
    for _, row in df_merged.iterrows():
        site_emoji = site_type_emoji(row['Name'])
        epa_note = ""
        if row['PM25_2025'] >= 12:
            epa_note = "<br><b style='color:red;'>⚠️ Above EPA annual limit (12 µg/m³)</b>"

        popup_text = (
            f"<b>{site_emoji} {row['Name']}</b><br>"
            f"PM2.5 (2024): {row['PM25_2024']:.2f} µg/m³<br>"
            f"PM2.5 (2025): {row['PM25_2025']:.2f} µg/m³{epa_note}<br>"
            f"Census Tract: {row['Census_Tract']}<br>"
            f"Asthma Prevalence: {row['asthma_rate']}% of adults (Year: {int(row['year'])})<br>"
            f"Upper CI: {row['Rate Upper Confidence Interval']}"
        )

        color = pm25_2025_color(row['PM25_2025'])
        icon_type = site_type_icon(row['Name'])

        marker = folium.Marker(
            location=(row['Latitude'], row['Longitude']),
            popup=folium.Popup(popup_text, max_width=300),
            icon=folium.Icon(color=color, icon=icon_type, prefix='fa'),
            tooltip=row['Name']
        )

        name_lower = row['Name'].lower()
        if 'school' in name_lower:
            marker.add_to(fg_schools)
        elif 'home' in name_lower:
            marker.add_to(fg_homes)
        elif 'park' in name_lower or 'playlot' in name_lower:
            marker.add_to(fg_parks)
        elif 'office' in name_lower:
            marker.add_to(fg_offices)
        else:
            marker.add_to(fg_other)

    # Search bar (tract GEOIDs)
    Search(
        layer=tracts_geojson,
        search_label='GEOID',
        placeholder='🔍 Search Census Tract GEOID (e.g., 6081604200)',
        collapsed=False
    ).add_to(m)

    # Legend (smaller size)
    legend_html = """
    <div style="position: fixed;
         bottom: 40px; left: 40px; width: 200px; height: auto;
         border:1px solid grey; z-index:9999; font-size:12px;
         background-color: white; padding: 8px;">
    <b>Legend</b><br><br>
    <b>PM2.5 (2025) Color:</b><br>
    <span style="color:green; font-size:14px;">■</span> Low (<6 µg/m³)<br>
    <span style="color:orange; font-size:14px;">■</span> Moderate (6–9 µg/m³)<br>
    <span style="color:red; font-size:14px;">■</span> High (>9 µg/m³)<br><br>
    <b>Site Type Icons:</b><br>
    <span style="font-size:14px;">🎓</span> School<br>
    <span style="font-size:14px;">🏠</span> Home<br>
    <span style="font-size:14px;">🍃</span> Park / Playlot<br>
    <span style="font-size:14px;">🏢</span> Office<br>
    <span style="font-size:14px;">📍</span> Other
    </div>
    """
    m.get_root().html.add_child(folium.Element(legend_html))

    folium.LayerControl().add_to(m)
    return m
