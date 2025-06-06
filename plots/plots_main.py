import plotly.express as px
import pandas as pd
import folium
import plotly.express as px
from folium.plugins import Search
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import plotly.graph_objects as go
from utils import t


# Helper: Color function for PM2.5
def pm25_2025_color(pm25_2025):
    """
    Returns a HEX color code for a given PM2.5 value (24-hour avg),
    using the EPA 2025 color scale, mapped continuously between thresholds.
    """
    # Define EPA breakpoints and corresponding hex colors
    breakpoints = [0.0, 12.0, 35.4, 55.4, 150.4, 250.4, 500.4]
    colors = [
        "#00E400",  # Good (Green)
        "#FFFF00",  # Moderate (Yellow)
        "#FF7E00",  # Unhealthy for Sensitive Groups (Orange)
        "#FF0000",  # Unhealthy (Red)
        "#8F3F97",  # Very Unhealthy (Purple)
        "#7E0023"   # Hazardous (Maroon)
    ]

    # Interpolate between the appropriate breakpoints
    for i in range(len(breakpoints) - 1):
        if breakpoints[i] <= pm25_2025 < breakpoints[i + 1]:
            # Linear interpolation between the two colors
            ratio = ((pm25_2025 - breakpoints[i]) /
                     (breakpoints[i + 1] - breakpoints[i]))
            color_start = colors[i].lstrip('#')
            color_end = colors[i + 1].lstrip('#')

            # Convert hex to RGB
            r1, g1, b1 = int(color_start[0:2], 16), int(color_start[2:4], 16), int(color_start[4:6], 16)
            r2, g2, b2 = int(color_end[0:2], 16), int(color_end[2:4], 16), int(color_end[4:6], 16)

            # Interpolate RGB
            r = int(r1 + (r2 - r1) * ratio)
            g = int(g1 + (g2 - g1) * ratio)
            b = int(b1 + (b2 - b1) * ratio)

            return f'#{r:02X}{g:02X}{b:02X}'

    # Fallback (shouldn't be hit)
    return "#000000"

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

def create_div_icon_marker(row):
    color = pm25_2025_color(row['PM25_2025'])
    emoji = site_type_emoji(row['Name'])  

    html = f"""
    <div style="
        display: flex;
        align-items: center;
        justify-content: center;
        width: 26px;
        height: 26px;
        background-color: {color};
        border-radius: 50%;
        border: 1.5px solid black;
        font-size: 14px;
        text-align: center;
    ">
        {emoji}
    </div>
    """

    popup_text = (
        f"<b>{emoji} {row['Name']}</b><br>"
        f"PM2.5 (2024): {row['PM25_2024']:.2f} µg/m³<br>"
        f"PM2.5 (2025): {row['PM25_2025']:.2f} µg/m³<br>"
        f"Census Tract: {row['Census_Tract']}<br>"
        f"Asthma Prevalence: {row['asthma_rate']}% of adults (Year: {int(row['year'])})<br>"
        f"Upper CI: {row['Rate Upper Confidence Interval']}"
    )

    return folium.Marker(
        location=(row['Latitude'], row['Longitude']),
        icon=folium.DivIcon(html=html),
        popup=folium.Popup(popup_text, max_width=300),
        tooltip=row['Name']
    )

