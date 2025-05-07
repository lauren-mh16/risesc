# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
# import seaborn as sns

# Import the updated Clarity data from the csv file
data = pd.read_csv('data/risesouthcity_april_daily.csv') # 10/31 to 4/1
# data2 = pd.read_csv('clarity_daily.csv') # 10/31 to 1/1
# data3 = pd.read_csv('risesouthcity_clarity_24hmean_cleaned (1).csv') # 10/31 to 1/1

# Display and summarize the data
# print(data.head())
# print(data.describe())
# print(data.isnull().sum()) # num null values
# print(data['endOfPeriod'].min(), data['endOfPeriod'].max()) # range of dates
# print(data['Name'].unique()) # List the "Name" columns in the data dataframe

# Calculate the mean of pm2_5ConcMass24HourMean.value for each endOfPeriod
data['pm2_5ConcMass24HourMean.value'] = data['pm2_5ConcMass24HourMean.value'].fillna(0)
data['mean_pm2_5ConcMass24HourMean.value'] = data.groupby('endOfPeriod')['pm2_5ConcMass24HourMean.value'].transform('mean')
data['endOfPeriod'] = pd.to_datetime(data['endOfPeriod']) # Convert endOfPeriod to datetime format


# Make a dataframe with the mean of pm2_5ConcMass24HourMean.value for each endOfPeriod
data_mean = data[['endOfPeriod', 'mean_pm2_5ConcMass24HourMean.value']]
data_mean = data_mean.sort_values(by='endOfPeriod')

# Add the PM2.5  for 'Belle Air School', 'Rise South City Office', and 'Portola Elementary' to the dataframe
target_locations = ['Belle Air School', 'Rise South City Office','Portola Elementary']
for loc in target_locations:
    loc_data = data[data['Name'] == loc][['endOfPeriod', 'pm2_5ConcMass24HourMean.value']]
    loc_data = loc_data.rename(columns={'pm2_5ConcMass24HourMean.value': loc})
    data_mean = pd.merge(data_mean, loc_data, on='endOfPeriod', how='left') # Merge on endOfPeriod
print(data_mean.head())

# Make a Plot for PM2.5 average!
plt.figure(figsize=(10, 6))
plt.plot(data_mean['endOfPeriod'], data_mean['mean_pm2_5ConcMass24HourMean.value'],label='Average', color='black', linewidth=5, alpha=0.7)
plt.plot(data_mean['endOfPeriod'], data_mean['Belle Air School'], label='Belle Air School', color='blue', linewidth=1, alpha=0.7)
plt.plot(data_mean['endOfPeriod'], data_mean['Rise South City Office'], label='Rise South City Office', color='red', linewidth=1, alpha=0.7)
plt.plot(data_mean['endOfPeriod'], data_mean['Portola Elementary'], label='Portola Elementary', color='green', linewidth=1, alpha=0.7)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%B'))  # '%b' = abbreviated month name; use '%B' for full name

# Labels
plt.xlabel('Date (Nov 2024 through Mar 2025)')
plt.ylabel('Mean PM2.5 (µg/m³)')
plt.legend(title='Location')
plt.title('Rolling Averages of PM2.5 Concentration (Clarity)')
plt.show()
