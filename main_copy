import pandas as pd
import streamlit as st
from plots import pm25_day_plot, pm25_month_plot, create_map, site_type_icon, pm25_2025_color
from streamlit_folium import st_folium 


st.set_page_config(page_title="Air Quality Dashboard", layout="wide")

st.title("Hallo")

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

df = load_data('data/clarity.csv') 
df_merged = load_data('data/pm25_asthma_clean.csv')


#fig_day = pm25_day_plot(df)
fig_month = pm25_month_plot(df)

#st.plotly_chart(fig_day)

st.plotly_chart(fig_month)



# def main():
st.title("PM2.5 and Asthma Rate Map (2025 Focus)")

# Create and display map
folium_map = create_map(df_merged)
st_folium(folium_map, width=800, height=600)

# if __name__ == '__main__':
#     main()
