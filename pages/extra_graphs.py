import streamlit as st
import pandas as pd
import plotly.express as px
from plots_extra_graphs import demo_v_pm25, asthma_v_pm25, pm25_day_plot



st.set_page_config(page_title="Additional Information", layout="wide")
st.title("Additional Information")

def load_data(url):
    return pd.read_csv(url)

df_demo = load_data('data/demo.csv')
df_clarity = load_data('data/clarity.csv')


# demographic_vars = ['Smoking Prevalence', 'Obesity Prevalence', 'COPD Prevalence', 'Lack of Health Care Access Prevalence',
#                     'Percent Population Within Half a Mile to Parks', 'Population Below Poverty Level', 'Housing Stress']
#
# col1, col2 = st.columns(2)
# with col2:
#     selected_var = st.selectbox(
#         "Choose a variable to visualize",
#         options=demographic_vars
#     )

# df_graph = df.groupby(["Name"]).agg({
#     "pm_conc": "mean",
#     "asthma_rate": "first",
#     selected_var: "first"
#
# }).reset_index()

# fig1 = px.scatter(
#     df_graph, x = 'pm_conc', y = 'asthma_rate',
#     hover_name="Name",
#     hover_data={
#     "pm_conc": ":.2f",
#     }
# )
# fig1.update_traces(marker=dict(size=20, opacity=0.6))


# fig2 = px.scatter(
#     df_graph, x = selected_var, y = 'asthma_rate', hover_name="Name"
# )
# fig2.update_traces(marker=dict(size=20, opacity=0.6))

# with col1:
#     st.plotly_chart(fig1, use_container_width=True)
#
# with col2:
#     st.plotly_chart(fig2, use_container_width=True)
#

fig1 = demo_v_pm25(df_demo)
fig2 = asthma_v_pm25(df_demo)
fig3 = pm25_day_plot(df_clarity)

st.plotly_chart(fig1, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)
st.plotly_chart(fig3)


