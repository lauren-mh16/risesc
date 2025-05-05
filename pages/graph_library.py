import streamlit as st
import pandas as pd
from plots.plots_graph_library import demo_v_pm25, asthma_v_pm25, pm25_day_plot, pm25_month_plot



st.set_page_config(page_title="Additional Graphs", layout="wide")
st.title("Additional Graphs")

def load_data(url):
    return pd.read_csv(url)

df_demo = load_data('data/demo.csv')
df_clarity = load_data('data/clarity.csv')

col1, col2, = st.columns(2)

with col1:
    with st.expander("demographics and asthma rate", expanded=False):
        st.markdown("some brief description")
        fig1 = demo_v_pm25(df_demo)
        st.plotly_chart(fig1, use_container_width=True)
        st.caption("Sources: San Mateo County Health Asthma Reporting (2022), XXX Demographics Reporting (year)")

    fig3 = pm25_day_plot(df_clarity)
    st.plotly_chart(fig3)
    st.caption("Source: Rise South City Clarity Monitors (2024-2025)")

with col2:
    fig2 = asthma_v_pm25(df_demo)
    st.plotly_chart(fig2, use_container_width=True)
    st.caption("Sources: Rise South City Clarity Monitors (2024-2025), San Mateo County Health Asthma Reporting (2022)")
    fig4 = pm25_month_plot(df_clarity)
    st.plotly_chart(fig4)
    st.caption("Source: Rise South City Clarity Monitors (2024-2025)")

