import streamlit as st
import pandas as pd
from plots.plots_graph_library import demo_v_pm25, asthma_v_pm25, pm25_day_plot, pm25_month_plot

if "graph_view" not in st.session_state:
    st.session_state.graph_view = None

st.set_page_config(page_title="Additional Graphs", layout="wide")
st.title("Additional Graphs")

def load_data(url):
    return pd.read_csv(url)

df_demo = load_data('data/demo.csv')
df_clarity = load_data('data/clarity.csv')

col1, col2, = st.columns(2)

if st.session_state.graph_view is None:

    with col1:
        with st.expander("demographics and asthma rate", expanded=False):
            st.markdown("some brief description")
            fig1 = demo_v_pm25(df_demo)
            st.plotly_chart(fig1, use_container_width=True)
            st.caption("Sources: San Mateo County Health Asthma Reporting (2022), U.S. Census Demographics Reporting (2020)")

        fig3 = pm25_day_plot(df_clarity)
        st.plotly_chart(fig3)
        st.caption("Source: Rise South City Clarity Monitors (2024-2025)")

    with col2:
        #fig2 = asthma_v_pm25(df_demo)
        #st.plotly_chart(fig2, use_container_width=True)
        st.caption("Sources: Rise South City Clarity Monitors (2024-2025), San Mateo County Health Asthma Reporting (2022)")
        if st.button("View Full", key="view_testing"):
            st.session_state.graph_view = "testing"

        fig4 = pm25_month_plot(df_clarity)
        st.plotly_chart(fig4)
        st.caption("Source: Rise South City Clarity Monitors (2024-2025)")

if st.session_state.graph_view == "testing":
    st.title("🟢 Demographics vs PM2.5")
    fig2 = asthma_v_pm25(df_demo)
    st.plotly_chart(fig2, use_container_width=True)
    st.button("🔙 Back to gallery", on_click=lambda: st.session_state.update(graph_view=None))
