import streamlit as st
import pandas as pd
import json
from shapely.geometry import Point, shape
from geopy.geocoders import Nominatim
from utils import t, select_lang

st.set_page_config(page_title="Address Search-Up", layout="wide")

select_lang()

st.title(t("Search for information in your neighborhood"))
geolocator = Nominatim(user_agent="my_app", timeout=5)


def load_data(url):
    return pd.read_csv(url)

df_pollution = load_data('data/demo.csv')
df_pollution['Census_Tract'] = df_pollution['Census_Tract'].astype(str)
df_demo = load_data('data/CA_census tracts_demographic_data (1).csv')
df_demo['Census_Tract'] = df_demo['GEOID'].astype(str)

with open("data/sf_sanbruno_census_tracts.geojson") as f:
    tracts_geojson = json.load(f)


address = st.text_input(t("Please follow this format: 123 Street, City, CA"), placeholder=t("123 Street, City, CA"))
st.markdown(t("**Note:** Information is only available for Bay Area neighborhoods from San Francisco to Menlo Park."))

tract_id = None

if address:
    geolocator = Nominatim(user_agent="my_app")
    location = geolocator.geocode(address)

    if location:
        st.success(f"Found: {location.address}")
        lat, lon = location.latitude, location.longitude

        point = Point(lon, lat)

        for feature in tracts_geojson["features"]:
            polygon = shape(feature["geometry"])
            if polygon.contains(point):
                tract_id = feature["properties"]["GEOID"]
                st.success(f"Matched Census Tract: {tract_id}")
                break

        if not tract_id:
            st.warning(t("Could not match to a census tract."))
    else:
        st.error(t("Address not found."))


if tract_id:
    rows = df_pollution[df_pollution["Census_Tract"] == tract_id[1:]]
    if not rows.empty:
        r = rows.iloc[0]
        mean_pm = round(rows['pm_conc'].mean(), 2)
        std_pm = round(rows['pm_conc'].std(), 2)
        st.metric(t("PM2.5 average (Nov 2024 - March 2025)"), f"{mean_pm} µg/m³")
        st.metric(t("PM2.5 standard deviation (Nov 2024 - March 2025)"), f"{std_pm} µg/m³")
        st.metric(t("Asthma Rate (2022)"), f"{r['asthma_rate']}%")
    else:
        st.error(t("No air quality information found"))

if tract_id:
    rows = df_demo[df_demo["Census_Tract"] == tract_id[1:]]
    if not rows.empty:
        r = rows.iloc[0]
        st.metric(t("Population Below Poverty Level"), f"{r['Population Below Poverty Level']}")
        st.metric(t("Smoking Prevalence"), f"{r['Smoking Prevalence']%}")
        st.metric(t("Obesity Prevalence"), f"{r['Obesity Prevalence']%}")
        st.metric(t("Lack of Health Care Access Prevalence"), f"{r['Lack of Health Care Access Prevalence']%}")
    else:
        st.error(t("No demographics information found"))