def create_folium_map(df_merged):
    center_lat = df_merged['Latitude'].mean()
    center_lon = df_merged['Longitude'].mean()
    m = folium.Map(location=[center_lat, center_lon], zoom_start=12)

    # Add Census Tract Choropleth (Asthma Prevalence)
    tracts_path = 'data/sf_sanbruno_census_tracts.geojson'

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
        legend_name=t('Asthma Prevalence (%) (Adults 18+)'),
        highlight=True,
    ).add_to(m)

    # GeoJson layer for tract outlines + search
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

    # FeatureGroups for toggling
    fg_schools = folium.FeatureGroup(name='Schools').add_to(m)
    fg_homes = folium.FeatureGroup(name='Homes').add_to(m)
    fg_parks = folium.FeatureGroup(name='Parks / Playlots').add_to(m)
    fg_offices = folium.FeatureGroup(name='Offices').add_to(m)
    fg_other = folium.FeatureGroup(name='Other').add_to(m)

    # Add markers
    for _, row in df_merged.iterrows():
        standard_marker = create_div_icon_marker(row)

        name_lower = row['Name'].lower()
        if 'school' in name_lower:
            standard_marker.add_to(fg_schools)
        elif 'home' in name_lower:
            standard_marker.add_to(fg_homes)
        elif 'park' in name_lower or 'playlot' in name_lower:
            standard_marker.add_to(fg_parks)
        elif 'office' in name_lower:
            standard_marker.add_to(fg_offices)
        else:
            standard_marker.add_to(fg_other)

    # Add search bar for Census Tract GEOIDs
    Search(
        layer=tracts_geojson,
        search_label='GEOID',
        placeholder='🔍 Search Census Tract GEOID (e.g., 6081604200)',
        collapsed=False
    ).add_to(m)

    # Add legend with dark mode-safe colors
    # Add updated legend for PM2.5 (2025) with finer color scale and dark mode-safe formatting
    legend_html = """
    <div style="position: fixed;
         bottom: 40px; left: 40px; width: 220px; height: auto;
         border:1px solid grey; z-index:9999; font-size:12px;
         background-color: white; padding: 10px; color: black;">
    <b>Legend</b><br><br>
    <b>PM2.5 (2025) Color:</b><br>
    <span style="color:#006400; font-size:14px;">■</span> 0–3 µg/m³ (Very Low)<br>
    <span style="color:#228B22; font-size:14px;">■</span> 3–6 µg/m³ (Low)<br>
    <span style="color:#ADFF2F; font-size:14px;">■</span> 6–9 µg/m³ (Moderate)<br>
    <span style="color:#FFD700; font-size:14px;">■</span> 9–12 µg/m³ (Elevated)<br>
    <span style="color:#FF8C00; font-size:14px;">■</span> 12–15 µg/m³ (Unhealthy for Sensitive Groups)<br>
    <span style="color:#FF0000; font-size:14px;">■</span> 15+ µg/m³ (Unhealthy)<br><br>
    <b>Site Type Icons:</b><br>
    <span style="font-size:14px;">🎓 School</span><br>
    <span style="font-size:14px;">🏠 Home</span><br>
    <span style="font-size:14px;">🍃 Park / Playlot</span><br>
    <span style="font-size:14px;">🏢 Office</span><br>
    <span style="font-size:14px;">📍 Other</span>
    </div>
    """
    
    m.get_root().html.add_child(folium.Element(legend_html))


    # ✅ Add LayerControl LAST
    folium.LayerControl().add_to(m)

    return m


def pm25_avg(data):

    data['pm2_5ConcMass24HourMean.value'] = data['pm2_5ConcMass24HourMean.value'].fillna(0)
    data['endOfPeriod'] = pd.to_datetime(data['endOfPeriod'])

    avg_df = (
        data.groupby('endOfPeriod', as_index=False)
            .agg(mean_pm2_5=('pm2_5ConcMass24HourMean.value', 'mean'))
    )

    fig = px.line(
        avg_df,
        x='endOfPeriod',
        y='mean_pm2_5',
        title=t('Average PM2.5 Across All Monitors'),
        labels={'endOfPeriod': t('Date'), 'mean_pm2_5': t('PM2.5 (µg/m³)')},
    )
    fig.update_traces(line=dict(color='#1E4D94', width=3))
    fig.update_layout(template='plotly_white', height=450)
    return fig

def trends_all(data):
    avg_df = (
        data.groupby('endOfPeriod', as_index=False)
            .agg(mean_pm2_5=('pm2_5ConcMass24HourMean.value', 'mean'))
    )

    data['pm2_5ConcMass24HourMean.value'] = data['pm2_5ConcMass24HourMean.value'].fillna(0)
    data['endOfPeriod'] = pd.to_datetime(data['endOfPeriod'])
    data = data.sort_values(by=["Name", "endOfPeriod"])

    fig = go.Figure()

    for site in data['Name'].unique():
        df_site = data[data['Name'] == site]
        fig.add_trace(
            go.Scatter(
                x = df_site['endOfPeriod'],
                y=df_site['pm2_5ConcMass24HourMean.value'],
                mode = 'lines',
                name = site,
                opacity = 0.6,
                hovertemplate='<br>Site: %{fullData.name}<br>Date: %{x|%b %d, %Y}<br>PM2.5: %{y:.2f} µg/m³<extra></extra>'
            )
        )

    fig.add_trace(
        go.Scatter(
            x = avg_df['endOfPeriod'],
            y=avg_df['mean_pm2_5'],
            mode='lines',
            name='Average (All Sites)',
            visible='legendonly',
            line=dict(color='#1E4D94', width=4,), showlegend=True,
            hovertemplate='<br>Site: %{fullData.name}<br>Date: %{x|%b %d, %Y}<br>PM2.5: %{y:.2f} µg/m³<extra></extra>',
        )

    )

    fig.update_layout(template='plotly_white', height=550, title=t("PM2.5 through time across monitors"),
                      xaxis_title=t('Date'), yaxis_title=t('PM2.5 (µg/m³)'))

    return fig
