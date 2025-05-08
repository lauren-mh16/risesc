import streamlit as st
import pandas as pd
import plotly.express as px
import pydeck as pdk


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
        },
        labels={
            'pm_conc': 'Average PM2.5 Concentration',
            'asthma_rate': '2022 Asthma Rate by Census Tract',
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
        df_graph, x=selected_var, y='pm_conc', hover_name="Name",
        labels={
            'pm_conc': 'Average PM2.5 Concentration',
            'asthma_rate': '2022 Asthma Rate by Census Tract',
            'day': 'Day of Week'
        }
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
            'pm_conc_std': 'Standard Deviation',
            'day': 'Day of Week'
        },
        hover_name="Name",
        hover_data={
            "pm_conc_mean": ":.2f",
            "pm_conc_std": ":.2f"
        }
    )
    return fig

# Plot: PM2.5 by Month
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

    fig = px.scatter(graph, x='pm_conc_mean', y='asthma_rate_first', color='month_cat', size='pm_conc_std',
                     labels={
                         'pm_conc_mean': 'Average PM2.5 Concentration',
                         'pm_conc_std': 'Standard Deviation',
                         'month_cat': 'Month',
                         'asthma_rate_first': '2022 Asthma Rate by Census Tract'
                     }
                     )
    return fig


## create animated dot map

def color_values(val):
    if val <= 12:
        return "Low"

    elif val > 12 and val < 35:
        return "Moderate"

    elif val >= 35:
        return "High"


def animated_pm25(df):
    df = df.sort_values("datetime")
    df['cats'] = df['pm_conc'].apply(color_values) # only 8 values considered high

    colors = {
        "Low": "blue",
        "Moderate": "orange",
        "High": "red"
    }

    dummy_rows = []
    for dt in df['datetime'].unique():
        for cat in colors:
            dummy_rows.append({
                "Latitude": None,
                "Longitude": None,
                "pm_conc": 10,
                "Name": "",
                "datetime": dt,
                "cats": cat
            })
    df_graph = pd.concat([df, pd.DataFrame(dummy_rows)], ignore_index=True)

    fig = px.scatter_map(
        df_graph,
        lat="Latitude",
        lon="Longitude",
        size="pm_conc",  # Changes point size over time
        #text="Name",
        animation_frame="datetime",  # Creates animation per time period
        zoom=11,
        center={"lat": 37.640664, "lon": -122.4111},  # Center on San Bruno
       # map_style="carto-positron",
        color='cats',
        color_discrete_map=colors,
        hover_data={"pm_conc": True, "Latitude": False, "Longitude": False, "Name": True}
    )

    fig.update_layout(

        height=400, width=400,
    )


    return fig

# def animation_test(df):
#     df['datetime'] = pd.to_datetime(df['datetime'])
#     dates = sorted(df["datetime"].dt.date.unique())
#     selected_date = st.slider(
#         "Select Date",
#         min_value=dates[0],
#         max_value=dates[-1],
#         value=dates[0]
#     )
#     filtered = df[df["datetime"].dt.date == selected_date]
#     filtered = filtered.dropna()
#     filtered = filtered.rename(columns={"Longitude": "lon", "Latitude": "lat"})

#     if filtered.empty:
#         st.warning("No data available for this date.")
#         return None

#     layer = pdk.Layer(
#         "ScatterplotLayer",
#         data=filtered,
#         get_position='[lon, lat]',
#         get_radius='pm_conc * 20',
#         get_fill_color='[180, 0, 200, 140]',
#         pickable=True,
#         auto_highlight=True
#     )

#     view_state = pdk.ViewState(
#         latitude=filtered["lat"].mean(),
#         longitude=filtered["lon"].mean(),
#         zoom=11,
#         pitch=45
#     )

#     r = pdk.Deck(
#         layers=[layer],
#         initial_view_state=view_state,
#         tooltip={"text": "Site: {Name}\nPM2.5: {pm_conc}"},
#         map_style="mapbox://styles/mapbox/light-v9"
#     )

#     return r



