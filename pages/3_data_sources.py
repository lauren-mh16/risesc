import streamlit as st

st.set_page_config(page_title="Data Information", layout="wide")

st.markdown("#### Rise South City Clarity Monitors (2024-2025)")
st.markdown("Rise South City has 14 Clarity monitors around the South San Francisco and San Bruno area. The data collection "
            "timeframe ranges from November of 2024 to March of 2025.")
st.markdown("---")

st.markdown("#### PurpleAir Monitors (2018-XXXX)")
st.markdown("PurpleAir has an extensive network of air quality monitors. In South San Francisco and San Bruno, there is a total of"
            "# air monitors. The data collection timeframe is from 2018 to XXXX, so PurpleAir is used for the majority of longitudinal"
            "analyses and visualizations. However, a key limitation is that PurpleAir data suffers from more missing data, which we've imputed"
            "based on [some algorithmic formula].")
st.markdown("---")

st.markdown("#### San Mateo County Health Asthma Reporting (2022)")
st.markdown("San Mateo County collects health indicator data from a variety of data sources. We are particularly intersted in asthma indicators"
            "and we focus on census tract-level rates of asthma. ")
st.markdown("---")

st.markdown("#### U.S. Census Demographics Reporting (2020)")
st.markdown("---")
