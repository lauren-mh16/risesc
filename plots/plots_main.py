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
        legend_name='Asthma Prevalence (%) (Adults 18+)',
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

        standard_marker = folium.Marker(
            location=(row['Latitude'], row['Longitude']),
            popup=folium.Popup(popup_text, max_width=300),
            icon=folium.Icon(color=color, icon=icon_type, prefix='fa'),
            tooltip=row['Name']
        )

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
    legend_html = """
    <div style="position: fixed;
         bottom: 40px; left: 40px; width: 200px; height: auto;
         border:1px solid grey; z-index:9999; font-size:12px;
         background-color: white; padding: 8px; color: black;">
    <b>Legend</b><br><br>
    <b>PM2.5 (2025) Color:</b><br>
    <span style="color:green; font-size:14px;">■</span> Low (&lt;6 µg/m³)<br>
    <span style="color:orange; font-size:14px;">■</span> Moderate (6–9 µg/m³)<br>
    <span style="color:red; font-size:14px;">■</span> High (&gt;9 µg/m³)<br><br>
    <b>Site Type Icons:</b><br>
    <span style="font-size:14px; color: black;">🎓 School</span><br>
    <span style="font-size:14px; color: black;">🏠 Home</span><br>
    <span style="font-size:14px; color: black;">🍃 Park / Playlot</span><br>
    <span style="font-size:14px; color: black;">🏢 Office</span><br>
    <span style="font-size:14px; color: black;">📍 Other</span>
    </div>
    """
    m.get_root().html.add_child(folium.Element(legend_html))

    # ✅ Add LayerControl LAST
    folium.LayerControl().add_to(m)

    return m

def create_pm25_over_time():
    # Load Clarity dataset
    data = pd.read_csv('data/risesouthcity_april_daily.csv')

    # Clean and process
    data['pm2_5ConcMass24HourMean.value'] = data['pm2_5ConcMass24HourMean.value'].fillna(0)
    data['endOfPeriod'] = pd.to_datetime(data['endOfPeriod'])
    data['mean_pm2_5ConcMass24HourMean.value'] = data.groupby('endOfPeriod')['pm2_5ConcMass24HourMean.value'].transform('mean')

    # Build mean data frame
    data_mean = data[['endOfPeriod', 'mean_pm2_5ConcMass24HourMean.value']].drop_duplicates().sort_values(by='endOfPeriod')

    # Add selected locations
    target_locations = ['Belle Air School', 'Rise South City Office', 'Portola Elementary']
    for loc in target_locations:
        loc_data = data[data['Name'] == loc][['endOfPeriod', 'pm2_5ConcMass24HourMean.value']]
        loc_data = loc_data.rename(columns={'pm2_5ConcMass24HourMean.value': loc})
        data_mean = pd.merge(data_mean, loc_data, on='endOfPeriod', how='left')

    # Plot with matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(data_mean['endOfPeriod'], data_mean['mean_pm2_5ConcMass24HourMean.value'], label='Average', color='black', linewidth=5, alpha=0.7)
    ax.plot(data_mean['endOfPeriod'], data_mean['Belle Air School'], label='Belle Air School', color='blue', linewidth=1, alpha=0.7)
    ax.plot(data_mean['endOfPeriod'], data_mean['Rise South City Office'], label='Rise South City Office', color='red', linewidth=1, alpha=0.7)
    ax.plot(data_mean['endOfPeriod'], data_mean['Portola Elementary'], label='Portola Elementary', color='green', linewidth=1, alpha=0.7)

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%B'))
    ax.set_xlabel('Date (Nov 2024 through Mar 2025)')
    ax.set_ylabel('Mean PM2.5 (µg/m³)')
    ax.set_title('Rolling Averages of PM2.5 Concentration (Clarity)')
    ax.legend(title='Location')

    # Streamlit output
    st.subheader("PM2.5 Over Time")
    st.pyplot(fig)
