import streamlit as st
import pandas as pd
from plots.plots_graph_library import demo_v_pm25, asthma_v_pm25, pm25_day_plot, pm25_month_plot, animated_pm25, day_graph
from utils import t, select_lang


st.set_page_config(page_title="Exploratory Data Visualizations", layout="wide")

select_lang()

st.title(t("Exploratory Data Visualizations"))

def load_data(url):
    return pd.read_csv(url)

df_demo = load_data('data/demo.csv')
df_clarity = load_data('data/clarity.csv')
df_hourly = load_data('data/clarity_hourly.csv')


with st.expander(t("PM2.5 and Asthma"), expanded=True):
    st.markdown(t("This set of graphs explores pollution and health through looking at asthma rates (first plot) "
                  "and health indicators of interest (second plot)."))
    st.markdown("---")

    fig2 = asthma_v_pm25(df_demo)
    st.plotly_chart(fig2, use_container_width=True)
    st.caption(
       t("Sources: Rise South City Clarity Monitors (2024-2025), San Mateo County Health Asthma Reporting (2022)"))
    st.markdown("---")

    # st.markdown(t("Compare average PM2.5 (y-axis) with a health indicators of interest (x-axis): smoking, obesity, "
    #                 "COPD, health care access, poverty, proximity to parks, and housing stress"))
    fig1 = demo_v_pm25(df_demo)
    st.plotly_chart(fig1, use_container_width=True)
    st.caption(
        t("Sources: San Mateo County Health Asthma Reporting (2022), U.S. Census Demographics Reporting (2020)"))
    st.markdown("---")
    
    st.markdown(t("1. Select a date range (be sure to select both a 'from' date and 'to' date!)"))
    st.markdown(t("2. If desired, select air monitor names to see individual trends. Deselect the name to remove the corresponding trendline.)"))
    fig6 = day_graph(df_hourly)
    st.plotly_chart(fig6, use_container_width=True)
    st.caption(
        t("Sources: Rise South City Clarity Monitors (2024-2025)"))

# with col2:
#     with st.expander("PM2.5 Across Time", expanded=True):
#         st.markdown("This set of graphs focuses on how PM2.5 levels vary through time.")
#         st.markdown("---")

#         fig3 = pm25_day_plot(df_clarity)
#         st.plotly_chart(fig3)
#         st.caption("Source: Rise South City Clarity Monitors (2024-2025)")
#         st.markdown("---")

#         fig4 = pm25_month_plot(df_clarity)
#         st.plotly_chart(fig4)
#         st.caption("Source: Rise South City Clarity Monitors (2024-2025)")


with st.expander(t("PM2.5 Interactive"), expanded=True):
    st.markdown(t("This interactive map displays PM2.5 through time. Use the slider to view a specific date's PM2.5 or "
                  "press the play button for the animation to run automatically."))
    st.markdown("---")
    fig5 = animated_pm25(df_clarity)
    st.plotly_chart(fig5)
    st.caption(t("Source: Rise South City Clarity Monitors (2024-2025)"))
    st.markdown("---")




