import streamlit as st
import pandas as pd
import json
from shapely.geometry import Point, shape
from geopy.geocoders import Nominatim

st.set_page_config(page_title="Address Search-Up", layout="wide")
st.title("Type in your address and get info!")
geolocator = Nominatim(user_agent="my_app", timeout=5)


def load_data(url):
    return pd.read_csv(url)

df = load_data('data/demo.csv')
df['Census_Tract'] = df['Census_Tract'].astype(str)

with open("data/sf_sanbruno_census_tracts.geojson") as f:
    tracts_geojson = json.load(f)


address = st.text_input("Enter your address", placeholder = "Please follow this exact format: 123 Street, City, CA")
tract_id = None

if address:
    geolocator = Nominatim(user_agent="my_app")
    location = geolocator.geocode(address)

    if location:
        st.success(f"Found: {location.address}")
        lat, lon = location.latitude, location.longitude

        # Convert to shapely Point
        point = Point(lon, lat)

        # Find matching tract
        for feature in tracts_geojson["features"]:
            polygon = shape(feature["geometry"])
            if polygon.contains(point):
                tract_id = feature["properties"]["GEOID"]
                st.success(f"Matched Census Tract: {tract_id}")
                break

        if not tract_id:
            st.warning("Could not match to a census tract.")
    else:
        st.error("Address not found.")


if tract_id:
    rows = df[df["Census_Tract"] == tract_id[1:]]
    if not rows.empty:
        r = rows.iloc[0]
        st.metric("PM2.5", f"{r['pm_conc']} µg/m³")
        st.metric("Asthma Rate", f"{r['asthma_rate']}%")
        st.metric("Population Below Poverty Level", f"{r['Population Below Poverty Level']}")
    else:
        st.error("No information found")