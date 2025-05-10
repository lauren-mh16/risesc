import streamlit as st
from utils import t, select_lang

st.set_page_config(page_title="Data Sources & Methodology", layout="wide")

select_lang()

st.title(t("Data Sources & Methodology"))

st.markdown(t("#### Rise South City Clarity Monitors (2024–2025)"))
st.markdown(
    t("The Rise South City initiative deployed 14 Clarity air quality monitors across South San Francisco and San Bruno. "
    "These monitors collected PM2.5 concentration data from November 2024 through March 2025, providing hyperlocal air "
    "pollution readings to support environmental monitoring and health risk assessment.")
)
st.markdown("---")

st.markdown(t("#### PurpleAir Monitors (2018–Present)"))
st.markdown(
    t("PurpleAir maintains an extensive network of low-cost air quality sensors. In South San Francisco and San Bruno, a total of "
    "34 monitors provide continuous air quality measurements. The dataset spans from 2018 to the present and is used "
    "for most longitudinal analyses and visualizations. A key limitation is the presence of missing data; imputation was performed "
    "using a custom algorithm to address these gaps and maintain data continuity.")
)
st.markdown("---")

st.markdown(t("#### San Mateo County Health Asthma Reporting (2022)"))
st.markdown(
    t("San Mateo County compiles health indicator data from various sources. This dashboard focuses on asthma prevalence data at the census "
    "tract level, sourced from the county’s 2022 health reports. These model-based estimates provide insight into local health disparities "
    "and environmental health risks.")
)
st.markdown("---")

st.markdown(t("#### U.S. Census Demographics Reporting (2020)"))
st.markdown(
    t("Demographic data—including population counts, age distributions, and socioeconomic indicators—are drawn from the 2020 U.S. Census. "
    "These data are used to contextualize air quality and asthma prevalence findings at the census tract level, enabling analyses of potential "
    "environmental justice implications.")
)
st.markdown("---")
