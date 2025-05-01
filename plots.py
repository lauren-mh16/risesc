## creating plots

import plotly.express as px
import pandas as pd

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

def pm25_month_plot(df):
    df['month_cat'] = pd.Categorical(
        df["month"],
        categories=[11, 12, 1, 2, 3],
        ordered=True
    )
    graph = df.groupby(["Name", "month_cat"]).agg({
        "pm_conc": ["mean", "median", "std"],
        "asthma_rate": "first",
    }).reset_index()

    graph.columns = ['_'.join(col).strip('_') for col in graph.columns.values]
    graph = graph.dropna()

    fig = px.scatter(graph, x='pm_conc_mean', y='asthma_rate_first', color='month_cat', size='pm_conc_std')
    return fig

