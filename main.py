import pandas as pd
import streamlit as st
from plots import pm25_day_plot, pm25_month_plot


st.set_page_config(page_title="Air Quality Dashboard", layout="wide")

st.title("Hallo")

@st.cache_data
def load_data():
    df = pd.read_csv('data/clarity.csv')
    return df

df = load_data()

#fig_day = pm25_day_plot(df)
fig_month = pm25_month_plot(df)



#st.plotly_chart(fig_day)

st.plotly_chart(fig_month)

def main():
    st.title("PM2.5 and Asthma Rate Map (2025 Focus)")

    # Create and display map
    folium_map = create_map(df_merged)
    st_folium(folium_map, width=800, height=600)

if __name__ == '__main__':
    main()
