import streamlit as st
import pandas as pd
from plots.plots_graph_library import demo_v_pm25, asthma_v_pm25, pm25_day_plot, pm25_month_plot, animated_pm25

if "graph_view" not in st.session_state:
    st.session_state.graph_view = None

st.set_page_config(page_title="Exploratory Data Visualizations", layout="wide")
st.title("Exploratory Data Visualizations")

def load_data(url):
    return pd.read_csv(url)

df_demo = load_data('data/demo.csv')
df_clarity = load_data('data/clarity.csv')

# col1, col2, = st.columns(2)


# with col1:
with st.expander("PM2.5 and Asthma", expanded=True):
    st.markdown("This set of graphs explores pollution and health through looking at asthma rates, as well as demographic variation.")
    st.markdown("---")

    fig2 = asthma_v_pm25(df_demo)
    st.plotly_chart(fig2, use_container_width=True)
    st.caption(
        "Sources: Rise South City Clarity Monitors (2024-2025), San Mateo County Health Asthma Reporting (2022)")
    st.markdown("---")

    fig1 = demo_v_pm25(df_demo)
    st.plotly_chart(fig1, use_container_width=True)
    st.caption(
        "Sources: San Mateo County Health Asthma Reporting (2022), U.S. Census Demographics Reporting (2020)")



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


with st.expander("PM2.5 Interactive", expanded=True):
    fig5 = animated_pm25(df_clarity)
    st.plotly_chart(fig5)
    st.caption("Source: Rise South City Clarity Monitors (2024-2025)")
    st.markdown("---")

    # fig6 = animation_test(df_clarity)
    # st.pydeck_chart(fig6)
    # st.caption("Source: Rise South City Clarity Monitors (2024-2025)")

