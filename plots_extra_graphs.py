import streamlit as st
import pandas as pd
import plotly.express as px

def load_data():
    return pd.read_csv('data/demo.csv')

df = load_data()
demographic_vars = ['Smoking Prevalence', 'Obesity Prevalence', 'COPD Prevalence', 'Lack of Health Care Access Prevalence',
                    'Percent Population Within Half a Mile to Parks', 'Population Below Poverty Level', 'Housing Stress']


def asthma_v_pm25(df):
    df_graph = df.groupby(["Name"]).agg({
    "pm_conc": "mean",
    "asthma_rate": "first"
    }).reset_index()

    fig = px.scatter(
        df_graph, x='pm_conc', y='asthma_rate',
        hover_name="Name",
        hover_data={
            "pm_conc": ":.2f",
        }
    )
    fig.update_traces(marker=dict(size=20, opacity=0.6))
    return fig


def demo_v_pm25(df):

    selected_var = st.selectbox(
        "Choose a variable to visualize",
        options=demographic_vars
    )

    df_graph = df.groupby(["Name"]).agg({
        "pm_conc": "mean",
        "asthma_rate": "first",
        selected_var: "first"

    }).reset_index()

    fig = px.scatter(
        df_graph, x=selected_var, y='asthma_rate', hover_name="Name"
    )
    fig.update_traces(marker=dict(size=20, opacity=0.6))

    return fig


def pm25_day_plot(df):
    graph = df.groupby(["Name", "day"]).agg({
        "pm_conc": ["mean", "median", "std"],
        "asthma_rate": "first",
        "month_cat": "first",
        "Longitude": "first"
    }).reset_index()

    graph.columns = ['_'.join(col).strip('_') for col in graph.columns.values]

    fig = px.scatter(
        graph,
        x='pm_conc_mean',
        y='pm_conc_std',
        color='day',
        title="PM2.5 Mean vs. Standard Deviation by Day",
        labels={
            'pm_conc_mean': 'Average PM2.5 Concentration',
            'pm_conc_std': 'Standard Deviation of PM2.5 Concentration',
            'day': 'Day of Measurement'
        },
        hover_name="Name",
        hover_data={
            "pm_conc_mean": ":.2f",
            "pm_conc_std": ":.2f"
        }
    )
    return fig


