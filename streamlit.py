{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9dcf8f22-7b2b-4e32-adf6-9bb70cb825d2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import plotly.express as px"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "id": "da7f0064-332c-4f3f-87b0-dc3435b77b90",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Latitude</th>\n",
       "      <th>Longitude</th>\n",
       "      <th>datetime</th>\n",
       "      <th>pm_conc</th>\n",
       "      <th>Name</th>\n",
       "      <th>month</th>\n",
       "      <th>day</th>\n",
       "      <th>month_cat</th>\n",
       "      <th>threshold</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>37.63757</td>\n",
       "      <td>122.43270</td>\n",
       "      <td>2025-01-17 00:00:00+00:00</td>\n",
       "      <td>16.29</td>\n",
       "      <td>Brentwood Park</td>\n",
       "      <td>1</td>\n",
       "      <td>Friday</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>37.63757</td>\n",
       "      <td>122.43270</td>\n",
       "      <td>2024-12-20 00:00:00+00:00</td>\n",
       "      <td>24.40</td>\n",
       "      <td>Brentwood Park</td>\n",
       "      <td>12</td>\n",
       "      <td>Friday</td>\n",
       "      <td>12</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>37.63757</td>\n",
       "      <td>122.43270</td>\n",
       "      <td>2025-01-18 00:00:00+00:00</td>\n",
       "      <td>11.03</td>\n",
       "      <td>Brentwood Park</td>\n",
       "      <td>1</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>37.63757</td>\n",
       "      <td>122.43270</td>\n",
       "      <td>2025-01-19 00:00:00+00:00</td>\n",
       "      <td>11.56</td>\n",
       "      <td>Brentwood Park</td>\n",
       "      <td>1</td>\n",
       "      <td>Sunday</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>37.63757</td>\n",
       "      <td>122.43270</td>\n",
       "      <td>2024-12-29 00:00:00+00:00</td>\n",
       "      <td>2.58</td>\n",
       "      <td>Brentwood Park</td>\n",
       "      <td>12</td>\n",
       "      <td>Sunday</td>\n",
       "      <td>12</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2064</th>\n",
       "      <td>37.66409</td>\n",
       "      <td>122.40165</td>\n",
       "      <td>2024-11-19 00:00:00+00:00</td>\n",
       "      <td>4.77</td>\n",
       "      <td>Gardiner Park</td>\n",
       "      <td>11</td>\n",
       "      <td>Tuesday</td>\n",
       "      <td>11</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2065</th>\n",
       "      <td>37.66409</td>\n",
       "      <td>122.40165</td>\n",
       "      <td>2025-01-13 00:00:00+00:00</td>\n",
       "      <td>4.91</td>\n",
       "      <td>Gardiner Park</td>\n",
       "      <td>1</td>\n",
       "      <td>Monday</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2066</th>\n",
       "      <td>37.66409</td>\n",
       "      <td>122.40165</td>\n",
       "      <td>2024-11-22 00:00:00+00:00</td>\n",
       "      <td>1.91</td>\n",
       "      <td>Gardiner Park</td>\n",
       "      <td>11</td>\n",
       "      <td>Friday</td>\n",
       "      <td>11</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2067</th>\n",
       "      <td>37.66409</td>\n",
       "      <td>122.40165</td>\n",
       "      <td>2024-12-18 00:00:00+00:00</td>\n",
       "      <td>12.96</td>\n",
       "      <td>Gardiner Park</td>\n",
       "      <td>12</td>\n",
       "      <td>Wednesday</td>\n",
       "      <td>12</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2068</th>\n",
       "      <td>37.66409</td>\n",
       "      <td>122.40165</td>\n",
       "      <td>2025-04-01 00:00:00+00:00</td>\n",
       "      <td>3.90</td>\n",
       "      <td>Gardiner Park</td>\n",
       "      <td>4</td>\n",
       "      <td>Tuesday</td>\n",
       "      <td>4</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2069 rows × 9 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      Latitude  Longitude                  datetime  pm_conc            Name  \\\n",
       "0     37.63757  122.43270 2025-01-17 00:00:00+00:00    16.29  Brentwood Park   \n",
       "1     37.63757  122.43270 2024-12-20 00:00:00+00:00    24.40  Brentwood Park   \n",
       "2     37.63757  122.43270 2025-01-18 00:00:00+00:00    11.03  Brentwood Park   \n",
       "3     37.63757  122.43270 2025-01-19 00:00:00+00:00    11.56  Brentwood Park   \n",
       "4     37.63757  122.43270 2024-12-29 00:00:00+00:00     2.58  Brentwood Park   \n",
       "...        ...        ...                       ...      ...             ...   \n",
       "2064  37.66409  122.40165 2024-11-19 00:00:00+00:00     4.77   Gardiner Park   \n",
       "2065  37.66409  122.40165 2025-01-13 00:00:00+00:00     4.91   Gardiner Park   \n",
       "2066  37.66409  122.40165 2024-11-22 00:00:00+00:00     1.91   Gardiner Park   \n",
       "2067  37.66409  122.40165 2024-12-18 00:00:00+00:00    12.96   Gardiner Park   \n",
       "2068  37.66409  122.40165 2025-04-01 00:00:00+00:00     3.90   Gardiner Park   \n",
       "\n",
       "      month        day month_cat  threshold  \n",
       "0         1     Friday         1      False  \n",
       "1        12     Friday        12      False  \n",
       "2         1   Saturday         1      False  \n",
       "3         1     Sunday         1      False  \n",
       "4        12     Sunday        12      False  \n",
       "...     ...        ...       ...        ...  \n",
       "2064     11    Tuesday        11      False  \n",
       "2065      1     Monday         1      False  \n",
       "2066     11     Friday        11      False  \n",
       "2067     12  Wednesday        12      False  \n",
       "2068      4    Tuesday         4      False  \n",
       "\n",
       "[2069 rows x 9 columns]"
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clarity = pd.read_csv(\"/Users/laurenhe/Downloads/capstone/risesouthcity_april_daily.csv\")\n",
    "clarity_cleaned = clarity[['locationLatitude', 'locationLongitude', 'startOfPeriod', 'pm2_5ConcMass24HourMean.value', \"Name\"]]\n",
    "clarity_cleaned = clarity_cleaned.rename(columns= {\n",
    "    'locationLatitude': 'Latitude',\n",
    "    'locationLongitude': 'Longitude',\n",
    "    'startOfPeriod': 'datetime',\n",
    "    'pm2_5ConcMass24HourMean.value': 'pm_conc'\n",
    "})\n",
    "clarity_cleaned['Longitude'] = clarity_cleaned['Longitude'].abs()\n",
    "clarity_cleaned['Latitude'] = clarity_cleaned['Latitude'].abs()\n",
    "clarity_cleaned['datetime'] = pd.to_datetime(clarity_cleaned['datetime'])\n",
    "clarity_cleaned['month'] = clarity_cleaned['datetime'].dt.month\n",
    "clarity_cleaned['day'] = clarity_cleaned['datetime'].dt.day_name()\n",
    "clarity_cleaned['month_cat'] = pd.Categorical(\n",
    "    clarity_cleaned[\"month\"],\n",
    "    categories=[10, 11, 12, 1, 2, 3, 4],\n",
    "    ordered=True\n",
    ")\n",
    "clarity_cleaned['threshold'] = clarity_cleaned['pm_conc'] >= 35\n",
    "clarity_cleaned"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "9e504e03-5d4b-4b14-8e00-a1bd792a3e47",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Latitude</th>\n",
       "      <th>Longitude</th>\n",
       "      <th>datetime</th>\n",
       "      <th>pm_conc</th>\n",
       "      <th>Name</th>\n",
       "      <th>month</th>\n",
       "      <th>day</th>\n",
       "      <th>month_cat</th>\n",
       "      <th>threshold</th>\n",
       "      <th>Census_Tract</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>37.63757</td>\n",
       "      <td>122.43270</td>\n",
       "      <td>2025-01-17 00:00:00+00:00</td>\n",
       "      <td>16.29</td>\n",
       "      <td>Brentwood Park</td>\n",
       "      <td>1</td>\n",
       "      <td>Friday</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>6081602400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>37.63757</td>\n",
       "      <td>122.43270</td>\n",
       "      <td>2024-12-20 00:00:00+00:00</td>\n",
       "      <td>24.40</td>\n",
       "      <td>Brentwood Park</td>\n",
       "      <td>12</td>\n",
       "      <td>Friday</td>\n",
       "      <td>12</td>\n",
       "      <td>False</td>\n",
       "      <td>6081602400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>37.63757</td>\n",
       "      <td>122.43270</td>\n",
       "      <td>2025-01-18 00:00:00+00:00</td>\n",
       "      <td>11.03</td>\n",
       "      <td>Brentwood Park</td>\n",
       "      <td>1</td>\n",
       "      <td>Saturday</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>6081602400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>37.63757</td>\n",
       "      <td>122.43270</td>\n",
       "      <td>2025-01-19 00:00:00+00:00</td>\n",
       "      <td>11.56</td>\n",
       "      <td>Brentwood Park</td>\n",
       "      <td>1</td>\n",
       "      <td>Sunday</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>6081602400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>37.63757</td>\n",
       "      <td>122.43270</td>\n",
       "      <td>2024-12-29 00:00:00+00:00</td>\n",
       "      <td>2.58</td>\n",
       "      <td>Brentwood Park</td>\n",
       "      <td>12</td>\n",
       "      <td>Sunday</td>\n",
       "      <td>12</td>\n",
       "      <td>False</td>\n",
       "      <td>6081602400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2064</th>\n",
       "      <td>37.66409</td>\n",
       "      <td>122.40165</td>\n",
       "      <td>2024-11-19 00:00:00+00:00</td>\n",
       "      <td>4.77</td>\n",
       "      <td>Gardiner Park</td>\n",
       "      <td>11</td>\n",
       "      <td>Tuesday</td>\n",
       "      <td>11</td>\n",
       "      <td>False</td>\n",
       "      <td>6081602100</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2065</th>\n",
       "      <td>37.66409</td>\n",
       "      <td>122.40165</td>\n",
       "      <td>2025-01-13 00:00:00+00:00</td>\n",
       "      <td>4.91</td>\n",
       "      <td>Gardiner Park</td>\n",
       "      <td>1</td>\n",
       "      <td>Monday</td>\n",
       "      <td>1</td>\n",
       "      <td>False</td>\n",
       "      <td>6081602100</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2066</th>\n",
       "      <td>37.66409</td>\n",
       "      <td>122.40165</td>\n",
       "      <td>2024-11-22 00:00:00+00:00</td>\n",
       "      <td>1.91</td>\n",
       "      <td>Gardiner Park</td>\n",
       "      <td>11</td>\n",
       "      <td>Friday</td>\n",
       "      <td>11</td>\n",
       "      <td>False</td>\n",
       "      <td>6081602100</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2067</th>\n",
       "      <td>37.66409</td>\n",
       "      <td>122.40165</td>\n",
       "      <td>2024-12-18 00:00:00+00:00</td>\n",
       "      <td>12.96</td>\n",
       "      <td>Gardiner Park</td>\n",
       "      <td>12</td>\n",
       "      <td>Wednesday</td>\n",
       "      <td>12</td>\n",
       "      <td>False</td>\n",
       "      <td>6081602100</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2068</th>\n",
       "      <td>37.66409</td>\n",
       "      <td>122.40165</td>\n",
       "      <td>2025-04-01 00:00:00+00:00</td>\n",
       "      <td>3.90</td>\n",
       "      <td>Gardiner Park</td>\n",
       "      <td>4</td>\n",
       "      <td>Tuesday</td>\n",
       "      <td>4</td>\n",
       "      <td>False</td>\n",
       "      <td>6081602100</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2069 rows × 10 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      Latitude  Longitude                  datetime  pm_conc            Name  \\\n",
       "0     37.63757  122.43270 2025-01-17 00:00:00+00:00    16.29  Brentwood Park   \n",
       "1     37.63757  122.43270 2024-12-20 00:00:00+00:00    24.40  Brentwood Park   \n",
       "2     37.63757  122.43270 2025-01-18 00:00:00+00:00    11.03  Brentwood Park   \n",
       "3     37.63757  122.43270 2025-01-19 00:00:00+00:00    11.56  Brentwood Park   \n",
       "4     37.63757  122.43270 2024-12-29 00:00:00+00:00     2.58  Brentwood Park   \n",
       "...        ...        ...                       ...      ...             ...   \n",
       "2064  37.66409  122.40165 2024-11-19 00:00:00+00:00     4.77   Gardiner Park   \n",
       "2065  37.66409  122.40165 2025-01-13 00:00:00+00:00     4.91   Gardiner Park   \n",
       "2066  37.66409  122.40165 2024-11-22 00:00:00+00:00     1.91   Gardiner Park   \n",
       "2067  37.66409  122.40165 2024-12-18 00:00:00+00:00    12.96   Gardiner Park   \n",
       "2068  37.66409  122.40165 2025-04-01 00:00:00+00:00     3.90   Gardiner Park   \n",
       "\n",
       "      month        day month_cat  threshold  Census_Tract  \n",
       "0         1     Friday         1      False    6081602400  \n",
       "1        12     Friday        12      False    6081602400  \n",
       "2         1   Saturday         1      False    6081602400  \n",
       "3         1     Sunday         1      False    6081602400  \n",
       "4        12     Sunday        12      False    6081602400  \n",
       "...     ...        ...       ...        ...           ...  \n",
       "2064     11    Tuesday        11      False    6081602100  \n",
       "2065      1     Monday         1      False    6081602100  \n",
       "2066     11     Friday        11      False    6081602100  \n",
       "2067     12  Wednesday        12      False    6081602100  \n",
       "2068      4    Tuesday         4      False    6081602100  \n",
       "\n",
       "[2069 rows x 10 columns]"
      ]
     },
     "execution_count": 106,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "census_tracts = [\n",
    "    (\"06081601603\", \"Clay Ave Park\"),\n",
    "    (\"06081601800\", \"Buri Buri Park\"),\n",
    "    (\"06081602201\", \"Evelin Pacheco Home\"),\n",
    "    (\"06081602202\", \"Rise South City Office\"),\n",
    "    (\"06081602100\", \"Cypress and Pine Playlot\"),\n",
    "  #  (\"06081602100\", \"Marita Santos Home\"),\n",
    "    (\"06081602202\", \"Marita Santos Home\"),\n",
    "  #  (\"06081602100\", \"Nora Alvarado Home\"),\n",
    "    (\"06081602202\", \"Nora Alvarado Home\"),\n",
    "    (\"06081602100\", \"Gardiner Park\"),\n",
    "    (\"06081602400\", \"Brentwood Park\"),\n",
    "    (\"06081603700\", \"Rollingwood Elementary\"),\n",
    "    (\"06081614000\", \"Portola Elementary\"),\n",
    "    (\"06081604000\", \"San Bruno School District Office\"),\n",
    "    (\"06081604200\", \"Belle Air School\"),\n",
    "    (\"06081603900\", \"Parkside Middle\")\n",
    "]\n",
    "df_census = pd.DataFrame(census_tracts, columns=[\"Census_Tract\", \"Name\"])\n",
    "df_census['Census_Tract'] = df_census['Census_Tract'].astype(int)\n",
    "clarity_cleaned = pd.merge(clarity_cleaned, df_census,\n",
    "    on = [\"Name\"], \n",
    "    how = \"left\")\n",
    "clarity_cleaned"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "888b6e6e-df11-43a3-a18a-6efa3402e20f",
   "metadata": {},
   "outputs": [],
   "source": [
    "asthma_all = pd.read_csv(\"/Users/laurenhe/Downloads/capstone/asthma_data.csv\") \n",
    "asthma_all = asthma_all.rename(columns={\n",
    "    'Indicator Rate Value': 'asthma_rate',\n",
    "    'Period of Measure': 'year',\n",
    "    'Location': 'Census_Tract'\n",
    "})\n",
    "clarity_cleaned = clarity_cleaned.merge(asthma_all,\n",
    "                                       on = ['Census_Tract'], how = 'left')\n",
    "yr2024 = clarity_cleaned[(clarity_cleaned['datetime'] < '2025-01-01 00:00:00+00:00') & (clarity_cleaned['datetime'] >= '2024-11-01 00:00:00+00:00')]\n",
    "yr2025 = clarity_cleaned[(clarity_cleaned['datetime'] >= '2025-01-01 00:00:00+00:00') & (clarity_cleaned['datetime'] < '2025-04-01 00:00:00+00:00')]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "8988eade-b6ec-44ee-ac1c-6f8124ef909d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hovertemplate": "Name=Belle Air School<br>month=%{x}<br>pm_conc=%{y}<extra></extra>",
         "legendgroup": "Belle Air School",
         "marker": {
          "color": "#636efa",
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Belle Air School",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          11,
          12
         ],
         "xaxis": "x",
         "y": [
          5.074,
          10.446774193548388
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Name=Brentwood Park<br>month=%{x}<br>pm_conc=%{y}<extra></extra>",
         "legendgroup": "Brentwood Park",
         "marker": {
          "color": "#EF553B",
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Brentwood Park",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          11,
          12
         ],
         "xaxis": "x",
         "y": [
          4.289444444444444,
          11.355806451612903
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Name=Buri Buri Park<br>month=%{x}<br>pm_conc=%{y}<extra></extra>",
         "legendgroup": "Buri Buri Park",
         "marker": {
          "color": "#00cc96",
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Buri Buri Park",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          11,
          12
         ],
         "xaxis": "x",
         "y": [
          4.654444444444445,
          11.243548387096775
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Name=Clay Ave Park<br>month=%{x}<br>pm_conc=%{y}<extra></extra>",
         "legendgroup": "Clay Ave Park",
         "marker": {
          "color": "#ab63fa",
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Clay Ave Park",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          11,
          12
         ],
         "xaxis": "x",
         "y": [
          4.252777777777778,
          8.184516129032259
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Name=Cypress and Pine Playlot<br>month=%{x}<br>pm_conc=%{y}<extra></extra>",
         "legendgroup": "Cypress and Pine Playlot",
         "marker": {
          "color": "#FFA15A",
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Cypress and Pine Playlot",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          11,
          12
         ],
         "xaxis": "x",
         "y": [
          7.138333333333334,
          14.46225806451613
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Name=Evelin Pacheco Home<br>month=%{x}<br>pm_conc=%{y}<extra></extra>",
         "legendgroup": "Evelin Pacheco Home",
         "marker": {
          "color": "#19d3f3",
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Evelin Pacheco Home",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          11,
          12
         ],
         "xaxis": "x",
         "y": [
          5.42,
          10.958709677419353
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Name=Gardiner Park<br>month=%{x}<br>pm_conc=%{y}<extra></extra>",
         "legendgroup": "Gardiner Park",
         "marker": {
          "color": "#FF6692",
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Gardiner Park",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          11,
          12
         ],
         "xaxis": "x",
         "y": [
          4.5216666666666665,
          11.296774193548387
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Name=Marita Santos Home<br>month=%{x}<br>pm_conc=%{y}<extra></extra>",
         "legendgroup": "Marita Santos Home",
         "marker": {
          "color": "#B6E880",
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Marita Santos Home",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          11,
          12
         ],
         "xaxis": "x",
         "y": [
          5.625,
          12.026129032258064
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Name=Nora Alvarado Home<br>month=%{x}<br>pm_conc=%{y}<extra></extra>",
         "legendgroup": "Nora Alvarado Home",
         "marker": {
          "color": "#FF97FF",
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Nora Alvarado Home",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          11,
          12
         ],
         "xaxis": "x",
         "y": [
          5.37,
          11.77741935483871
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Name=Parkside Middle<br>month=%{x}<br>pm_conc=%{y}<extra></extra>",
         "legendgroup": "Parkside Middle",
         "marker": {
          "color": "#FECB52",
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Parkside Middle",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          11,
          12
         ],
         "xaxis": "x",
         "y": [
          5.101,
          9.751612903225807
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Name=Portola Elementary<br>month=%{x}<br>pm_conc=%{y}<extra></extra>",
         "legendgroup": "Portola Elementary",
         "marker": {
          "color": "#636efa",
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Portola Elementary",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          11,
          12
         ],
         "xaxis": "x",
         "y": [
          5.012,
          10.11483870967742
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Name=Rise South City Office<br>month=%{x}<br>pm_conc=%{y}<extra></extra>",
         "legendgroup": "Rise South City Office",
         "marker": {
          "color": "#EF553B",
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Rise South City Office",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          11,
          12
         ],
         "xaxis": "x",
         "y": [
          7.913,
          14.170322580645163
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Name=Rollingwood Elementary<br>month=%{x}<br>pm_conc=%{y}<extra></extra>",
         "legendgroup": "Rollingwood Elementary",
         "marker": {
          "color": "#00cc96",
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Rollingwood Elementary",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          11,
          12
         ],
         "xaxis": "x",
         "y": [
          4.631,
          9.86
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "Name=San Bruno School District Office<br>month=%{x}<br>pm_conc=%{y}<extra></extra>",
         "legendgroup": "San Bruno School District Office",
         "marker": {
          "color": "#ab63fa",
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "San Bruno School District Office",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          11,
          12
         ],
         "xaxis": "x",
         "y": [
          5.799666666666667,
          12.273225806451613
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "autosize": true,
        "legend": {
         "title": {
          "text": "Name"
         },
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "xaxis": {
         "anchor": "y",
         "autorange": true,
         "domain": [
          0,
          1
         ],
         "range": [
          10.938382074785393,
          12.061617925214607
         ],
         "title": {
          "text": "month"
         },
         "type": "linear"
        },
        "yaxis": {
         "anchor": "x",
         "autorange": true,
         "domain": [
          0,
          1
         ],
         "range": [
          3.4622799603006618,
          15.252755881993245
         ],
         "title": {
          "text": "pm_conc"
         },
         "type": "linear"
        }
       }
      },
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABF4AAAFoCAYAAABuXz/oAAAAAXNSR0IArs4c6QAAIABJREFUeF7snWdgVFW7hVcqoYTQexGQJh0BBaQISBOlSO9FIdKrdGnSkd6R3nuV3gSlCFIEKQoiSC+hpSeT3Ls334wJCSThzJA3M+v8uZI5e593P+uE787DLk7h4eHh4EUCJEACJEACJEACJEACJEACJEACJEACJGB1Ak4UL1Znyg5JgARIgARIgARIgARIgARIgARIgARIQBOgeOGLQAIkQAIkQAIkQAIkQAIkQAIkQAIkQAI2IkDxYiOw7JYESIAESIAESIAESIAESIAESIAESIAEKF74DpAACZAACZAACZAACZAACZAACZAACZCAjQhQvNgILLslARIgARIgARIgARIgARIgARIgARIgAYoXvgMkQAIkQAIkQAIkQAIkQAIkQAIkQAIkYCMCFC82AstuSYAESIAESIAESIAESIAESIAESIAESIDihe8ACZAACZAACZAACZAACZAACZAACZAACdiIAMWLjcCyWxIgARIgARIgARIgARIgARIgARIgARKgeOE7QAIkQAIkQAIkQAIkQAIkQAIkQAIkQAI2IkDxYiOw7JYESIAESIAESIAESIAESIAESIAESIAEKF74DpAACZAACZAACZAACZAACZAACZAACZCAjQhQvNgILLslARIgARIgARIgARIgARIgARIgARIgAYoXvgMkQAIkQAIkQAIkQAIkQAIkQAIkQAIkYCMCFC82AstuSYAESIAESIAESIAESIAESIAESIAESIDihe8ACZAACZAACZAACZAACZAACZAACZAACdiIAMWLjcCyWxIgARIgARIgARIgARIgARIgARIgARKgeOE7QAIkQAIkQAIkQAIkQAIkQAIkQAIkQAI2IkDxYiOw7JYESIAESIAESIAESIAESIAESIAESIAEKF74DpAACZAACZAACZAACZAACZAACZAACZCAjQhQvNgILLslARIgARIgARIgARIgARIgARIgARIgAYoXvgMkQAIkQAIkQAIkQAIkQAIkQAIkQAIkYCMCFC82AstuSYAESIAESIAESIAESIAESIAESIAESIDihe8ACZAACZAACZAACZAACZAACZAACZAACdiIAMWLjcCyWxIgARIgARIgARIgARIgARIgARIgARKgeOE7QAIkQAIkQAIkQAIkQAIkQAIkQAIkQAI2IkDxYiOw7JYESIAESIAESIAESIAESIAESIAESIAEKF74DpAACZAACZAACZAACZAACZAACZAACZCAjQhQvNgILLslARIgARIgARIgARIgARIgARIgARIgAYoXvgMkQAIkQAIkQAIkQAIkQAIkQAIkQAIkYCMCFC82AstuSYAESIAESIAESIAESIAESIAESIAESIDihe8ACZAACZAACZAACZAACZAACZAACZAACdiIAMWLjcCyWxIgARIgARIgARIgARIgARIgARIgARKgeOE7QAIkQAIkQAIkQAIkQAIkQAIkQAIkQAI2IkDxYiOw7JYESIAESIAESIAESIAESIAESIAESIAEKF74DpAACZAACZAACZAACZAACZAACZAACZCAjQhQvNgILLslARIgARIgARIgARIgARIgARIgARIgAYoXvgMkQAIkQAIkQAIkQAIkQAIkQAIkQAIkYCMCFC82AstuSYAESIAESIAESIAESIAESIAESIAESIDihe8ACZAACZAACZAACZAACZAACZAACZAACdiIAMWLjcCyWxIgARIgARIgARIgARIgARIgARIgARKgeOE7QAIkQAIkQAIkQAIkQAIkQAIkQAIkQAI2IkDxYiOw7JYESIAESIAESIAESIAESIAESIAESIAEKF74DpAACZAACZAACZAACZAACZAACZAACZCAjQhQvNgILLslARIgARIgARIgARIgARIgARIgARIgAYoXvgMkQAIkQAIkQAIkQAIkQAIkQAIkQAIkYCMCFC82AstuSYAESIAESIAESIAESIAESIAESIAESIDihe8ACZAACZAACZAACZAACZAACZAACZAACdiIAMWLjcCyWxIgARIgARIgARIgARIgARIgARIgARKgeOE7QAIkQAIkQAIkQAIkQAIkQAIkQAIkQAI2IkDxYiOw7JYESIAESIAESIAESIAESIAESIAESIAEKF74DpAACZAACZAACZAACZAACZAACZAACZCAjQhQvNgILLslARIgARIgARIgARIgARIgARIgARIgAYoXvgMkQAIkQAIkQAIkQAIkQAIkQAIkQAIkYCMCFC82AstuSYAESIAESIAESIAESIAESIAESIAESIDihe8ACZAACZAACZAACZAACZAACZAACZAACdiIAMWLjcCyWxIg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0DDsPnhSXiftt3aKvC3A3u7dD79s+iKQUL3je1fE3zB26OuDTi3qyltHrtz4B406jZC/QPfq1Ai2trYSlquLEzzT8IwXS35ztHxnrPDdDXFmhzhkOXrjViNLfivejz0sLBzh4eEYN2u1/DNkVP/2sLOzg62tWNsExPcOicOWfeatw7SR3eVhqS9fv0W1Jv3kVsVu7RrgwpVb8jB472/byC1qbJZLICQ0TB6uW7vlIOxc4yOvkzbItYT+PBKr5bJmTocBXs0kACGCc+fIDJ/hXnB1dsLM7zfi4LGzcqUUf2ax3Hckrsjj+47hzx/6qzczIgFrJUDxorPKix9exJL/qG3HqonInSNL5JkLUT/7smY5TBrWRWcUmI4gYPjFN656x/euiPM6ytXvgeF92qDFV9UgVs2Iv5WO3vj+WP67puU7Qxx46bv9EE7tWkjxYvmvQpwZ+G47iNHTV773+dhBHdGobkX57+J7h8Qvyz2HzcLmpWNRMO8H8vnjpy+i94g5eBsQKP9ZCJfBPVvyF2oLf4c+qeMVWVORijh4XRyAmpg/jxp2HC5/Tpk+qod8/tK121iwaqsUu64uzij9UUG57ahY4TwWTonhx0Ygvu8Y/vzBd4YESEAvBChe9FJJ5kECJEACJEACFkJArJIR21I806SWv1izkUBsBMS2I7HKKo17KgIiARIgARIgAYsmQPFi0eVj8CRAAiRAAiRAAiRAAiRAAiRAAiRAAioToHhRuTqMjQRIgARIgARIgARIgARIgARIgARIwKIJULxYdPkYPAmQAAmQAAmQAAmQAAmQAAmQAAmQgMoEKF5Urg5jIwESIAESIAESIAESIAESIAESIAESsGgCFC8WXT4GTwIkQAIkQAIkQAIkQAIkQAIkQAIkoDIBiheVq8PYSIAESIAESIAESIAESIAESIAESIAELJoAxYtFl4/BkwAJkAAJkAAJkAAJkAAJkAAJkAAJqEyA4kXl6jA2EiABEiABEiABEiABEiABEiABEiABiyZA8WLR5WPwJEACJEACJEACJEACJEACJEACJEACKhOgeFG5OoyNBEiABEiABEiABEiABEiABEiABEjAoglQvFh0+Rg8CZAACZAACZAACZAACZAACZAACZCAygQoXlSuDmMjARIgARIgARIgARIgARIgARIgARKwaAIULxZdPgZPAiRAAiRAAiRAAiRAAiRAAiRAAiSgMgGKF5Wrw9hIgARIgARIgARIgARIgARIgARIgAQsmgDFi0WXj8GTAAmQAAmQAAmQAAmQAAmQAAmQAAmoTIDiReXqMDYSIAESIAHdEggIDEbHfj7o2aEhyn9SVLd5MjESIAESIAESIAESsHYCFC/W/gYwfxIgARIggWQnMH/lVqzbsg9HfpoTOder12/xab3umDKiG+pWK5vsMXACEiABEiABEiABEiAB8xCgeDEPd85KAiRAAiRgRQTmLd+C9VsPULxYUc2ZKgmQAAmQAAmQAAkYCFC88F0gARIgARKwCgI/bj2A47//hU8//hBrN+/D/UfPUK1CKQzt1Qo/bN6HrbuPIiQ0FC0bVkerRjXg4uwouYSEhGLBqq34ed9vuHv/McqWLIz+Xs1QpGAu+fkff93AlPnrZT/f7Qdx8crfqFKuBNo1rS2fOXLiTwyb+D2e+b9CyaL5ZZ/6NcuhTtWycsVLjw4NcfP2v/jl+B8olC8H2jSuiZqVSltFTZgkCZAACZAACZAACVgDAYoXa6gycyQBEiABEsD0Rb5Yum4nsmfJgMb1KiE4OARiC5BoeXNmxVd1Psdz/9dYtn4nZo3theoVPpafjZq6Aht2HJJ9CufPiVUb/HD77kPsXjsZH2TNKMWK1+Dp8tm2TWrJf7fSdzc83FPjx0UjceP2v/CZuxa/nrqA4X3ayOeEYMmXK5sUL6J9Ue1TlCyWH78cP4cjJ87j+I75cE/tyqqRAAmQAAmQAAmQAAnogADFiw6KyBRIgARIgAQSJiDEy5ZdR7D3x2lwdnq3msVr8DT8++ApNi0ZAwcHe/nvmnUdjQ8L5sLIfu3w6Ik/qjTug47N66K/V1P5uf+L1yjfoCdaNaqOYb1bR4oXMYYQKqLtP3IGvUfMxsGNM5ExvQfi22rk/W0btGxYTfYTq2IqfNUL00f1QK3KnyScFJ8gARIgARIgARIgARJQngDFi/IlYoAkQAIkQAKmICDEi9+hU/BbNyVyuOE+S3Ht5l25MsXQennPkluOFvr0x4mzl9Cxrw8W+vRDhbLFI59p3HkkXJydsHrOsEjxss93OrJkTCufOX/5Fpp7jcb6hSNRrFDueMVL9MN1i1Ruj4Hdm6N909qmSJtjkAAJkAAJkAAJkAAJmJkAxYuZC8DpSYAESIAEUoZAbOJl5NTluHztznviRaxUEduQhHgR237EqhghWEoVKxAZaPs+kxAUHIJ180fEKl4uXbsNIWcoXlKmtpyFBEiABEiABEiABFQmQPGicnUYGwmQAAmQgMkIJEW8iLNc6rYejJ4dG6Jb2wYyloDAYJSu3QUNapXHhKGdEyVelqz9GYtWb8epXQsj84nrOmmueDFZyTkQCZAACZAACZAACShBgOJFiTIwCBIgARIggeQmkBTxImL6ZsAUXLl+B706NkLBfDmw0tcPfodOYs1cb3lLkeFw3ahbjaKvePnzrxto0X0sxg3uhA8L5IKNjY3cliQO1+VWo+SuPMcnARIgARIgARIgAfMSoHgxL3/OTgIkQAIkkEIEZizegN0HT753xou4sUhIkqhnvPT5bq7cRrRgUl8ZmThgd8j4RfK8F0MTAqVhnQryHw3iZf+G6cic4d0ZLwbxIsYtWjA3wsLC4e2zBNv3HJOfe7Wtjw7N6qDsF91iFS+DerRAuya1UogMpyEBEiABEiABEiABEkhOAhQvyUmXY5MACZAACeiGgLjN6OXrN8iaOT3s7eySlNfbgEC8DQhCOk93ueqFjQRIgARIgARIgARIQP8EKF70X2NmSAIkQAIkQAIkQAIkQAIkQAIkQAIkYCYCFC9mAs9pSYAESIAESIAESIAESIAESIAESIAE9E+A4kX/NWaGJEACJEACJEACJEACJEACJEACJEACZiJA8WIm8JyWBEiABEiABEiABEiABEiABEiABEhA/wQoXvRfY2ZIAiRAAiRAAiRAAiRAAiRAAiRAAiRgJgIUL2YCz2lJgARIgARIgARIgARIgARIgARIgAT0T4DiRf81ZoYkQAIkQAIkQAIkQAIkQAIkQAIkQAJmIkDxYibwnJYESIAESIAESIAESIAESIAESIAESED/BChe9F9jZkgCJEACJEACJEACJEACJEACJEACJGAmAhQvZgLPaUmABEiABEiABEiABEiABEiABEiABPRPgOJF/zVmhiRAAiRAAiRAAiRAAiRAAiRAAiRAAmYiQPFiJvCclgRIgARIgARIgARIgARIgARIgARIQP8EKF70X2NmSAIkQAIkQAIkQAIkQAIkQAIkQAIkYCYCFC9mAs9pSYAESIAESIAESIAESIAESIAESIAE9E+A4kX/NWaGJEACJEACJEACJEACJEACJEACJEACZiJA8WIm8JyWBEiABEiABEiABEiABEiABEiABEhA/wQoXvRfY2ZIAiRAAiRAAiRAAiRAAiRAAiRAAiRgJgIUL2YCz2lJgARIgARIgARIgARIgARIgARIgAT0T4DiRf81ZoYkQAIkQAIkQAIkQAIkQAIkQAIkQAJmIkDxYibwnJYESIAESIAESIAESIAESIAESIAESED/BChe9F9jZkgCJEACJEACJEACJEACJEACJEACJGAmAhQvZgLPaUmABEiABEiABEiABEiABEiABEiABPRPgOJF/zVmhiRAAiRAAiRAAiRAAiRAAiRAAiRAAmYiQPFiJvCclgRIgARIgARIgARIgARIgARIgARIQP8EKF70X2NmSAIkQAIkQAIkQAIkQAIkQAIkQAIkYCYCFC9mAs9pSYAESIAESIAESIAESIAESIAESIAE9E+A4kX/NWaGJEACJEACJEACJEACJEACJEACJEACZiJA8WIm8JyWBEiABEiABEiABEiABEiABEiABEhA/wQoXvRfY2ZIAiRAAiRAAiRAAiRAAiRAAiRAAiRgJgIUL2YCz2lJgARIgARIgARIgARIgARIgARIgAT0T4DiRf81ZoYkQAIkQAIkQAIkQAIkQAIkQAIkQAJmIkDxYibwnJYESIAESIAESIAESIAESIAESIAESED/BChe9F9jZkgCJEACJEACJEACJEACJEACJEACJGAmAhQvZgLPaUmABEiABEiABEiABEiABEiABEiABPRPgOJF/zVmhiRAAiRAAiRAAiRAAiRAAiRAAiRAAmYiQPFiJvCclgRIgARIgARIgARIgARIgARIgARIQP8EKF70X2NmSAIkQAIkQAIkQAIkQAIkQAIkQAIkYCYCFC9mAs9pSYAESIAESIAESIAESIAESIAESIAE9E+A4kX/NWaGJEACJEACJEACJEACJEACJEACJEACZiLwf0pyN9P1F8MGAAAAAElFTkSuQmCC",
      "text/html": [
       "<div>                            <div id=\"2ec427df-0008-4960-b77a-2441159c7a44\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"2ec427df-0008-4960-b77a-2441159c7a44\")) {                    Plotly.newPlot(                        \"2ec427df-0008-4960-b77a-2441159c7a44\",                        [{\"hovertemplate\":\"Name=Belle Air School\\u003cbr\\u003emonth=%{x}\\u003cbr\\u003epm_conc=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"Belle Air School\",\"marker\":{\"color\":\"#636efa\",\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Belle Air School\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[11,12],\"xaxis\":\"x\",\"y\":[5.074,10.446774193548388],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"Name=Brentwood Park\\u003cbr\\u003emonth=%{x}\\u003cbr\\u003epm_conc=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"Brentwood Park\",\"marker\":{\"color\":\"#EF553B\",\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Brentwood Park\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[11,12],\"xaxis\":\"x\",\"y\":[4.289444444444444,11.355806451612903],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"Name=Buri Buri Park\\u003cbr\\u003emonth=%{x}\\u003cbr\\u003epm_conc=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"Buri Buri Park\",\"marker\":{\"color\":\"#00cc96\",\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Buri Buri Park\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[11,12],\"xaxis\":\"x\",\"y\":[4.654444444444445,11.243548387096775],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"Name=Clay Ave Park\\u003cbr\\u003emonth=%{x}\\u003cbr\\u003epm_conc=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"Clay Ave Park\",\"marker\":{\"color\":\"#ab63fa\",\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Clay Ave Park\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[11,12],\"xaxis\":\"x\",\"y\":[4.252777777777778,8.184516129032259],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"Name=Cypress and Pine Playlot\\u003cbr\\u003emonth=%{x}\\u003cbr\\u003epm_conc=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"Cypress and Pine Playlot\",\"marker\":{\"color\":\"#FFA15A\",\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Cypress and Pine Playlot\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[11,12],\"xaxis\":\"x\",\"y\":[7.138333333333334,14.46225806451613],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"Name=Evelin Pacheco Home\\u003cbr\\u003emonth=%{x}\\u003cbr\\u003epm_conc=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"Evelin Pacheco Home\",\"marker\":{\"color\":\"#19d3f3\",\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Evelin Pacheco Home\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[11,12],\"xaxis\":\"x\",\"y\":[5.42,10.958709677419353],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"Name=Gardiner Park\\u003cbr\\u003emonth=%{x}\\u003cbr\\u003epm_conc=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"Gardiner Park\",\"marker\":{\"color\":\"#FF6692\",\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Gardiner Park\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[11,12],\"xaxis\":\"x\",\"y\":[4.5216666666666665,11.296774193548387],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"Name=Marita Santos Home\\u003cbr\\u003emonth=%{x}\\u003cbr\\u003epm_conc=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"Marita Santos Home\",\"marker\":{\"color\":\"#B6E880\",\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Marita Santos Home\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[11,12],\"xaxis\":\"x\",\"y\":[5.625,12.026129032258064],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"Name=Nora Alvarado Home\\u003cbr\\u003emonth=%{x}\\u003cbr\\u003epm_conc=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"Nora Alvarado Home\",\"marker\":{\"color\":\"#FF97FF\",\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Nora Alvarado Home\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[11,12],\"xaxis\":\"x\",\"y\":[5.37,11.77741935483871],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"Name=Parkside Middle\\u003cbr\\u003emonth=%{x}\\u003cbr\\u003epm_conc=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"Parkside Middle\",\"marker\":{\"color\":\"#FECB52\",\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Parkside Middle\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[11,12],\"xaxis\":\"x\",\"y\":[5.101,9.751612903225807],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"Name=Portola Elementary\\u003cbr\\u003emonth=%{x}\\u003cbr\\u003epm_conc=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"Portola Elementary\",\"marker\":{\"color\":\"#636efa\",\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Portola Elementary\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[11,12],\"xaxis\":\"x\",\"y\":[5.012,10.11483870967742],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"Name=Rise South City Office\\u003cbr\\u003emonth=%{x}\\u003cbr\\u003epm_conc=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"Rise South City Office\",\"marker\":{\"color\":\"#EF553B\",\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Rise South City Office\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[11,12],\"xaxis\":\"x\",\"y\":[7.913,14.170322580645163],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"Name=Rollingwood Elementary\\u003cbr\\u003emonth=%{x}\\u003cbr\\u003epm_conc=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"Rollingwood Elementary\",\"marker\":{\"color\":\"#00cc96\",\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Rollingwood Elementary\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[11,12],\"xaxis\":\"x\",\"y\":[4.631,9.86],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"Name=San Bruno School District Office\\u003cbr\\u003emonth=%{x}\\u003cbr\\u003epm_conc=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"San Bruno School District Office\",\"marker\":{\"color\":\"#ab63fa\",\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"San Bruno School District Office\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[11,12],\"xaxis\":\"x\",\"y\":[5.799666666666667,12.273225806451613],\"yaxis\":\"y\",\"type\":\"scatter\"}],                        {\"template\":{\"data\":{\"histogram2dcontour\":[{\"type\":\"histogram2dcontour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"choropleth\":[{\"type\":\"choropleth\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"histogram2d\":[{\"type\":\"histogram2d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmap\":[{\"type\":\"heatmap\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmapgl\":[{\"type\":\"heatmapgl\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"contourcarpet\":[{\"type\":\"contourcarpet\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"contour\":[{\"type\":\"contour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"surface\":[{\"type\":\"surface\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"mesh3d\":[{\"type\":\"mesh3d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"parcoords\":[{\"type\":\"parcoords\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolargl\":[{\"type\":\"scatterpolargl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"scattergeo\":[{\"type\":\"scattergeo\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolar\":[{\"type\":\"scatterpolar\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"scattergl\":[{\"type\":\"scattergl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatter3d\":[{\"type\":\"scatter3d\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattermapbox\":[{\"type\":\"scattermapbox\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterternary\":[{\"type\":\"scatterternary\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattercarpet\":[{\"type\":\"scattercarpet\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}]},\"layout\":{\"autotypenumbers\":\"strict\",\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"hovermode\":\"closest\",\"hoverlabel\":{\"align\":\"left\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"bgcolor\":\"#E5ECF6\",\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"ternary\":{\"bgcolor\":\"#E5ECF6\",\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]]},\"xaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"yaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"geo\":{\"bgcolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"subunitcolor\":\"white\",\"showland\":true,\"showlakes\":true,\"lakecolor\":\"white\"},\"title\":{\"x\":0.05},\"mapbox\":{\"style\":\"light\"}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"month\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"pm_conc\"}},\"legend\":{\"title\":{\"text\":\"Name\"},\"tracegroupgap\":0},\"margin\":{\"t\":60}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('2ec427df-0008-4960-b77a-2441159c7a44');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "graph = yr2024.groupby(['month', 'Name'])['pm_conc'].mean().reset_index()\n",
    "\n",
    "px.scatter(graph, x = 'month', y = 'pm_conc', color = 'Name')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "c03f68bc-8323-4e04-b529-d157b62bcba2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hovertemplate": "month_cat_first=11<br>pm_conc_mean=%{x}<br>asthma_rate_first=%{y}<br>pm_conc_std=%{marker.size}<extra></extra>",
         "legendgroup": "11",
         "marker": {
          "color": "#636efa",
          "size": [
           2.56295315194414,
           2.2531238544785936,
           2.1841878706242905,
           2.5088056721518153,
           2.8085508478873122,
           2.692928158894239,
           2.290457120363688,
           3.0413208904390028,
           2.8159214820558205,
           2.350662265670745,
           2.486085303087604,
           3.0264468184370243,
           2.380067324635726,
           2.7560896374184667
          ],
          "sizemode": "area",
          "sizeref": 0.021015160170439987,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "11",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          5.074,
          4.289444444444444,
          4.654444444444445,
          4.252777777777778,
          7.138333333333334,
          5.42,
          4.5216666666666665,
          5.625,
          5.37,
          5.101,
          5.012,
          7.913,
          4.631,
          5.799666666666667
         ],
         "xaxis": "x",
         "y": [
          8.1,
          8.1,
          7.9,
          6.2,
          8.6,
          9.2,
          8.6,
          9.1,
          9.1,
          8,
          7.2,
          9.1,
          7.6,
          8.2
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "month_cat_first=12<br>pm_conc_mean=%{x}<br>asthma_rate_first=%{y}<br>pm_conc_std=%{marker.size}<extra></extra>",
         "legendgroup": "12",
         "marker": {
          "color": "#EF553B",
          "size": [
           6.939570511007995,
           8.26435852987682,
           7.558531581256461,
           7.609356203606979,
           7.975611245425961,
           7.2963423448261535,
           7.9290978946350705,
           8.225558006368262,
           8.406064068175995,
           6.865905364375458,
           7.441130373810843,
           8.216440625912158,
           7.400116706696409,
           8.175230004745956
          ],
          "sizemode": "area",
          "sizeref": 0.021015160170439987,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "12",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          10.446774193548388,
          11.355806451612903,
          11.243548387096775,
          8.184516129032259,
          14.46225806451613,
          10.958709677419353,
          11.296774193548387,
          12.026129032258064,
          11.77741935483871,
          9.751612903225807,
          10.11483870967742,
          14.170322580645163,
          9.86,
          12.273225806451613
         ],
         "xaxis": "x",
         "y": [
          8.1,
          8.1,
          7.9,
          6.2,
          8.6,
          9.2,
          8.6,
          9.1,
          9.1,
          8,
          7.2,
          9.1,
          7.6,
          8.2
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "autosize": true,
        "legend": {
         "itemsizing": "constant",
         "title": {
          "text": "month_cat_first"
         },
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "xaxis": {
         "anchor": "y",
         "autorange": true,
         "domain": [
          0,
          1
         ],
         "range": [
          3.554834288862798,
          15.248868532135527
         ],
         "title": {
          "text": "pm_conc_mean"
         },
         "type": "linear"
        },
        "yaxis": {
         "anchor": "x",
         "autorange": true,
         "domain": [
          0,
          1
         ],
         "range": [
          5.735562368832968,
          9.658861938959106
         ],
         "title": {
          "text": "asthma_rate_first"
         },
         "type": "linear"
        }
       }
      },
      "image/png": "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Rulg5bkbERB7t4jNdY8Zfpm9X5B4nXTDLyfEGybFJuHizWw7bNdxw1Xt25byexrvopQINPU9bPMBuNQoJaQ8iQRcQ4DixTVRZNcIxUt2/Hj11gnM/vx7nD/xXtTU1tknCOEy4dzh/ADJGyYnBH6c/zseeGIaxEbOBdEI9turu73saI9dd8jJ+BzEfwSef/V9XHvn45tM/PrLxmBg38Ps/zbz43kQG+o2HFddeCqGnUCR7L87JfMZ799n7IafiWKUVi2LMeuVe+0BhUxevGzlFoMLQSOWiPAggeYINPc9bOPrKV6ao8k/JwF3EaB4cVce7IYEXEdAvLpQPFZdWlJk/+WYBwnkmoBYdiSeThCbBfIgAacJiN8o/7lyDdq1brlhyZHTNTk+CZAACZAACZCAvwlQvPg7f86eBEiABEiABEiABEiABEiABEiABEjAQQIULw7C5dAkQAIkQAIkQAIkQAIkQAIkQAIkQAL+JkDx4u/8OXsSIAESIAESIAESIAESIAESIAESIAEHCVC8OAiXQ5MACZAACZAACZAACZAACZAACZAACfibAMWLv/Pn7EmABEiABEiABEiABEiABEiABEiABBwkQPHiIFwOTQIkQAIkQAIkQAIkQAIkQAIkQAIk4G8CFC/+zp+zJwESIAESIAESIAESIAESIAESIAEScJAAxYuDcDk0CZAACZAACZAACZAACZAACZAACZCAvwlQvPg7f86eBEiABEiABEiABEiABEiABEiABEjAQQIULw7C5dAkQAIkQAIkQAIkQAIkQAIkQAIkQAL+JkDx4u/8OXsSIAESIAESIAESIAESIAESIAESIAEHCVC8OAiXQ5MACZAACZAACZAACZAACZAACZAACfibAMWLv/Pn7EmABEiABEiABEiABEiABEiABEiABBwkQPHiIFwOTQIkQAIkQAIkQAIkQAIkQAIkQAIk4G8CFC/+zp+zJwESIAESIAESIAESIAESIAESIAEScJAAxYuDcDk0CZAACZAACZAACZAACZAACZAACZCAvwlQvPg7f86eBEiABEiABEiABEiABEiABEiABEjAQQIULw7C5dAkQAIkQAIkQAIkQAIkQAIkQAIkQAL+JkDx4u/8OXsSIAESIAEHCPxn2kx8/Pl32G/P7pj6+odY8PtS9DxkH1x9ySi0aVViV5x466NoXdoC9fVxvPbu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wT/vfWpDbfHWoOsvOw2H7P8XrFhVhstvfBBiv5eG44YJp9lvXxJHw9MoG29y27DUSDzh8pfuXe2NgB984lX7tdQNh/jvd117Djp1aNNslFur8caMT3HZ9ZMx983J9puNxLHxUiPx7+WV1fZbi55/9f0NNQRjsfyoT88DseTPVfZmul9++4v95+LNR5ZpbVh6VVVday+T2nyzYrHHi9ivRogpHiRAAiRAAiRAAiSQawIUL7kmyvFIgARIgAR8T6BhqdH0p26xn8oQm8FGI6G8c1m1ptyuKV5FLZbibHyItxlVVFXboiRgGBn1JpYvrVi1FoWF0by+illsortyVRkikZC9bGvzY9ny1fZTMEI48SABEiABEiABEiAB2QQoXmQnwPokQAIkQAKeI7C1PV6ynaTYnPfS6yc3OYx4omXSdedmWyrj68Xrn8VTKk0d5582EKeedHTGNXghCZAACZAACZAACahGgOJFtcTYLwmQAAmQgOsJCPkw+/PvcO+NF+SsV/F0SX080eR4YmPbcCiYs5rpDhSPJ5AwrSYvCwaNjJ+wSbcfnk8CJEACJEACJEACbiBA8eKGFNgDCZAACZAACZAACZAACZAACZAACZCAJwlQvHgyVk6KBEiABEiABEiABEiABEiABEiABEjADQQoXtyQAnsgARIgARIgARIgARIgARIgARIgARLwJAGKF0/GykmRAAmQAAmQAAmQAAmQAAmQAAmQAAm4gQDFixtSYA8kQAIkQAIkQAIkQAIkQAIkQAIkQAKeJEDx4slYOSkSIAESIAESIAESIAESIAESIAESIAE3EKB4cUMK7IEESIAESIAESIAESIAESIAESIAESMCTBChePBkrJ0UCJEACJEACJEACJEACJEACJEACJOAGAhQvbkiBPZAACZAACZAACZAACZAACZAACZAACXiSAMWLJ2PlpEiABEiABEiABEiABEiABEiABEiABNxAgOLFDSmwBxIgARIgARIgARIgARIgARIgARIgAU8SoHjxZKycFAmQAAmQAAmQAAmQAAmQAAmQAAmQgBsIULy4IQX2QAIkQAIkQAIkQAIkQAIkQAIkQAIk4EkCFC+ejJWTIgESIAESIAESIAESIAESIAESIAEScAMBihc3pMAeSIAESIAESIAESIAESIAESIAESIAEPEmA4sWTsXJSJEACJEACJEACJEACJEACJEACJEACbiBA8eKGFNgDCZAACZAACZAACZAACZAACZAACZCAJwlQvHgyVk6KBEiABEiABEiABEiABEiABEiABEjADQQoXtyQAnsgARIgARIgARIgARIgARIgARIgARLwJAGKF0/GykmRAAmQAAmQAAmQAAmQAAmQAAmQAAm4gQDFixtSYA8kQAIkQAIkQAIkQAIkQAIkQAIkQAKeJEDx4slYOSkSIAESIAESIAESIAESIAESIAESIAE3EKB4cUMK7IEESIAESIAESIAESIAESIAESIAESMCTBChePBkrJ0UCJEACJEACJEACJEACJEACJEACJOAGAhQvbkiBPZAACZAACZAACZAACZAACZAACZAACXiSAMWLJ2PlpEiABEiABEiABEiABEiABEiABEiABNxAgOLFDSmwBxIgARIgARIgARIgARIgARIgARIgAU8SoHjxZKycFAmQAAmQAAmQAAmQAAmQAAmQAAmQgBsIULy4IQX2QAIkQAIkQAIkQAIkQAIkQAIkQAIk4EkCFC+ejJWTIgESIAESIAESIAESIAESIAESIAEScAMBihc3pMAeSIAESIAESIAESIAESIAESIAESIAEPEmA4sWTsXJSJEACJEACJEACJEACJEACJEACJEACbiBA8eKGFNgDCZAACZAACZAACZAACZAACZAACZCAJwlQvHgyVk6KBEiABEiABEiABEiABEiABEiABEjADQQoXtyQAnsgARIgARIgARIgARIgARIgARIgARLwJAGKF0/GykmRAAmQAAmQAAmQAAmQAAmQAAmQAAm4gQDFixtSYA8kQAIkQAIkQAIkQAIkQAIkQAIkQAKeJPD/AcrOUwExxqDrAAAAAElFTkSuQmCC",
      "text/html": [
       "<div>                            <div id=\"11a8f104-572c-495b-b781-687c3a6cdfed\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"11a8f104-572c-495b-b781-687c3a6cdfed\")) {                    Plotly.newPlot(                        \"11a8f104-572c-495b-b781-687c3a6cdfed\",                        [{\"hovertemplate\":\"month_cat_first=11\\u003cbr\\u003epm_conc_mean=%{x}\\u003cbr\\u003easthma_rate_first=%{y}\\u003cbr\\u003epm_conc_std=%{marker.size}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"11\",\"marker\":{\"color\":\"#636efa\",\"size\":[2.56295315194414,2.2531238544785936,2.1841878706242905,2.5088056721518153,2.8085508478873122,2.692928158894239,2.290457120363688,3.0413208904390028,2.8159214820558205,2.350662265670745,2.486085303087604,3.0264468184370243,2.380067324635726,2.7560896374184667],\"sizemode\":\"area\",\"sizeref\":0.021015160170439987,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"11\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[5.074,4.289444444444444,4.654444444444445,4.252777777777778,7.138333333333334,5.42,4.5216666666666665,5.625,5.37,5.101,5.012,7.913,4.631,5.799666666666667],\"xaxis\":\"x\",\"y\":[8.1,8.1,7.9,6.2,8.6,9.2,8.6,9.1,9.1,8.0,7.2,9.1,7.6,8.2],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"month_cat_first=12\\u003cbr\\u003epm_conc_mean=%{x}\\u003cbr\\u003easthma_rate_first=%{y}\\u003cbr\\u003epm_conc_std=%{marker.size}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"12\",\"marker\":{\"color\":\"#EF553B\",\"size\":[6.939570511007995,8.26435852987682,7.558531581256461,7.609356203606979,7.975611245425961,7.2963423448261535,7.9290978946350705,8.225558006368262,8.406064068175995,6.865905364375458,7.441130373810843,8.216440625912158,7.400116706696409,8.175230004745956],\"sizemode\":\"area\",\"sizeref\":0.021015160170439987,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"12\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[10.446774193548388,11.355806451612903,11.243548387096775,8.184516129032259,14.46225806451613,10.958709677419353,11.296774193548387,12.026129032258064,11.77741935483871,9.751612903225807,10.11483870967742,14.170322580645163,9.86,12.273225806451613],\"xaxis\":\"x\",\"y\":[8.1,8.1,7.9,6.2,8.6,9.2,8.6,9.1,9.1,8.0,7.2,9.1,7.6,8.2],\"yaxis\":\"y\",\"type\":\"scatter\"}],                        {\"template\":{\"data\":{\"histogram2dcontour\":[{\"type\":\"histogram2dcontour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"choropleth\":[{\"type\":\"choropleth\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"histogram2d\":[{\"type\":\"histogram2d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmap\":[{\"type\":\"heatmap\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmapgl\":[{\"type\":\"heatmapgl\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"contourcarpet\":[{\"type\":\"contourcarpet\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"contour\":[{\"type\":\"contour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"surface\":[{\"type\":\"surface\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"mesh3d\":[{\"type\":\"mesh3d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"parcoords\":[{\"type\":\"parcoords\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolargl\":[{\"type\":\"scatterpolargl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"scattergeo\":[{\"type\":\"scattergeo\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolar\":[{\"type\":\"scatterpolar\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"scattergl\":[{\"type\":\"scattergl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatter3d\":[{\"type\":\"scatter3d\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattermapbox\":[{\"type\":\"scattermapbox\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterternary\":[{\"type\":\"scatterternary\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattercarpet\":[{\"type\":\"scattercarpet\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}]},\"layout\":{\"autotypenumbers\":\"strict\",\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"hovermode\":\"closest\",\"hoverlabel\":{\"align\":\"left\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"bgcolor\":\"#E5ECF6\",\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"ternary\":{\"bgcolor\":\"#E5ECF6\",\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]]},\"xaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"yaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"geo\":{\"bgcolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"subunitcolor\":\"white\",\"showland\":true,\"showlakes\":true,\"lakecolor\":\"white\"},\"title\":{\"x\":0.05},\"mapbox\":{\"style\":\"light\"}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"pm_conc_mean\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"asthma_rate_first\"}},\"legend\":{\"title\":{\"text\":\"month_cat_first\"},\"tracegroupgap\":0,\"itemsizing\":\"constant\"},\"margin\":{\"t\":60}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('11a8f104-572c-495b-b781-687c3a6cdfed');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "graph = yr2024.groupby([\"Name\", \"month\"]).agg({\n",
    "    \"pm_conc\": [\"mean\", \"median\", \"std\"],\n",
    "    \"asthma_rate\": \"first\",\n",
    "    \"month_cat\": \"first\"\n",
    "    \n",
    "}).reset_index()\n",
    "\n",
    "graph.columns = ['_'.join(col).strip('_') for col in graph.columns.values]\n",
    "\n",
    "px.scatter(graph, x = 'pm_conc_mean', y = 'asthma_rate_first', color = 'month_cat_first', size = 'pm_conc_std')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "1b8babc9-4542-4980-8754-b91705c8863e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hovertemplate": "month_cat_first=1<br>pm_conc_mean=%{x}<br>asthma_rate_first=%{y}<br>pm_conc_std=%{marker.size}<extra></extra>",
         "legendgroup": "1",
         "marker": {
          "color": "#636efa",
          "size": [
           2.9957810020621873,
           3.7258773354374433,
           3.5430858102888165,
           3.3880464862226662,
           4.335886073638159,
           3.6818208737303557,
           3.7806533782515843,
           4.180907268930734,
           4.0660934198472045,
           2.2476522220089565,
           3.8396829102515433,
           4.32301544996605,
           3.4648238625977763,
           3.82866443355699
          ],
          "sizemode": "area",
          "sizeref": 0.021015160170439987,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "1",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          7.583225806451614,
          7.880645161290323,
          7.723225806451612,
          7.32,
          11.034516129032257,
          7.998709677419355,
          8.159032258064517,
          8.855483870967742,
          8.460967741935484,
          6.365483870967742,
          7.153225806451613,
          11.263225806451612,
          6.9561290322580644,
          8.916774193548386
         ],
         "xaxis": "x",
         "y": [
          8.1,
          8.1,
          7.9,
          6.2,
          8.6,
          9.2,
          8.6,
          9.1,
          9.1,
          8,
          7.2,
          9.1,
          7.6,
          8.2
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "month_cat_first=2<br>pm_conc_mean=%{x}<br>asthma_rate_first=%{y}<br>pm_conc_std=%{marker.size}<extra></extra>",
         "legendgroup": "2",
         "marker": {
          "color": "#EF553B",
          "size": [
           1.7675237365594645,
           1.9345616166226813,
           1.84826892566605,
           1.8744370697360528,
           2.3328871129146584,
           1.9507750121805816,
           2.065622795527259,
           2.089673622018722,
           2.0544377054839815,
           1.4347537666852355,
           1.8572005090268797,
           2.8394439009543158,
           1.7900531665727828,
           1.9500426577145626
          ],
          "sizemode": "area",
          "sizeref": 0.021015160170439987,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "2",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          4.399642857142857,
          4.499642857142858,
          4.7525,
          4.406785714285714,
          7.232142857142857,
          4.7275,
          4.652857142857143,
          4.931071428571428,
          4.795714285714285,
          4.1432142857142855,
          4.199285714285714,
          7.7124999999999995,
          4.147857142857143,
          5.2725
         ],
         "xaxis": "x",
         "y": [
          8.1,
          8.1,
          7.9,
          6.2,
          8.6,
          9.2,
          8.6,
          9.1,
          9.1,
          8,
          7.2,
          9.1,
          7.6,
          8.2
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "month_cat_first=3<br>pm_conc_mean=%{x}<br>asthma_rate_first=%{y}<br>pm_conc_std=%{marker.size}<extra></extra>",
         "legendgroup": "3",
         "marker": {
          "color": "#00cc96",
          "size": [
           1.3381565551407615,
           1.4241798439456765,
           1.5458032702495494,
           1.528309920709372,
           2.2076427781560817,
           1.512228150278464,
           1.4528193701659144,
           1.5096692652109536,
           1.6414789423807934,
           1.1964568555204615,
           1.5912980792028684,
           3.196387746137179,
           1.4660361674962887,
           1.7268966307188458
          ],
          "sizemode": "area",
          "sizeref": 0.021015160170439987,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "3",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          4.428387096774194,
          4.426774193548387,
          4.662903225806452,
          4.672258064516129,
          7.428709677419355,
          4.691612903225806,
          4.580967741935484,
          4.837096774193548,
          4.917419354838709,
          4.513225806451612,
          4.460967741935484,
          8.002903225806453,
          4.299032258064516,
          5.259677419354839
         ],
         "xaxis": "x",
         "y": [
          8.1,
          8.1,
          7.9,
          6.2,
          8.6,
          9.2,
          8.6,
          9.1,
          9.1,
          8,
          7.2,
          9.1,
          7.6,
          8.2
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "month_cat_first=4<br>pm_conc_mean=%{x}<br>asthma_rate_first=%{y}<br>pm_conc_std=%{marker.size}<extra></extra>",
         "legendgroup": "4",
         "marker": {
          "color": "#ab63fa",
          "size": [
           0,
           0,
           0,
           0,
           0,
           0,
           0,
           0,
           0,
           0
          ],
          "sizemode": "area",
          "sizeref": 0.021015160170439987,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "4",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          3.7599999999999993,
          3.87,
          4.22,
          4.47,
          7.019999999999999,
          3.9,
          3.9200000000000004,
          3.84,
          3.8299999999999996,
          4.68
         ],
         "xaxis": "x",
         "y": [
          8.1,
          8.1,
          7.9,
          6.2,
          8.6,
          8.6,
          8,
          7.2,
          7.6,
          8.2
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "month_cat_first=11<br>pm_conc_mean=%{x}<br>asthma_rate_first=%{y}<br>pm_conc_std=%{marker.size}<extra></extra>",
         "legendgroup": "11",
         "marker": {
          "color": "#FFA15A",
          "size": [
           2.56295315194414,
           2.2531238544785936,
           2.1841878706242905,
           2.5088056721518153,
           2.8085508478873122,
           2.692928158894239,
           2.290457120363688,
           3.0413208904390028,
           2.8159214820558205,
           2.350662265670745,
           2.486085303087604,
           3.0264468184370243,
           2.380067324635726,
           2.7560896374184667
          ],
          "sizemode": "area",
          "sizeref": 0.021015160170439987,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "11",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          5.074,
          4.289444444444444,
          4.654444444444445,
          4.252777777777778,
          7.138333333333334,
          5.42,
          4.5216666666666665,
          5.625,
          5.37,
          5.101,
          5.012,
          7.913,
          4.631,
          5.799666666666667
         ],
         "xaxis": "x",
         "y": [
          8.1,
          8.1,
          7.9,
          6.2,
          8.6,
          9.2,
          8.6,
          9.1,
          9.1,
          8,
          7.2,
          9.1,
          7.6,
          8.2
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "month_cat_first=12<br>pm_conc_mean=%{x}<br>asthma_rate_first=%{y}<br>pm_conc_std=%{marker.size}<extra></extra>",
         "legendgroup": "12",
         "marker": {
          "color": "#19d3f3",
          "size": [
           6.939570511007995,
           8.26435852987682,
           7.558531581256461,
           7.609356203606979,
           7.975611245425961,
           7.2963423448261535,
           7.9290978946350705,
           8.225558006368262,
           8.406064068175995,
           6.865905364375458,
           7.441130373810843,
           8.216440625912158,
           7.400116706696409,
           8.175230004745956
          ],
          "sizemode": "area",
          "sizeref": 0.021015160170439987,
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "12",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          10.446774193548388,
          11.355806451612903,
          11.243548387096775,
          8.184516129032259,
          14.46225806451613,
          10.958709677419353,
          11.296774193548387,
          12.026129032258064,
          11.77741935483871,
          9.751612903225807,
          10.11483870967742,
          14.170322580645163,
          9.86,
          12.273225806451613
         ],
         "xaxis": "x",
         "y": [
          8.1,
          8.1,
          7.9,
          6.2,
          8.6,
          9.2,
          8.6,
          9.1,
          9.1,
          8,
          7.2,
          9.1,
          7.6,
          8.2
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "autosize": true,
        "legend": {
         "itemsizing": "constant",
         "title": {
          "text": "month_cat_first"
         },
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "xaxis": {
         "anchor": "y",
         "autorange": true,
         "domain": [
          0,
          1
         ],
         "range": [
          3.1105503720241305,
          15.280908946697975
         ],
         "title": {
          "text": "pm_conc_mean"
         },
         "type": "linear"
        },
        "yaxis": {
         "anchor": "x",
         "autorange": true,
         "domain": [
          0,
          1
         ],
         "range": [
          5.735562368832968,
          9.658861938959106
         ],
         "title": {
          "text": "asthma_rate_first"
         },
         "type": "linear"
        }
       }
      },
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABF4AAAFoCAYAAABuXz/oAAAAAXNSR0IArs4c6QAAIABJREFUeF7snQd4HNXZtp8zbYu6ZLl3bDAYA6bXUJxQTQm9BEggpiUESAFCIMCXhIQaAoGQQIDAD9j03gkG03EoNhiMe5etXrdN+a8zsmzJkrVldqVd7TO5nMTWzJkz93lntXPPe94jHMdxwI0ESIAESIAESIAESIAESIAESIAESIAESCDtBATFS9qZskESIAESIAESIAESIAESIAESIAESIAEScAlQvDAQSIAESIAESIAESIAESIAESIAESIAESCBDBCheMgSWzZIACZAACZAACZAACZAACZAACZAACZAAxQtjgARIgARIgARIgARIgARIgARIgARIgAQyRIDiJUNg2SwJkAAJkAAJkAAJkAAJkAAJkAAJkAAJULwwBkiABEiABEiABEiABEiABEiABEiABEggQwQoXjIEls2SAAmQAAmQAAmQAAmQAAmQAAmQAAmQAMULY4AESIAESIAESIAESIAESIAESIAESIAEMkSA4iVDYNksCZAACZAACZAACZAACZAACZAACZAACVC8MAZIgARIgARIgARIgARIgARIgARIgARIIEMEKF4yBJbNkgAJkAAJkAAJkAAJkAAJkAAJkAAJkADFC2OABEiABEiABEiABEiABEiABEiABEiABDJEgOIlQ2DZLAmQAAmQAAmQAAmQAAmQAAmQAAmQAAlQvDAGSIAESIAESIAESIAESIAESIAESIAESCBDBCheMgSWzZIACZAACZAACZAACZAACZAACZAACZAAxQtjgARIgARIgARIgARIgARIgARIgARIgAQyRIDiJUNg2SwJkAAJkAAJkAAJkAAJkAAJkAAJkAAJULwwBkiABEiABEiABEiABEiABEiABEiABEggQwQoXjIEls2SAAmQAAmQAAmQAAmQAAmQAAmQAAmQAMULY4AESIAESIAESIAESIAESIAESIAESIAEMkSA4iVDYNksCZAACZAACZAACZAACZAACZAACZAACVC8MAZIgARIgARIgARIgARIgARIgARIgARIIEMEKF4yBJbNkgAJkAAJkAAJkAAJkAAJkAAJkAAJkADFC2OABEiABEiABEiABEiABEiABEiABEiABDJEgOIlQ2DZLAmQAAmQAAmQAAmQAAmQAAmQAAmQAAlQvDAGSIAESIAESIAESIAESIAESIAESIAESCBDBCheMgSWzZIACZAACZAACZAACZAACZAACZAACZAAxQtjgARIgARIgARIgARIgARIgARIgARIgAQyRIDiJUNg2SwJkAAJkAAJkAAJkAAJkAAJkAAJkAAJULwwBkiABEiABEiABEiABEiABEiABEiABEggQwQoXjIEls2SAAmQAAmQAAmQAAmQAAmQAAmQAAmQAMULY4AESIAESIAESIAESIAESIAESIAESIAEMkSA4iVDYNksCZAACZAACZAACZAACZAACZAACZAACVC8MAZIgARIgARIgARIgARIgARIgARIgARIIEMEKF4yBJbNkgAJkAAJkAAJkAAJkAAJkAAJkAAJkADFC2OABEiABEiABEiABEiABEiABEiABEiABDJEgOIlQ2DZLAmQAAmQAAmQAAmQAAmQAAmQAAmQAAlQvDAGSIAESIAESIAESIAESIAESIAESIAESCBDBCheMgSWzZIACZAACZAACZAACZAACZAACZAACZAAxQtjgARIgARIgARIgARIgARIgARIgARIgAQyRIDiJUNg2SwJkAAJkAAJkAAJkAAJkAAJkAAJkAAJULwwBkiABEiABEiABEiABEiABEiABEiABEggQwQoXjIEls2SAAmQAAmQAAmQAAmQAAmQAAmQAAmQAMULY4AESIAESIAESIAESIAESIAESIAESIAEMkSA4iVDYNksCZAACZAACZAACZAACZAACZAACZAACVC8MAZIgARIgARIgARIgARIgARIgARIgARIIEMEKF4yBJbNkgAJkAAJkAAJkAAJkAAJkAAJkAAJkADFC2OABEiABEiABEiABEiABEiABEiABEiABDJEgOIlQ2DZLAmQAAmQAAmQAAmQAAmQAAmQAAmQAAlQvDAGSIAESIAESIAESIAESIAESIAESIAESCBDBCheMgSWzZIACZAACZAACZAACZAACZAACZAACZAAxQtjgARIgARIgARIgARIgARIgARIgARIgAQyRIDiJUNg2SwJkAAJkAAJkAAJkAAJkAAJkAAJkAAJULwwBkiABEiABEiABEiABEiABEiABEiABEggQwQoXjIEls2SAAmQAAmQAAmQAAmQAAmQAAmQAAmQAMULY4AESIAESIAESIAESIAESIAESIAESIAEMkSA4iVD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8eZTE/XXSTf0CnseNXLZwmC6OU2A4iWny+ecyVO8OKcWuTYT8QrXK264v/4bnK4H7Y07xo6s39afa/lwvvYQKCuvxJRHnscb732qT6Djzq0x9LQT9J14fEigKQLigtP+w67fpol4VXTdxcxLV6zGyNF366+bFs8pJ/yf/oHa6/UQLAlsQ6Bux+bWfzj+2uEY2LcHxC6Y516ZuwMx7n7hImqIgPi9Wuwwr3vEcWxxLHv7h+KF64cEcocAxUvu1IozJQGpCYi7gzwerf6uF6mTZXJZI1D3auA2pSVZi8GB3UlAbPsvyA8iPy/gTgDMmgRIgARIgARIIG0CFC9po2NHEiABEiABEiABEiABEiABEiABEiABEmiaAMULVwgJkAAJkAAJkAAJkAAJkAAJkAAJkAAJZIkAxUuWwHJYEiABEiABEiABEiABEiABEiABEiABEqB44RogARIgARIgARIgARIgARIgARIgARIggSwRoHjJElgOSwIkQAIkQAIkQAIkQAIkQAIkQAIkQAIUL1wDJEACJEACJEACJEACJEACJEACJEACJJAlAhQvWQLLYUmABEiABEiABEiABEiABEiABEiABEiA4oVrgARIgARIgARIgARIgARIgARIgARIgASyRIDiJUtgOSwJkAAJkAAJkAAJkAAJkAAJkAAJkAAJULxwDZAACZAACZAACZAACZAACZAACZAACZBAlghQvGQJLIclARIgARIgARIgARIgARIgARIgARIgAYoXrgESIAESIAESIAESIAESIAESIAESIAESyBIBipcsgeWwJEACJEACJEACJEACJEACJEACJEACJEDxwjVAAiRAAiRAAiRAAiRAAiRAAiRAAiRAAlkiQPGSJbAclgRIgARIgARIgARIgARIgARIgARIgAQoXrgGSIAESIAESIAESIAESIAESIAESIAESCBLBChesgSWw5IACZAACZAACZAACZAACZAACZAACZAAxQvXAAmQAAmQAAmQAAmQAAmQAAmQAAmQAAlkiQDFS5bAclgSIAESIAH3Enjulbn4+IvvcWiXznj+9XlYsvx39DryIIy7eihalhTrYMbe8RhaNC9COBzBa3M+0f/snFOPx8C+PTD54Vn48NNvsFPrljj3tN448ZjDU4K5YtVaTHnkBfz3h8WIRKI4pEtnjDz3ZOy1ewf9vx984hW88e6n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R43Ef5dXVOlvLZr56vv1MQRjcfyoT6+uWLVmg36Z7lff/aL/vXjzUTwWrz96VVlVox+T2v6yYnHHi7ivRogpPiRAAiRAAiRAAiRgNgGKF7OJcjwSIAESIAHXE6g7avTmUxP1XRniMthgwGc5lw2byvWY4lXU4ijO1o94m9GWyipdlHg0La25ieNL6zZsRn5+0NJXMYtLdNdvKEMg4NOPbW3/rF67Ud8FI4QTHxIgARIgARIgARKwmwDFi90VYHwSIAESIAHpCDR0x0umSYrLea8ZP63JYcSOlik3X5JpqLT7i9c/i10qTT2XnTcQ55x6fNox2JEESIAESIAESIAEco0AxUuuVYzzJQESIAEScDwBIR8WfPE97ptwuWlzFbtLwpFok+OJi239Pq9pMVMdKBKJIhqLN9nN69XS3mGT6nzYngRIgARIgARIgAScQIDixQlV4BxIgARIgARIgARIgARIgARIgARIgASkJEDxImVZmRQJkAAJkAAJkAAJkAAJkAAJkAAJkIATCFC8OKEKnAMJkAAJkAAJkAAJkAAJkAAJkAAJkICUBChepCwrkyIBEiABEiABEiABEiABEiABEiABEnACAYoXJ1SBcyABEiABEiABEiABEiABEiABEiABEpCSAMWLlGVlUiRAAiRAAiRAAiRAAiRAAiRAAiRAAk4gQPHihCpwDiRAAiRAAiRAAiRAAiRAAiRAAiRAAlISoHiRsqxMigRIgARIgARIgARIgARIgARIgARIwAkEKF6cUAXOgQRIgARIgARIgARIgARIgARIgARIQEoCFC9SlpVJkQAJkAAJkAAJkAAJkAAJkAAJkAAJOIEAxYsTqsA5kAAJkAAJkAAJkAAJkAAJkAAJkAAJSEmA4kXKsjIpEiABEiABEiABEiABEiABEiABEiABJxCgeHFCFTgHEiABEiABEiABEiABEiABEiABEiABKQlQvEhZViZFAiRAAiRAAiRAAiRAAiRAAiRAAiTgBAIUL06oAudAAiRAAiRAAiRAAiRAAiRAAiRAAiQgJQGKFynLyqRIgARIgARIgARIgARIgARIgARIgAScQIDixQlV4BxIgARIgARIgARIgARIgARIgARIgASkJEDxImVZmRQJkAAJkAAJkAAJkAAJkAAJkAAJkIATCFC8OKEKnAMJkAAJkAAJkAAJkAAJkAAJkAAJkICUBChepCwrkyIBEiABEiABEiABEiABEiABEiABEnACAYoXJ1SBcyABEiABEiABEiABEiABEiABEiABEpCSAMWLlGVlUiRAAiRAAiRAAiRAAiRAAiRAAiRAAk4gQPHihCpwDiRAAiRAAiRAAiRAAiRAAiRAAiRAAlISoHiRsqxMigRIgARIgARIgARIgARIgARIgARIwAkEKF6cUAXOgQRIgARIgARIgARIgARIgARIgARIQEoCFC9SlpVJkQAJkAAJkAAJkAAJkAAJkAAJkAAJOIEAxYsTqsA5kAAJkAAJkAAJkAAJkAAJkAAJkAAJSEmA4kXKsjIpEiABEiABEiABEiABEiABEiABEiABJxCgeHFCFTgHEiABEiABEiABEiABEiABEiABEiABKQlQvEhZViZFAiRAAiRAAiRAAiRAAiRAAiRAAiTgBAIUL06oAudAAiRAAiRAAiRAAiRAAiRAAiRAAiQgJQGKFynLyqRIgARIgARIgARIgARIgARIgARIgAScQIDixQlV4BxIgARIgARIgARIgARIgARIgARIgASkJEDxImVZmRQJkAAJkAAJkAAJkAAJkAAJkAAJkIATCFC8OKEKnAMJkAAJkAAJkAAJkAAJkAAJkAAJkICUBChepCwrkyIBEiABEiABEiABEiABEiABEiABEnACAYoXJ1SBcyABEiABEiABEiABEiABEiABEiABEpCSwP8DgtmjLSU3Gd8AAAAASUVORK5CYII=",
      "text/html": [
       "<div>                            <div id=\"b5e09a32-6d63-4b56-baf7-4f2a2d7160d5\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"b5e09a32-6d63-4b56-baf7-4f2a2d7160d5\")) {                    Plotly.newPlot(                        \"b5e09a32-6d63-4b56-baf7-4f2a2d7160d5\",                        [{\"hovertemplate\":\"month_cat_first=1\\u003cbr\\u003epm_conc_mean=%{x}\\u003cbr\\u003easthma_rate_first=%{y}\\u003cbr\\u003epm_conc_std=%{marker.size}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"1\",\"marker\":{\"color\":\"#636efa\",\"size\":[2.9957810020621873,3.7258773354374433,3.5430858102888165,3.3880464862226662,4.335886073638159,3.6818208737303557,3.7806533782515843,4.180907268930734,4.0660934198472045,2.2476522220089565,3.8396829102515433,4.32301544996605,3.4648238625977763,3.82866443355699],\"sizemode\":\"area\",\"sizeref\":0.021015160170439987,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"1\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[7.583225806451614,7.880645161290323,7.723225806451612,7.32,11.034516129032257,7.998709677419355,8.159032258064517,8.855483870967742,8.460967741935484,6.365483870967742,7.153225806451613,11.263225806451612,6.9561290322580644,8.916774193548386],\"xaxis\":\"x\",\"y\":[8.1,8.1,7.9,6.2,8.6,9.2,8.6,9.1,9.1,8.0,7.2,9.1,7.6,8.2],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"month_cat_first=2\\u003cbr\\u003epm_conc_mean=%{x}\\u003cbr\\u003easthma_rate_first=%{y}\\u003cbr\\u003epm_conc_std=%{marker.size}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"2\",\"marker\":{\"color\":\"#EF553B\",\"size\":[1.7675237365594645,1.9345616166226813,1.84826892566605,1.8744370697360528,2.3328871129146584,1.9507750121805816,2.065622795527259,2.089673622018722,2.0544377054839815,1.4347537666852355,1.8572005090268797,2.8394439009543158,1.7900531665727828,1.9500426577145626],\"sizemode\":\"area\",\"sizeref\":0.021015160170439987,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"2\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[4.399642857142857,4.499642857142858,4.7525,4.406785714285714,7.232142857142857,4.7275,4.652857142857143,4.931071428571428,4.795714285714285,4.1432142857142855,4.199285714285714,7.7124999999999995,4.147857142857143,5.2725],\"xaxis\":\"x\",\"y\":[8.1,8.1,7.9,6.2,8.6,9.2,8.6,9.1,9.1,8.0,7.2,9.1,7.6,8.2],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"month_cat_first=3\\u003cbr\\u003epm_conc_mean=%{x}\\u003cbr\\u003easthma_rate_first=%{y}\\u003cbr\\u003epm_conc_std=%{marker.size}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"3\",\"marker\":{\"color\":\"#00cc96\",\"size\":[1.3381565551407615,1.4241798439456765,1.5458032702495494,1.528309920709372,2.2076427781560817,1.512228150278464,1.4528193701659144,1.5096692652109536,1.6414789423807934,1.1964568555204615,1.5912980792028684,3.196387746137179,1.4660361674962887,1.7268966307188458],\"sizemode\":\"area\",\"sizeref\":0.021015160170439987,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"3\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[4.428387096774194,4.426774193548387,4.662903225806452,4.672258064516129,7.428709677419355,4.691612903225806,4.580967741935484,4.837096774193548,4.917419354838709,4.513225806451612,4.460967741935484,8.002903225806453,4.299032258064516,5.259677419354839],\"xaxis\":\"x\",\"y\":[8.1,8.1,7.9,6.2,8.6,9.2,8.6,9.1,9.1,8.0,7.2,9.1,7.6,8.2],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"month_cat_first=4\\u003cbr\\u003epm_conc_mean=%{x}\\u003cbr\\u003easthma_rate_first=%{y}\\u003cbr\\u003epm_conc_std=%{marker.size}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"4\",\"marker\":{\"color\":\"#ab63fa\",\"size\":[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],\"sizemode\":\"area\",\"sizeref\":0.021015160170439987,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"4\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[3.7599999999999993,3.87,4.22,4.47,7.019999999999999,3.9,3.9200000000000004,3.84,3.8299999999999996,4.68],\"xaxis\":\"x\",\"y\":[8.1,8.1,7.9,6.2,8.6,8.6,8.0,7.2,7.6,8.2],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"month_cat_first=11\\u003cbr\\u003epm_conc_mean=%{x}\\u003cbr\\u003easthma_rate_first=%{y}\\u003cbr\\u003epm_conc_std=%{marker.size}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"11\",\"marker\":{\"color\":\"#FFA15A\",\"size\":[2.56295315194414,2.2531238544785936,2.1841878706242905,2.5088056721518153,2.8085508478873122,2.692928158894239,2.290457120363688,3.0413208904390028,2.8159214820558205,2.350662265670745,2.486085303087604,3.0264468184370243,2.380067324635726,2.7560896374184667],\"sizemode\":\"area\",\"sizeref\":0.021015160170439987,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"11\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[5.074,4.289444444444444,4.654444444444445,4.252777777777778,7.138333333333334,5.42,4.5216666666666665,5.625,5.37,5.101,5.012,7.913,4.631,5.799666666666667],\"xaxis\":\"x\",\"y\":[8.1,8.1,7.9,6.2,8.6,9.2,8.6,9.1,9.1,8.0,7.2,9.1,7.6,8.2],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"month_cat_first=12\\u003cbr\\u003epm_conc_mean=%{x}\\u003cbr\\u003easthma_rate_first=%{y}\\u003cbr\\u003epm_conc_std=%{marker.size}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"12\",\"marker\":{\"color\":\"#19d3f3\",\"size\":[6.939570511007995,8.26435852987682,7.558531581256461,7.609356203606979,7.975611245425961,7.2963423448261535,7.9290978946350705,8.225558006368262,8.406064068175995,6.865905364375458,7.441130373810843,8.216440625912158,7.400116706696409,8.175230004745956],\"sizemode\":\"area\",\"sizeref\":0.021015160170439987,\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"12\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[10.446774193548388,11.355806451612903,11.243548387096775,8.184516129032259,14.46225806451613,10.958709677419353,11.296774193548387,12.026129032258064,11.77741935483871,9.751612903225807,10.11483870967742,14.170322580645163,9.86,12.273225806451613],\"xaxis\":\"x\",\"y\":[8.1,8.1,7.9,6.2,8.6,9.2,8.6,9.1,9.1,8.0,7.2,9.1,7.6,8.2],\"yaxis\":\"y\",\"type\":\"scatter\"}],                        {\"template\":{\"data\":{\"histogram2dcontour\":[{\"type\":\"histogram2dcontour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"choropleth\":[{\"type\":\"choropleth\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"histogram2d\":[{\"type\":\"histogram2d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmap\":[{\"type\":\"heatmap\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmapgl\":[{\"type\":\"heatmapgl\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"contourcarpet\":[{\"type\":\"contourcarpet\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"contour\":[{\"type\":\"contour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"surface\":[{\"type\":\"surface\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"mesh3d\":[{\"type\":\"mesh3d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"parcoords\":[{\"type\":\"parcoords\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolargl\":[{\"type\":\"scatterpolargl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"scattergeo\":[{\"type\":\"scattergeo\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolar\":[{\"type\":\"scatterpolar\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"scattergl\":[{\"type\":\"scattergl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatter3d\":[{\"type\":\"scatter3d\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattermapbox\":[{\"type\":\"scattermapbox\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterternary\":[{\"type\":\"scatterternary\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattercarpet\":[{\"type\":\"scattercarpet\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}]},\"layout\":{\"autotypenumbers\":\"strict\",\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"hovermode\":\"closest\",\"hoverlabel\":{\"align\":\"left\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"bgcolor\":\"#E5ECF6\",\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"ternary\":{\"bgcolor\":\"#E5ECF6\",\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]]},\"xaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"yaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"geo\":{\"bgcolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"subunitcolor\":\"white\",\"showland\":true,\"showlakes\":true,\"lakecolor\":\"white\"},\"title\":{\"x\":0.05},\"mapbox\":{\"style\":\"light\"}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"pm_conc_mean\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"asthma_rate_first\"}},\"legend\":{\"title\":{\"text\":\"month_cat_first\"},\"tracegroupgap\":0,\"itemsizing\":\"constant\"},\"margin\":{\"t\":60}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('b5e09a32-6d63-4b56-baf7-4f2a2d7160d5');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "graph = clarity_cleaned.groupby([\"Name\", \"month\"]).agg({\n",
    "    \"pm_conc\": [\"mean\", \"median\", \"std\"],\n",
    "    \"asthma_rate\": \"first\",\n",
    "    \"month_cat\": \"first\",\n",
    "    \"threshold\": lambda x: (x == True).sum()\n",
    "    \n",
    "}).reset_index()\n",
    "\n",
    "graph.columns = ['_'.join(col).strip('_') for col in graph.columns.values]\n",
    "graph = graph.dropna()\n",
    "\n",
    "px.scatter(graph, x = 'pm_conc_mean', y = 'asthma_rate_first', color = 'month_cat_first', size = 'pm_conc_std')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "id": "80f4755b-1d28-4a88-8456-1952ae008940",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hovertemplate": "month_cat_first=1<br>pm_conc_mean=%{x}<br>pm_conc_std=%{y}<extra></extra>",
         "legendgroup": "1",
         "marker": {
          "color": "#636efa",
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "1",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          7.583225806451614,
          7.880645161290323,
          7.723225806451612,
          7.32,
          11.034516129032257,
          7.998709677419355,
          8.159032258064517,
          8.855483870967742,
          8.460967741935484,
          6.365483870967742,
          7.153225806451613,
          11.263225806451612,
          6.9561290322580644,
          8.916774193548386
         ],
         "xaxis": "x",
         "y": [
          2.9957810020621873,
          3.7258773354374433,
          3.5430858102888165,
          3.3880464862226662,
          4.335886073638159,
          3.6818208737303557,
          3.7806533782515843,
          4.180907268930734,
          4.0660934198472045,
          2.2476522220089565,
          3.8396829102515433,
          4.32301544996605,
          3.4648238625977763,
          3.82866443355699
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "month_cat_first=2<br>pm_conc_mean=%{x}<br>pm_conc_std=%{y}<extra></extra>",
         "legendgroup": "2",
         "marker": {
          "color": "#EF553B",
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "2",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          4.399642857142857,
          4.499642857142858,
          4.7525,
          4.406785714285714,
          7.232142857142857,
          4.7275,
          4.652857142857143,
          4.931071428571428,
          4.795714285714285,
          4.1432142857142855,
          4.199285714285714,
          7.7124999999999995,
          4.147857142857143,
          5.2725
         ],
         "xaxis": "x",
         "y": [
          1.7675237365594645,
          1.9345616166226813,
          1.84826892566605,
          1.8744370697360528,
          2.3328871129146584,
          1.9507750121805816,
          2.065622795527259,
          2.089673622018722,
          2.0544377054839815,
          1.4347537666852355,
          1.8572005090268797,
          2.8394439009543158,
          1.7900531665727828,
          1.9500426577145626
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "month_cat_first=3<br>pm_conc_mean=%{x}<br>pm_conc_std=%{y}<extra></extra>",
         "legendgroup": "3",
         "marker": {
          "color": "#00cc96",
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "3",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          4.428387096774194,
          4.426774193548387,
          4.662903225806452,
          4.672258064516129,
          7.428709677419355,
          4.691612903225806,
          4.580967741935484,
          4.837096774193548,
          4.917419354838709,
          4.513225806451612,
          4.460967741935484,
          8.002903225806453,
          4.299032258064516,
          5.259677419354839
         ],
         "xaxis": "x",
         "y": [
          1.3381565551407615,
          1.4241798439456765,
          1.5458032702495494,
          1.528309920709372,
          2.2076427781560817,
          1.512228150278464,
          1.4528193701659144,
          1.5096692652109536,
          1.6414789423807934,
          1.1964568555204615,
          1.5912980792028684,
          3.196387746137179,
          1.4660361674962887,
          1.7268966307188458
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "month_cat_first=4<br>pm_conc_mean=%{x}<br>pm_conc_std=%{y}<extra></extra>",
         "legendgroup": "4",
         "marker": {
          "color": "#ab63fa",
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "4",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          3.7599999999999993,
          3.87,
          4.22,
          4.47,
          7.019999999999999,
          3.9,
          3.9200000000000004,
          3.84,
          3.8299999999999996,
          4.68
         ],
         "xaxis": "x",
         "y": [
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "month_cat_first=11<br>pm_conc_mean=%{x}<br>pm_conc_std=%{y}<extra></extra>",
         "legendgroup": "11",
         "marker": {
          "color": "#FFA15A",
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "11",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          5.074,
          4.289444444444444,
          4.654444444444445,
          4.252777777777778,
          7.138333333333334,
          5.42,
          4.5216666666666665,
          5.625,
          5.37,
          5.101,
          5.012,
          7.913,
          4.631,
          5.799666666666667
         ],
         "xaxis": "x",
         "y": [
          2.56295315194414,
          2.2531238544785936,
          2.1841878706242905,
          2.5088056721518153,
          2.8085508478873122,
          2.692928158894239,
          2.290457120363688,
          3.0413208904390028,
          2.8159214820558205,
          2.350662265670745,
          2.486085303087604,
          3.0264468184370243,
          2.380067324635726,
          2.7560896374184667
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "month_cat_first=12<br>pm_conc_mean=%{x}<br>pm_conc_std=%{y}<extra></extra>",
         "legendgroup": "12",
         "marker": {
          "color": "#19d3f3",
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "12",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          10.446774193548388,
          11.355806451612903,
          11.243548387096775,
          8.184516129032259,
          14.46225806451613,
          10.958709677419353,
          11.296774193548387,
          12.026129032258064,
          11.77741935483871,
          9.751612903225807,
          10.11483870967742,
          14.170322580645163,
          9.86,
          12.273225806451613
         ],
         "xaxis": "x",
         "y": [
          6.939570511007995,
          8.26435852987682,
          7.558531581256461,
          7.609356203606979,
          7.975611245425961,
          7.2963423448261535,
          7.9290978946350705,
          8.225558006368262,
          8.406064068175995,
          6.865905364375458,
          7.441130373810843,
          8.216440625912158,
          7.400116706696409,
          8.175230004745956
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "autosize": true,
        "legend": {
         "title": {
          "text": "month_cat_first"
         },
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "xaxis": {
         "anchor": "y",
         "autorange": true,
         "domain": [
          0,
          1
         ],
         "range": [
          3.1093597668560853,
          15.112898297660044
         ],
         "title": {
          "text": "pm_conc_mean"
         },
         "type": "linear"
        },
        "yaxis": {
         "anchor": "x",
         "autorange": true,
         "domain": [
          0,
          1
         ],
         "range": [
          -0.6508632283758317,
          9.056927296551827
         ],
         "title": {
          "text": "pm_conc_std"
         },
         "type": "linear"
        }
       }
      },
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABF4AAAFoCAYAAABuXz/oAAAAAXNSR0IArs4c6QAAIABJREFUeF7snQd8FNXah/+zJT2kEEIHAQHFAgKCgAiCigXwogIXC1iuIIKo2BBUQAVErFgRewMUxUq7oiiKIope7CKCdEgICenZ9n0zgZBlA7ubOTO7s+c/9/f9vnuTOe8553nfhOTJKYrP5/OBDwmQAAmQAAmQAAmQAAmQAAmQAAmQAAmQgHACCsWLcKYMSAIkQAIkQAIkQAIkQAIkQAIkQAIkQAIaAYoXFgIJkAAJkAAJkAAJkAAJkAAJkAAJkAAJGESA4sUgsAxLAiRAAiRAAiRAAiRAAiRAAiRAAiRAAhQvrAESIAESIAESIAESIAESIAESIAESIAESMIgAxYtBYBmWBEiABEiABEiABEiABEiABEiABEiABCheWAMkQAIkQAIkQAIkQAIkQAIkQAIkQAIkYBABiheDwDIsCZAACZAACZAACZAACZAACZAACZAACVC8sAZIgARIgARIgARIgARIgARIgARIgARIwCACFC8GgWVYEiABEiABEiABEiABEiABEiABEiABEqB4YQ2QAAmQAAmQAAmQAAmQAAmQAAmQAAmQgEEEKF4MAsuwJEACJEACJEACJEACJEACJEACJEACJEDxwhogARIgARIgARIgARIgARIgARIgARIgAYMIULwYBJZhSYAESIAESIAESIAESIAESIAESIAESIDihTVAAiRAAiRAAiRAAiRAAiRAAiRAAiRAAgYRoHgxCCzDkgAJkAAJkAAJkAAJkAAJkAAJkAAJkADFC2uABEiABEiABEiABEiABEiABEiABEiABAwiQPFiEFiGJQESIAESIAESIAESIAESIAESIAESIAGKF9YACZAACZAACZAACZAACZAACZAACZAACRhEgOLFILAMSwIkQAIkQAIkQAIkQAIkQAIkQAIkQAIUL6wBEiABEiABEiABEiABEiABEiABEiABEjCIAMWLQWAZlgRIgARIgARIgARIgARIgARIgARIgAQoXlgDJEACJEACJEACJEACJEACJEACJEACJGAQAYoXg8AyLAmQAAmQAAmQAAmQAAmQAAmQAAmQAAlQvLAGSIAESIAESIAESIAESIAESIAESIAESMAgAhQvBoFlWBIgARIgARIgARIgARIgARIgARIgARKgeGENkAAJkAAJkAAJkAAJkAAJkAAJkAAJkIBBBCheDALLsCRAAiRAAiRAAiRAAiRAAiRAAiRAAiRA8cIaIAESIAESIAESIAESIAESIAESIAESIAGDCFC8GASWYUmABEiABEiABEiABEiABEiABEiABEiA4oU1QAIkQAIkQAIkQAIkQAIkQAIkQAIkQAIGEaB4MQgsw5IACZAACZAACZAACZAACZAACZAACZAAxQtrgARIgARIgARIgARIgARIgARIgARIgAQMIkDxYhBYhiUBEiABEiABEiABEiABEiABEiABEiABihfWAAmQAAmQAAmQAAmQAAmQAAmQAAmQAAkYRIDixSCwDEsCJEACJEACJEACJEACJEACJEACJEACFC+sARIgARIgARIgARIgARIgARIgARIgARIwiADFi0FgGZYESIAESIAESIAESIAESIAESIAESIAEKF5YAyRAAiRAAiRAAiRAAiRAAiRAAiRAAiRgEAGKF4PAMiwJkAAJkAAJkAAJkAAJkAAJkAAJkAAJULywBkiABEiABEiABEiABEiABEiABEiABEjAIAIULwaBZVgSIAESIAESIAESIAESIAESIAESIAESoHhhDZAACZAACZAACZAACZAACZAACZAACZCAQQQoXgwCy7AkQAIkQAIkQAIkQAIkQAIkQAIkQAIkQPHCGiABEiABEiABEiABEiABEiABEiABEiABgwhQvBgElmFJgARIgARIgARIgARIgARIgARIgARIgOKFNUACJEACJEACJEACJEACJEACJEACJEACBhGgeDEILMOSAAmQAAmQAAmQAAmQAAmQAAmQAAmQAMULa4AESIAESIAESIAESIAESIAESIAESIAEDCJA8WIQWIYlARIgARIgARIgARIgARIgARIgARIgAYoX1gAJkAAJkAAJkAAJkAAJkAAJkAAJkAAJGESA4sUgsAxLAiRAAiRAAiRAAiRAAiRAAiRAAiRAAhQvrAESIAESIAESIAESIAESIAESIAESIAESMIgAxYtBYBmWBEiABEiABEiABEiABEiABEiABEiABCheWAMkQAIkQAIkQAIkQAIkQAIkQAIkQAIkYBABiheDwDIsCZAACZAACZAACZAACZAACZAACZAACVC8sAZIgARIgARIgARIgARIgARIgARIgARIwCACFC8GgWVYEiABEiAB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",
      "text/html": [
       "<div>                            <div id=\"633378e7-9a9b-410c-8ff9-095a4b97057d\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"633378e7-9a9b-410c-8ff9-095a4b97057d\")) {                    Plotly.newPlot(                        \"633378e7-9a9b-410c-8ff9-095a4b97057d\",                        [{\"hovertemplate\":\"month_cat_first=1\\u003cbr\\u003epm_conc_mean=%{x}\\u003cbr\\u003epm_conc_std=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"1\",\"marker\":{\"color\":\"#636efa\",\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"1\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[7.583225806451614,7.880645161290323,7.723225806451612,7.32,11.034516129032257,7.998709677419355,8.159032258064517,8.855483870967742,8.460967741935484,6.365483870967742,7.153225806451613,11.263225806451612,6.9561290322580644,8.916774193548386],\"xaxis\":\"x\",\"y\":[2.9957810020621873,3.7258773354374433,3.5430858102888165,3.3880464862226662,4.335886073638159,3.6818208737303557,3.7806533782515843,4.180907268930734,4.0660934198472045,2.2476522220089565,3.8396829102515433,4.32301544996605,3.4648238625977763,3.82866443355699],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"month_cat_first=2\\u003cbr\\u003epm_conc_mean=%{x}\\u003cbr\\u003epm_conc_std=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"2\",\"marker\":{\"color\":\"#EF553B\",\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"2\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[4.399642857142857,4.499642857142858,4.7525,4.406785714285714,7.232142857142857,4.7275,4.652857142857143,4.931071428571428,4.795714285714285,4.1432142857142855,4.199285714285714,7.7124999999999995,4.147857142857143,5.2725],\"xaxis\":\"x\",\"y\":[1.7675237365594645,1.9345616166226813,1.84826892566605,1.8744370697360528,2.3328871129146584,1.9507750121805816,2.065622795527259,2.089673622018722,2.0544377054839815,1.4347537666852355,1.8572005090268797,2.8394439009543158,1.7900531665727828,1.9500426577145626],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"month_cat_first=3\\u003cbr\\u003epm_conc_mean=%{x}\\u003cbr\\u003epm_conc_std=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"3\",\"marker\":{\"color\":\"#00cc96\",\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"3\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[4.428387096774194,4.426774193548387,4.662903225806452,4.672258064516129,7.428709677419355,4.691612903225806,4.580967741935484,4.837096774193548,4.917419354838709,4.513225806451612,4.460967741935484,8.002903225806453,4.299032258064516,5.259677419354839],\"xaxis\":\"x\",\"y\":[1.3381565551407615,1.4241798439456765,1.5458032702495494,1.528309920709372,2.2076427781560817,1.512228150278464,1.4528193701659144,1.5096692652109536,1.6414789423807934,1.1964568555204615,1.5912980792028684,3.196387746137179,1.4660361674962887,1.7268966307188458],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"month_cat_first=4\\u003cbr\\u003epm_conc_mean=%{x}\\u003cbr\\u003epm_conc_std=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"4\",\"marker\":{\"color\":\"#ab63fa\",\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"4\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[3.7599999999999993,3.87,4.22,4.47,7.019999999999999,3.9,3.9200000000000004,3.84,3.8299999999999996,4.68],\"xaxis\":\"x\",\"y\":[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"month_cat_first=11\\u003cbr\\u003epm_conc_mean=%{x}\\u003cbr\\u003epm_conc_std=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"11\",\"marker\":{\"color\":\"#FFA15A\",\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"11\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[5.074,4.289444444444444,4.654444444444445,4.252777777777778,7.138333333333334,5.42,4.5216666666666665,5.625,5.37,5.101,5.012,7.913,4.631,5.799666666666667],\"xaxis\":\"x\",\"y\":[2.56295315194414,2.2531238544785936,2.1841878706242905,2.5088056721518153,2.8085508478873122,2.692928158894239,2.290457120363688,3.0413208904390028,2.8159214820558205,2.350662265670745,2.486085303087604,3.0264468184370243,2.380067324635726,2.7560896374184667],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"month_cat_first=12\\u003cbr\\u003epm_conc_mean=%{x}\\u003cbr\\u003epm_conc_std=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"12\",\"marker\":{\"color\":\"#19d3f3\",\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"12\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[10.446774193548388,11.355806451612903,11.243548387096775,8.184516129032259,14.46225806451613,10.958709677419353,11.296774193548387,12.026129032258064,11.77741935483871,9.751612903225807,10.11483870967742,14.170322580645163,9.86,12.273225806451613],\"xaxis\":\"x\",\"y\":[6.939570511007995,8.26435852987682,7.558531581256461,7.609356203606979,7.975611245425961,7.2963423448261535,7.9290978946350705,8.225558006368262,8.406064068175995,6.865905364375458,7.441130373810843,8.216440625912158,7.400116706696409,8.175230004745956],\"yaxis\":\"y\",\"type\":\"scatter\"}],                        {\"template\":{\"data\":{\"histogram2dcontour\":[{\"type\":\"histogram2dcontour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"choropleth\":[{\"type\":\"choropleth\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"histogram2d\":[{\"type\":\"histogram2d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmap\":[{\"type\":\"heatmap\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmapgl\":[{\"type\":\"heatmapgl\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"contourcarpet\":[{\"type\":\"contourcarpet\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"contour\":[{\"type\":\"contour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"surface\":[{\"type\":\"surface\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"mesh3d\":[{\"type\":\"mesh3d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"parcoords\":[{\"type\":\"parcoords\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolargl\":[{\"type\":\"scatterpolargl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"scattergeo\":[{\"type\":\"scattergeo\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolar\":[{\"type\":\"scatterpolar\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"scattergl\":[{\"type\":\"scattergl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatter3d\":[{\"type\":\"scatter3d\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattermapbox\":[{\"type\":\"scattermapbox\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterternary\":[{\"type\":\"scatterternary\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattercarpet\":[{\"type\":\"scattercarpet\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}]},\"layout\":{\"autotypenumbers\":\"strict\",\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"hovermode\":\"closest\",\"hoverlabel\":{\"align\":\"left\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"bgcolor\":\"#E5ECF6\",\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"ternary\":{\"bgcolor\":\"#E5ECF6\",\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]]},\"xaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"yaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"geo\":{\"bgcolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"subunitcolor\":\"white\",\"showland\":true,\"showlakes\":true,\"lakecolor\":\"white\"},\"title\":{\"x\":0.05},\"mapbox\":{\"style\":\"light\"}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"pm_conc_mean\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"pm_conc_std\"}},\"legend\":{\"title\":{\"text\":\"month_cat_first\"},\"tracegroupgap\":0},\"margin\":{\"t\":60}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('633378e7-9a9b-410c-8ff9-095a4b97057d');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "px.scatter(graph, x = 'pm_conc_mean', y = 'pm_conc_std', color = 'month_cat_first')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "0a577f4e-06ed-4f5b-b384-cdb12de8467d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Name</th>\n",
       "      <th>month</th>\n",
       "      <th>pm_conc_mean</th>\n",
       "      <th>pm_conc_median</th>\n",
       "      <th>pm_conc_std</th>\n",
       "      <th>asthma_rate_first</th>\n",
       "      <th>month_cat_first</th>\n",
       "      <th>threshold_&lt;lambda&gt;</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Belle Air School</td>\n",
       "      <td>1</td>\n",
       "      <td>7.583226</td>\n",
       "      <td>6.470</td>\n",
       "      <td>2.995781</td>\n",
       "      <td>8.1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Belle Air School</td>\n",
       "      <td>2</td>\n",
       "      <td>4.399643</td>\n",
       "      <td>4.045</td>\n",
       "      <td>1.767524</td>\n",
       "      <td>8.1</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Belle Air School</td>\n",
       "      <td>3</td>\n",
       "      <td>4.428387</td>\n",
       "      <td>4.010</td>\n",
       "      <td>1.338157</td>\n",
       "      <td>8.1</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Belle Air School</td>\n",
       "      <td>4</td>\n",
       "      <td>3.760000</td>\n",
       "      <td>3.760</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>8.1</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Belle Air School</td>\n",
       "      <td>11</td>\n",
       "      <td>5.074000</td>\n",
       "      <td>4.585</td>\n",
       "      <td>2.562953</td>\n",
       "      <td>8.1</td>\n",
       "      <td>11</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>80</th>\n",
       "      <td>San Bruno School District Office</td>\n",
       "      <td>2</td>\n",
       "      <td>5.272500</td>\n",
       "      <td>4.835</td>\n",
       "      <td>1.950043</td>\n",
       "      <td>8.2</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>81</th>\n",
       "      <td>San Bruno School District Office</td>\n",
       "      <td>3</td>\n",
       "      <td>5.259677</td>\n",
       "      <td>4.660</td>\n",
       "      <td>1.726897</td>\n",
       "      <td>8.2</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>82</th>\n",
       "      <td>San Bruno School District Office</td>\n",
       "      <td>4</td>\n",
       "      <td>4.680000</td>\n",
       "      <td>4.680</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>8.2</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>83</th>\n",
       "      <td>San Bruno School District Office</td>\n",
       "      <td>11</td>\n",
       "      <td>5.799667</td>\n",
       "      <td>5.150</td>\n",
       "      <td>2.756090</td>\n",
       "      <td>8.2</td>\n",
       "      <td>11</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>84</th>\n",
       "      <td>San Bruno School District Office</td>\n",
       "      <td>12</td>\n",
       "      <td>12.273226</td>\n",
       "      <td>10.810</td>\n",
       "      <td>8.175230</td>\n",
       "      <td>8.2</td>\n",
       "      <td>12</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>80 rows × 8 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                                Name  month  pm_conc_mean  pm_conc_median  \\\n",
       "0                   Belle Air School      1      7.583226           6.470   \n",
       "1                   Belle Air School      2      4.399643           4.045   \n",
       "2                   Belle Air School      3      4.428387           4.010   \n",
       "3                   Belle Air School      4      3.760000           3.760   \n",
       "4                   Belle Air School     11      5.074000           4.585   \n",
       "..                               ...    ...           ...             ...   \n",
       "80  San Bruno School District Office      2      5.272500           4.835   \n",
       "81  San Bruno School District Office      3      5.259677           4.660   \n",
       "82  San Bruno School District Office      4      4.680000           4.680   \n",
       "83  San Bruno School District Office     11      5.799667           5.150   \n",
       "84  San Bruno School District Office     12     12.273226          10.810   \n",
       "\n",
       "    pm_conc_std  asthma_rate_first month_cat_first  threshold_<lambda>  \n",
       "0      2.995781                8.1               1                   0  \n",
       "1      1.767524                8.1               2                   0  \n",
       "2      1.338157                8.1               3                   0  \n",
       "3      0.000000                8.1               4                   0  \n",
       "4      2.562953                8.1              11                   0  \n",
       "..          ...                ...             ...                 ...  \n",
       "80     1.950043                8.2               2                   0  \n",
       "81     1.726897                8.2               3                   0  \n",
       "82     0.000000                8.2               4                   0  \n",
       "83     2.756090                8.2              11                   0  \n",
       "84     8.175230                8.2              12                   5  \n",
       "\n",
       "[80 rows x 8 columns]"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "graph"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "id": "715ac12a-4e67-40f9-ac12-d5a68e675591",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hovertemplate": "day=Friday<br>pm_conc_mean=%{x}<br>pm_conc_std=%{y}<extra></extra>",
         "legendgroup": "Friday",
         "marker": {
          "color": "#636efa",
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Friday",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          7.264545454545455,
          7.755,
          7.8255,
          6.9565,
          11.0975,
          7.875,
          7.980499999999999,
          8.337272727272726,
          8.137727272727274,
          6.65590909090909,
          7.3536363636363635,
          10.790909090909091,
          6.957727272727273,
          8.580454545454545
         ],
         "xaxis": "x",
         "y": [
          4.67236922718685,
          5.5207254134677894,
          5.0068140185313075,
          3.820631945593186,
          5.404095785848569,
          4.912312761486861,
          5.2584270749940325,
          5.6229302493223745,
          5.228951394302942,
          3.9978992867825034,
          5.0617195698863195,
          5.538697551118906,
          4.770900836039538,
          5.534776192215448
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "day=Monday<br>pm_conc_mean=%{x}<br>pm_conc_std=%{y}<extra></extra>",
         "legendgroup": "Monday",
         "marker": {
          "color": "#EF553B",
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Monday",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          5.518636363636364,
          5.5275,
          5.562,
          4.4975,
          8.3035,
          5.568181818181818,
          5.627000000000001,
          5.915,
          5.806818181818182,
          5.116363636363636,
          4.819545454545454,
          8.782272727272728,
          4.879545454545455,
          6.393636363636364
         ],
         "xaxis": "x",
         "y": [
          2.5550961766751663,
          2.8556976097591,
          2.5481159607629613,
          1.8527680861364135,
          2.971669725860523,
          2.4035244683859305,
          2.5113341055898935,
          2.7220995923140268,
          2.661706195305911,
          2.039372869638568,
          2.0681873401753803,
          3.3609308968657023,
          2.399568916316733,
          3.076029767835563
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "day=Saturday<br>pm_conc_mean=%{x}<br>pm_conc_std=%{y}<extra></extra>",
         "legendgroup": "Saturday",
         "marker": {
          "color": "#00cc96",
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Saturday",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          6.880909090909091,
          7.056,
          7.232,
          6.619000000000001,
          10.408,
          7.233636363636363,
          7.117999999999999,
          7.766363636363637,
          7.537272727272727,
          6.540454545454545,
          7.027727272727272,
          10.792727272727273,
          6.575,
          8.035909090909092
         ],
         "xaxis": "x",
         "y": [
          4.061832764221559,
          4.405061826690937,
          4.084894074019496,
          4.1038498208335215,
          4.789257338939501,
          4.127601108282014,
          4.693719853230065,
          4.838522546490864,
          4.601185335704974,
          3.6765179443547717,
          3.8731822393068986,
          4.436590477487759,
          3.7596453936825656,
          4.500825264888008
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "day=Sunday<br>pm_conc_mean=%{x}<br>pm_conc_std=%{y}<extra></extra>",
         "legendgroup": "Sunday",
         "marker": {
          "color": "#ab63fa",
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Sunday",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          6.8986363636363635,
          7.2829999999999995,
          7.419,
          7.133,
          10.16,
          7.173181818181818,
          7.063,
          7.737272727272727,
          7.712272727272728,
          6.573181818181817,
          6.654090909090909,
          10.190454545454545,
          6.5240909090909085,
          8.124545454545455
         ],
         "xaxis": "x",
         "y": [
          5.931429500685424,
          7.807295280438648,
          7.265092893244708,
          7.158926911565705,
          7.87140650735562,
          6.335727406927462,
          7.105257052195773,
          7.313259439973646,
          7.832611880749542,
          5.7444072412908564,
          6.183906798651807,
          7.87738564153454,
          6.461968242698302,
          7.095744122632821
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "day=Thursday<br>pm_conc_mean=%{x}<br>pm_conc_std=%{y}<extra></extra>",
         "legendgroup": "Thursday",
         "marker": {
          "color": "#FFA15A",
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Thursday",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          6.0947619047619055,
          6.4575,
          6.547,
          5.2764999999999995,
          9.4805,
          6.646666666666667,
          6.8745,
          7.208571428571428,
          6.9452380952380945,
          5.5495238095238095,
          5.9261904761904765,
          9,
          5.763809523809524,
          7.322857142857143
         ],
         "xaxis": "x",
         "y": [
          3.760841532064868,
          4.587791082885315,
          4.31361141438858,
          3.6281805888730028,
          4.876042727126954,
          4.460060911392728,
          4.71554218847771,
          4.935534708331294,
          4.90956272904993,
          3.1139952018614463,
          4.2430128947374675,
          5.03355313301222,
          3.999666423819805,
          4.502470628248646
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "day=Tuesday<br>pm_conc_mean=%{x}<br>pm_conc_std=%{y}<extra></extra>",
         "legendgroup": "Tuesday",
         "marker": {
          "color": "#19d3f3",
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Tuesday",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          5.281818181818182,
          5.318,
          5.4615,
          4.466,
          7.9905,
          5.493181818181818,
          5.6475,
          5.870909090909091,
          5.634545454545455,
          5.000909090909091,
          4.960909090909091,
          8.702272727272726,
          4.8136363636363635,
          6.208181818181818
         ],
         "xaxis": "x",
         "y": [
          2.4888202067816656,
          2.5764739823677982,
          2.4429868186217454,
          1.7171093027358217,
          2.8542056069009205,
          2.5371063126243727,
          3.009436127928421,
          2.7514185243441056,
          2.767756057363725,
          2.081739985638577,
          2.3518954079653156,
          3.189993180793102,
          2.248758159751928,
          2.8458300998943264
         ],
         "yaxis": "y"
        },
        {
         "hovertemplate": "day=Wednesday<br>pm_conc_mean=%{x}<br>pm_conc_std=%{y}<extra></extra>",
         "legendgroup": "Wednesday",
         "marker": {
          "color": "#FF6692",
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "Wednesday",
         "orientation": "v",
         "showlegend": true,
         "type": "scatter",
         "x": [
          6.990952380952381,
          7.6345,
          7.6325,
          6.546,
          10.495,
          7.568095238095238,
          7.725,
          8.24,
          7.954761904761905,
          6.5928571428571425,
          6.808571428571429,
          10.902857142857142,
          6.568095238095238,
          8.13904761904762
         ],
         "xaxis": "x",
         "y": [
          5.741937411544576,
          6.709972583454203,
          6.299585424069705,
          5.570684601319152,
          6.976119076803189,
          6.368033934463305,
          6.708123749784601,
          7.0590332199246655,
          6.846965473147663,
          5.736191733580355,
          6.328795065257047,
          6.737115957779815,
          5.941316076561802,
          6.817129799236162
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "autosize": true,
        "legend": {
         "title": {
          "text": "day"
         },
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "xaxis": {
         "anchor": "y",
         "autorange": true,
         "domain": [
          0,
          1
         ],
         "range": [
          4.062918611215657,
          11.500581388784344
         ],
         "title": {
          "text": "pm_conc_mean"
         },
         "type": "linear"
        },
        "yaxis": {
         "anchor": "x",
         "autorange": true,
         "domain": [
          0,
          1
         ],
         "range": [
          1.2401325258472071,
          8.354362418423154
         ],
         "title": {
          "text": "pm_conc_std"
         },
         "type": "linear"
        }
       }
      },
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABF4AAAFoCAYAAABuXz/oAAAAAXNSR0IArs4c6QAAIABJREFUeF7snXmAjdX/x993mdWYMcMMY993ZQlFIkkqEalEZW0V0deWrSSVSEWSyhIVpVIUoWQpJYqQNcnOzGDMjNnvvb/f80wzzZ1rzJ25z3mW+7yff77f5j7n8/mc1+fM+Mx7zvkci8vlcoEPCZAACZAACZAACZAACZAACZAACZAACZCA4gQsFF4UZ0qDJEACJEACJEACJEACJEACJEACJEACJCAToPDChUACJEACJEACJEACJEACJEACJEACJEACgghQeBEElmZJgARIgARIgARIgARIgARIgARIgARIgMIL1wAJkAAJkAAJkAAJkAAJkAAJkAAJkAAJCCJA4UUQWJolARIgARIgARIgARIgARIgARIgARIgAQovXAMkQAIkQAIkQAIkQAIkQAIkQAIkQAIkIIgAhRdBYGmWBEiABEiABEiABEiABEiABEiABEiABCi8cA2QAAmQAAmQAAmQAAmQAAmQAAmQAAmQgCACFF4EgaVZEiABEiABEiABEiABEiABEiABEiABEqDwwjVAAiRAAiRAAiRAAiRAAiRAAiRAAiRAAoIIUHgRBJZmSYAESIAESIAESIAESIAESIAESIAESIDCC9cACZAACZAACZAACZAACZAACZAACZAACQgiQOFFEFiaJQESIAESIAESIAESIAESIAESIAESIAEKL1wDJEACJEACJEACJEACJEACJEACJEACJCCIAIUXQWBplgRIgARIgARIgARIgARIgARIgARIgAQovHANkAAJkAAJkAAJkAAJkAAJkAAJkAAJkIAgAhReBIGlWRIgARIgARIgARIgARIgARIgARIgARKg8MI1QAIkQAIkQAIkQAIkQAIkQAIkQAIkQAKCCFB4EQSWZkmABEiABEiABEiABEiABEiABEiABEiAwgvXAAmQAAmQAAmQAAmQAAmQAAmQAAmQAAkIIkDhRRBYmiUBEiABEiABEiABEiABEiABEiABEiABCi9cAyRAAiRAAiRAAiRAAiRAAiRAAiRAAiQgiACFF0FgaZYESIAESIAESIAESIAESIAESIAESIAEKLxwDZAACZAACZAACZAACZAACZAACZAACZCAIAIUXgSBpVkSIAESIAESIAESIAESIAESIAESIAESoPDCNUACJEACJEACJEACJEACJEACJEACJEACgghQeBEElmZJgARIgARIgARIgARIgARIgARIgARIgMIL1wAJkAAJkAAJkAAJkAAJkAAJkAAJkAAJCCJA4UUQWJolARIgARIgARIgARIgARIgARIgARIgAQovXAMkQAIkQAIkQAIkQAIkQAIkQAIkQAIkIIgAhRdBYGmWBEiABEiABEiABEiABEiABEiABEiABCi8cA2QAAmQAAmQAAmQAAmQAAmQAAmQAAmQgCACFF4EgaVZEiABEiABEiABEiABEiABEiABEiABEqDwwjVAAiRAAiRAAiRAAiRAAiRAAiRAAiRAAoIIUHgRBJZmSYAESIAESIAESIAESIAESIAESIAESIDCC9cACZAACZAACZAACZAACZAACZAACZAACQgiQOFFEFiaJQESIAESIAESIAESIAESIAESIAESIAEKL1wDJEACJEACJEACJEACJEACJEACJEACJCCIAIUXQWBplgRIgARIgARIgARIgARIgARIgARIgAQovHANkAAJkAAJkAAJkAAJkAAJkAAJkAAJkIAgAhReBIGlWRIgARIgARIgARIgARIgARIgARIgARKg8MI1QAIkQAIkQAIkQAIkQAIkQAIkQAIkQAKCCFB4EQSWZkmABEiABEiABEiABEiABEiABEiABEiAwgvXAAmQAAmQAAmQAAmQAAmQAAmQAAmQAAkIIkDhRRBYmiUBEiABEiABEiABEiABEiABEiABEiABCi9cAyRAAiRAAiRAAiRAAiRAAiRAAiRAAiQgiACFF0FgaZYESIAESIAESIAESIAESIAESIAESIAEKLxwDZAACZAACZAACZAACZAACZAACZAACZCAIAIUXgSBpVkSIAESIAESIAESIAESIAESIAESIAESoPDCNUACJEACJEACJEACJEACJEACJEACJEACgghQeBEElmZJgARIgARIgARIgARIgARIgARIgARIgMIL1wAJkAAJkAAJkAAJkAAJkAAJkAAJkAAJCCJA4UUQWJolARIgARIgARIgARIgARIgARIgARIgAQovXAMkQAIkQAIkQAIkQAIkQAIkQAIkQAIkIIgAhRdBYGmWBEiABEiABEiABEiABEiABEiABEiABCi8cA2QAAmQAAmQAAmQAAmQAAmQAAmQAAmQgCACFF4EgaVZEiAB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n5No9exwj8gfa1w3s+G5EE/FleJZn3ULx6N8mRIGnC1DJgH1CFB4UY8tLeuYgFDvxe03ogAUOyEyVHsdh8zQ/CAQe/4ygoIcmb1e/DDBISRAAhoRyLjCtHiRGI0ioFu1CJw5dxHBQUEoFF1ALRe0qzMCYleMyHvRQgW5G0JnuWE4JEACgSFA4SUwnOmFBEiABEiABEiABEiABEiABEiABEjAggQovFgw6ZwyCZAACZAACZAACZAACZAACZAACZBAYAhQeAkMZ3ohARIgARIgARIgARIgARIgARIgARKwIAEKLxZMOqdMAiRAAiRAAiRAAiRAAiRAAiRAAiQQGAIUXgLDmV5IgARIgARIgARIgARIgARIgARIgAQsSIDCiwWTzimTAAmQAAmQAAmQAAmQAAmQAAmQAAkEhgCFl8BwphcSIAESIAESIAESIAESIAESIAESIAELEqDwYsGkc8okQAIkQAIkQAIkQAIkQAIkQAIkQAKBIUDhJTCc6YUESIAESIAESIAESIAESIAESIAESMCCBCi8WDDpnDIJkAAJkAAJkAAJkAAJkAAJkAAJkEBgCFB4CQxneiEBEiABEiABEiABEiABEiABEiABErAgAQovFkw6p0wCJEACJEACJEACJEACJEACJEACJBAYAhReAsOZXkiABEiABEiABEiABEiABEiABEiABCxIgMKLBZPOKZMACZAACZAACZAACZAACZAACZAACQSGAIWXwHCmFxIgAYFuA14AAA2ESURBVBIgARIgARIgARIgARIgARIgAQsSoPBiwaRzyiRAAiRAAiRAAiRAAiRAAiRAAiRAAoEhQOElMJzphQRIgARIgARIgARIgARIgARIgARIwIIEKLxYMOmcMgmQAAmQAAmQAAmQAAmQAAmQAAmQQGAIUHgJDGd6IQESIAESsBiB5Wu24Lt9v+GeGlWwct12/H30FBo8UBMjB3VD4ZgoicaIt+ehUHQBpKSkYu3X30tf69y2Mdo0fxhT53yKHT/8jJLFCqNL+yZo0fB+nwgeO3kW0+Z+hgO/H0Zqahpq1aiC3l0eR9Vby0h//mDhGnz5zQ84cfocate8DYN6d8DtVcpJPn7+429MmrkMT7duhBVrt+L3g//ikbp3oWv7ppnviPd27fsdcxevw69//YMihaJQp9bteLF7a0RHReYZa4aPp1o1wLI1W7D/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yae4ilocxcn6iNuMrl6Ll4SSIIfDr9jE8aXY85eQL194QK9iFk10z52/jLCwEOnYVvbn9NkL0i4YITjxIQESIAESIAESIAEtCVB40ZI+fZMACZAACZiWQG49XuROVjTnHfLmrJuaETtapo15Ua4rv8eL65/FLpWbPf17tEHnto399sGBJEACJEACJEACJGAkAhRejJQtxkoCJEACJGAYAkJ82LXvN7w39iXFYha7S1JS025qTzS2DQ0JVsynr4ZSU9OQ5nTddFhwsMPvHTa+xsP3SYAESIAESIAESEBrAhRetM4A/ZMACZAACZAACZAACZAACZAACZAACZiWAIUX06aWEyMBEiABEiABEiABEiABEiABEiABEtCaAIUXrTNA/yRAAiRAAiRAAiRAAiRAAiRAAiRAAqYlQOHFtKnlxEiABEiABEiABEiABEiABEiABEiABLQmQOFF6wzQPwmQAAmQAAmQAAmQAAmQAAmQAAmQgGkJUHgxbWo5MRIgARIgARIgARIgARIgARIgARIgAa0JUHjROgP0TwIkQAIkQAIkQAIkQAIkQAIkQAIkYFoCFF5Mm1pOjARIgARIgARIgARIgARIgARIgARIQGsCFF60zgD9kwAJkAAJkAAJkAAJkAAJkAAJkAAJmJYAhRfTppYTIwESIAESIAESIAESIAESIAESIAES0JoAhRetM0D/JEACJEACJEACJEACJEACJEACJEACpiVA4cW0qeXESIAESIAESIAESIAESIAESIAESIAEtCZA4UXrDNA/CZAACZAACZAACZAACZAACZAACZCAaQlQeDFtajkxEiABEiABEiABEiABEiABEiABEiABrQlQeNE6A/RPAiRAAiRAAiRAAiRAAiRAAiRAAiRgWgIUXkybWk6MBEiABEiABEiABEiABEiABEiABEhAawIUXrTOAP2TAAmQAAmQAAmQAAmQAAmQAAmQAAmYlgCFF9OmlhMjARIgARIgARIgARIgARIgARIgARLQmgCFF60zQP8kQAIkQAIkQAIkQAIkQAIkQAIkQAKmJUDhxbSp5cRIgARIgARIgARIgARIgARIgARIgAS0JkDhResM0D8JkAAJkAAJkAAJkAAJkAAJkAAJkIBpCVB4MW1qOTESIAESIAESIAESIAESIAESIAESIAGtCVB40ToD9E8CJEACJEACJEACJEACJEACJEACJGBaAhReTJtaTowESIAESIAESIAESIAESIAESIAESEBrAhRetM4A/ZMACZAACZAACZAACZAACZAACZAACZiWAIUX06aWEyMBEiABEiABEiABEiABEiABEiABEtCaAIUXrTNA/yRAAiRAAiRAAiRAAiRAAiRAAiRAAqYlQOHFtKnlxEiABEiABEiABEiABEiABEiABEiABLQmQOFF6wzQPwmQAAmQAAmQAAmQAAmQAAmQAAmQgGkJUHgxbWo5MRIgARIgARIgARIgARIgARIgARIgAa0JUHjROgP0TwIkQAIkQAIkQAIkQAIkQAIkQAIkYFoCFF5Mm1pOjARIgARIgARIgARIgARIgARIgARIQGsCFF60zgD9kwAJkAAJkAAJkAAJkAAJkAAJkAAJmJYAhRfTppYTIwESIAESIAESIAESIAESIAESIAES0JoAhRetM0D/JEACJEACJEACJEACJEACJEACJEACpiVA4cW0qeXESIAESIAESIAESIAESIAESIAESIAEtCZA4UXrDNA/CZAACZAACZAACZAACZAACZAACZCAaQn8H2rP+WrGxfTXAAAAAElFTkSuQmCC",
      "text/html": [
       "<div>                            <div id=\"bcc0ad7e-dc7a-4ea5-ae2a-b6b5458a9403\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"bcc0ad7e-dc7a-4ea5-ae2a-b6b5458a9403\")) {                    Plotly.newPlot(                        \"bcc0ad7e-dc7a-4ea5-ae2a-b6b5458a9403\",                        [{\"hovertemplate\":\"day=Friday\\u003cbr\\u003epm_conc_mean=%{x}\\u003cbr\\u003epm_conc_std=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"Friday\",\"marker\":{\"color\":\"#636efa\",\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Friday\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[7.264545454545455,7.755,7.8255,6.9565,11.0975,7.875,7.980499999999999,8.337272727272726,8.137727272727274,6.65590909090909,7.3536363636363635,10.790909090909091,6.957727272727273,8.580454545454545],\"xaxis\":\"x\",\"y\":[4.67236922718685,5.5207254134677894,5.0068140185313075,3.820631945593186,5.404095785848569,4.912312761486861,5.2584270749940325,5.6229302493223745,5.228951394302942,3.9978992867825034,5.0617195698863195,5.538697551118906,4.770900836039538,5.534776192215448],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"day=Monday\\u003cbr\\u003epm_conc_mean=%{x}\\u003cbr\\u003epm_conc_std=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"Monday\",\"marker\":{\"color\":\"#EF553B\",\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Monday\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[5.518636363636364,5.5275,5.562,4.4975,8.3035,5.568181818181818,5.627000000000001,5.915,5.806818181818182,5.116363636363636,4.819545454545454,8.782272727272728,4.879545454545455,6.393636363636364],\"xaxis\":\"x\",\"y\":[2.5550961766751663,2.8556976097591,2.5481159607629613,1.8527680861364135,2.971669725860523,2.4035244683859305,2.5113341055898935,2.7220995923140268,2.661706195305911,2.039372869638568,2.0681873401753803,3.3609308968657023,2.399568916316733,3.076029767835563],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"day=Saturday\\u003cbr\\u003epm_conc_mean=%{x}\\u003cbr\\u003epm_conc_std=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"Saturday\",\"marker\":{\"color\":\"#00cc96\",\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Saturday\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[6.880909090909091,7.056,7.232,6.619000000000001,10.408,7.233636363636363,7.117999999999999,7.766363636363637,7.537272727272727,6.540454545454545,7.027727272727272,10.792727272727273,6.575,8.035909090909092],\"xaxis\":\"x\",\"y\":[4.061832764221559,4.405061826690937,4.084894074019496,4.1038498208335215,4.789257338939501,4.127601108282014,4.693719853230065,4.838522546490864,4.601185335704974,3.6765179443547717,3.8731822393068986,4.436590477487759,3.7596453936825656,4.500825264888008],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"day=Sunday\\u003cbr\\u003epm_conc_mean=%{x}\\u003cbr\\u003epm_conc_std=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"Sunday\",\"marker\":{\"color\":\"#ab63fa\",\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Sunday\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[6.8986363636363635,7.2829999999999995,7.419,7.133,10.16,7.173181818181818,7.063,7.737272727272727,7.712272727272728,6.573181818181817,6.654090909090909,10.190454545454545,6.5240909090909085,8.124545454545455],\"xaxis\":\"x\",\"y\":[5.931429500685424,7.807295280438648,7.265092893244708,7.158926911565705,7.87140650735562,6.335727406927462,7.105257052195773,7.313259439973646,7.832611880749542,5.7444072412908564,6.183906798651807,7.87738564153454,6.461968242698302,7.095744122632821],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"day=Thursday\\u003cbr\\u003epm_conc_mean=%{x}\\u003cbr\\u003epm_conc_std=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"Thursday\",\"marker\":{\"color\":\"#FFA15A\",\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Thursday\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[6.0947619047619055,6.4575,6.547,5.2764999999999995,9.4805,6.646666666666667,6.8745,7.208571428571428,6.9452380952380945,5.5495238095238095,5.9261904761904765,9.0,5.763809523809524,7.322857142857143],\"xaxis\":\"x\",\"y\":[3.760841532064868,4.587791082885315,4.31361141438858,3.6281805888730028,4.876042727126954,4.460060911392728,4.71554218847771,4.935534708331294,4.90956272904993,3.1139952018614463,4.2430128947374675,5.03355313301222,3.999666423819805,4.502470628248646],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"day=Tuesday\\u003cbr\\u003epm_conc_mean=%{x}\\u003cbr\\u003epm_conc_std=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"Tuesday\",\"marker\":{\"color\":\"#19d3f3\",\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Tuesday\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[5.281818181818182,5.318,5.4615,4.466,7.9905,5.493181818181818,5.6475,5.870909090909091,5.634545454545455,5.000909090909091,4.960909090909091,8.702272727272726,4.8136363636363635,6.208181818181818],\"xaxis\":\"x\",\"y\":[2.4888202067816656,2.5764739823677982,2.4429868186217454,1.7171093027358217,2.8542056069009205,2.5371063126243727,3.009436127928421,2.7514185243441056,2.767756057363725,2.081739985638577,2.3518954079653156,3.189993180793102,2.248758159751928,2.8458300998943264],\"yaxis\":\"y\",\"type\":\"scatter\"},{\"hovertemplate\":\"day=Wednesday\\u003cbr\\u003epm_conc_mean=%{x}\\u003cbr\\u003epm_conc_std=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"Wednesday\",\"marker\":{\"color\":\"#FF6692\",\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"Wednesday\",\"orientation\":\"v\",\"showlegend\":true,\"x\":[6.990952380952381,7.6345,7.6325,6.546,10.495,7.568095238095238,7.725,8.24,7.954761904761905,6.5928571428571425,6.808571428571429,10.902857142857142,6.568095238095238,8.13904761904762],\"xaxis\":\"x\",\"y\":[5.741937411544576,6.709972583454203,6.299585424069705,5.570684601319152,6.976119076803189,6.368033934463305,6.708123749784601,7.0590332199246655,6.846965473147663,5.736191733580355,6.328795065257047,6.737115957779815,5.941316076561802,6.817129799236162],\"yaxis\":\"y\",\"type\":\"scatter\"}],                        {\"template\":{\"data\":{\"histogram2dcontour\":[{\"type\":\"histogram2dcontour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"choropleth\":[{\"type\":\"choropleth\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"histogram2d\":[{\"type\":\"histogram2d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmap\":[{\"type\":\"heatmap\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmapgl\":[{\"type\":\"heatmapgl\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"contourcarpet\":[{\"type\":\"contourcarpet\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"contour\":[{\"type\":\"contour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"surface\":[{\"type\":\"surface\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"mesh3d\":[{\"type\":\"mesh3d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"parcoords\":[{\"type\":\"parcoords\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolargl\":[{\"type\":\"scatterpolargl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"scattergeo\":[{\"type\":\"scattergeo\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolar\":[{\"type\":\"scatterpolar\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"scattergl\":[{\"type\":\"scattergl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatter3d\":[{\"type\":\"scatter3d\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattermapbox\":[{\"type\":\"scattermapbox\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterternary\":[{\"type\":\"scatterternary\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattercarpet\":[{\"type\":\"scattercarpet\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}]},\"layout\":{\"autotypenumbers\":\"strict\",\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"hovermode\":\"closest\",\"hoverlabel\":{\"align\":\"left\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"bgcolor\":\"#E5ECF6\",\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"ternary\":{\"bgcolor\":\"#E5ECF6\",\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]]},\"xaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"yaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"geo\":{\"bgcolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"subunitcolor\":\"white\",\"showland\":true,\"showlakes\":true,\"lakecolor\":\"white\"},\"title\":{\"x\":0.05},\"mapbox\":{\"style\":\"light\"}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"pm_conc_mean\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"pm_conc_std\"}},\"legend\":{\"title\":{\"text\":\"day\"},\"tracegroupgap\":0},\"margin\":{\"t\":60}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('bcc0ad7e-dc7a-4ea5-ae2a-b6b5458a9403');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "graph = clarity_cleaned.groupby([\"Name\", \"day\"]).agg({\n",
    "    \"pm_conc\": [\"mean\", \"median\", \"std\"],\n",
    "    \"asthma_rate\": \"first\",\n",
    "    \"month_cat\": \"first\",\n",
    "    \"Longitude\": \"first\"\n",
    "    \n",
    "}).reset_index()\n",
    "graph.columns = ['_'.join(col).strip('_') for col in graph.columns.values]\n",
    "\n",
    "\n",
    "px.scatter(graph, x = 'pm_conc_mean', y = 'pm_conc_std', color = 'day')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "id": "0a28ee4f-1bc8-4c84-8c7b-9977cb3344c0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "hovertemplate": "pm_conc_mean=%{x}<br>asthma_rate_first=%{y}<br>Longitude_first=%{marker.color}<extra></extra>",
         "legendgroup": "",
         "marker": {
          "color": [
           122.40469,
           122.40469,
           122.40469,
           122.40469,
           122.40469,
           122.40469,
           122.40469,
           122.4327,
           122.4327,
           122.4327,
           122.4327,
           122.4327,
           122.4327,
           122.4327,
           122.44095,
           122.44095,
           122.44095,
           122.44095,
           122.44095,
           122.44095,
           122.44095,
           122.46329,
           122.46329,
           122.46329,
           122.46329,
           122.46329,
           122.46329,
           122.46329,
           122.407,
           122.407,
           122.407,
           122.407,
           122.407,
           122.407,
           122.407,
           122.41898,
           122.41898,
           122.41898,
           122.41898,
           122.41898,
           122.41898,
           122.41898,
           122.40165,
           122.40165,
           122.40165,
           122.40165,
           122.40165,
           122.40165,
           122.40165,
           122.40707,
           122.40707,
           122.40707,
           122.40707,
           122.40707,
           122.40707,
           122.40707,
           122.41055,
           122.41055,
           122.41055,
           122.41055,
           122.41055,
           122.41055,
           122.41055,
           122.41844,
           122.41844,
           122.41844,
           122.41844,
           122.41844,
           122.41844,
           122.41844,
           122.45347,
           122.45347,
           122.45347,
           122.45347,
           122.45347,
           122.45347,
           122.45347,
           122.41276,
           122.41276,
           122.41276,
           122.41276,
           122.41276,
           122.41276,
           122.41276,
           122.44371,
           122.44371,
           122.44371,
           122.44371,
           122.44371,
           122.44371,
           122.44371,
           122.41611,
           122.41611,
           122.41611,
           122.41611,
           122.41611,
           122.41611,
           122.41611
          ],
          "coloraxis": "coloraxis",
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "",
         "orientation": "v",
         "showlegend": false,
         "type": "scatter",
         "x": [
          7.264545454545455,
          5.518636363636364,
          6.880909090909091,
          6.8986363636363635,
          6.0947619047619055,
          5.281818181818182,
          6.990952380952381,
          7.755,
          5.5275,
          7.056,
          7.2829999999999995,
          6.4575,
          5.318,
          7.6345,
          7.8255,
          5.562,
          7.232,
          7.419,
          6.547,
          5.4615,
          7.6325,
          6.9565,
          4.4975,
          6.619000000000001,
          7.133,
          5.2764999999999995,
          4.466,
          6.546,
          11.0975,
          8.3035,
          10.408,
          10.16,
          9.4805,
          7.9905,
          10.495,
          7.875,
          5.568181818181818,
          7.233636363636363,
          7.173181818181818,
          6.646666666666667,
          5.493181818181818,
          7.568095238095238,
          7.980499999999999,
          5.627000000000001,
          7.117999999999999,
          7.063,
          6.8745,
          5.6475,
          7.725,
          8.337272727272726,
          5.915,
          7.766363636363637,
          7.737272727272727,
          7.208571428571428,
          5.870909090909091,
          8.24,
          8.137727272727274,
          5.806818181818182,
          7.537272727272727,
          7.712272727272728,
          6.9452380952380945,
          5.634545454545455,
          7.954761904761905,
          6.65590909090909,
          5.116363636363636,
          6.540454545454545,
          6.573181818181817,
          5.5495238095238095,
          5.000909090909091,
          6.5928571428571425,
          7.3536363636363635,
          4.819545454545454,
          7.027727272727272,
          6.654090909090909,
          5.9261904761904765,
          4.960909090909091,
          6.808571428571429,
          10.790909090909091,
          8.782272727272728,
          10.792727272727273,
          10.190454545454545,
          9,
          8.702272727272726,
          10.902857142857142,
          6.957727272727273,
          4.879545454545455,
          6.575,
          6.5240909090909085,
          5.763809523809524,
          4.8136363636363635,
          6.568095238095238,
          8.580454545454545,
          6.393636363636364,
          8.035909090909092,
          8.124545454545455,
          7.322857142857143,
          6.208181818181818,
          8.13904761904762
         ],
         "xaxis": "x",
         "y": [
          8.1,
          8.1,
          8.1,
          8.1,
          8.1,
          8.1,
          8.1,
          8.1,
          8.1,
          8.1,
          8.1,
          8.1,
          8.1,
          8.1,
          7.9,
          7.9,
          7.9,
          7.9,
          7.9,
          7.9,
          7.9,
          6.2,
          6.2,
          6.2,
          6.2,
          6.2,
          6.2,
          6.2,
          8.6,
          8.6,
          8.6,
          8.6,
          8.6,
          8.6,
          8.6,
          9.2,
          9.2,
          9.2,
          9.2,
          9.2,
          9.2,
          9.2,
          8.6,
          8.6,
          8.6,
          8.6,
          8.6,
          8.6,
          8.6,
          9.1,
          9.1,
          9.1,
          9.1,
          9.1,
          9.1,
          9.1,
          9.1,
          9.1,
          9.1,
          9.1,
          9.1,
          9.1,
          9.1,
          8,
          8,
          8,
          8,
          8,
          8,
          8,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          7.2,
          9.1,
          9.1,
          9.1,
          9.1,
          9.1,
          9.1,
          9.1,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          7.6,
          8.2,
          8.2,
          8.2,
          8.2,
          8.2,
          8.2,
          8.2
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "autosize": true,
        "coloraxis": {
         "colorbar": {
          "title": {
           "text": "Longitude_first"
          }
         },
         "colorscale": [
          [
           0,
           "#0d0887"
          ],
          [
           0.1111111111111111,
           "#46039f"
          ],
          [
           0.2222222222222222,
           "#7201a8"
          ],
          [
           0.3333333333333333,
           "#9c179e"
          ],
          [
           0.4444444444444444,
           "#bd3786"
          ],
          [
           0.5555555555555556,
           "#d8576b"
          ],
          [
           0.6666666666666666,
           "#ed7953"
          ],
          [
           0.7777777777777778,
           "#fb9f3a"
          ],
          [
           0.8888888888888888,
           "#fdca26"
          ],
          [
           1,
           "#f0f921"
          ]
         ]
        },
        "legend": {
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "xaxis": {
         "anchor": "y",
         "autorange": true,
         "domain": [
          0,
          1
         ],
         "range": [
          4.062482660060976,
          11.501017339939025
         ],
         "title": {
          "text": "pm_conc_mean"
         },
         "type": "linear"
        },
        "yaxis": {
         "anchor": "x",
         "autorange": true,
         "domain": [
          0,
          1
         ],
         "range": [
          5.9677165354330715,
          9.432283464566929
         ],
         "title": {
          "text": "asthma_rate_first"
         },
         "type": "linear"
        }
       }
      },
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABF4AAAFoCAYAAABuXz/oAAAAAXNSR0IArs4c6QAAIABJREFUeF7snQd4FFXbhp9NDwmEhN57B+lKl6L0IiIo8ElREURQRBAEkSKgCAqIIAIqiCCCCgiIoAhKF0Tp0nsNJb1n9/9nwibZbJLdZObMzC7PXNf3xWTPed9z7ncSsnfOnGOyWCwW8CIBEiABEiABEiABEiABEiABEiABEiABElCdgIniRXWmDEgCJEACJEACJEACJEACJEACJEACJEACMgGKF94IJEACJEACJEACJEACJEACJEACJEACJCCIAMWLILAMSwIkQAIkQAIkQAIkQAIkQAIkQAIkQAIUL7wHSIAESIAESIAESIAESIAESIAESIAESEAQAYoXQWAZlgRIgARIgARIgARIgARIgARIgARIgAQoXngPkAAJkAAJkAAJkAAJkAAJkAAJkAAJkIAgAhQvgsAyLAmQAAmQAAmQAAmQAAmQAAmQAAmQAAlQvPAeIAESIAESIAESIAESIAESIAESIAESIAFBBCheBIFlWBIgARIgARIgARIgARIgARIgARIgARKgeOE9QAIkQAIkQAIkQAIkQAIkQAIkQAIkQAKCCFC8CALLsCRAAiRAAiRAAiRAAiRAAiRAAiRAAiRA8cJ7gARIgARIgARIgARIgARIgARIgARIgAQEEaB4EQSWYUmABEiABEiABEiABEiABEiABEiABEiA4oX3AAmQAAmQAAmQAAmQAAmQAAmQAAmQAAkIIkDxIggsw5IACZAACZAACZAACZAACZAACZAACZAAxQvvARIgARIgARIgARIgARIgARIgARIgARIQRIDiRRBYhiUBEiABEiABEiABEiABEiABEiABEiABihfeAyRAAiRAAiRAAiRAAiRAAiRAAiRAAiQgiADFiyCwDEsCJEACJEACJEACJEACJEACJEACJEACFC+8B0iABEiABEiABEiABEiABEiABEiABEhAEAGKF0FgGZYESIAESIAESIAESIAESIAESIAESIAEKF54D5AACZAACZAACZAACZAACZAACZAACZCAIAIUL4LAMiwJkAAJkAAJkAAJkAAJkAAJkAAJkAAJULzwHiABEiABEiABEiABEiABEiABEiABEiABQQQoXgSBZVgSIAESIAESIAESIAESIAESIAESIAESoHjhPUACJEACJEACJEACJEACJEACJEACJEACgghQvAgCy7AkQAIkQAIkQAIkQAIkQAIkQAIkQAIkQPHCe4AESIAESIAESIAESIAESIAESIAESIAEBBGgeBEElmFJgARIgARIgARIgARIgARIgARIgARIgOKF9wAJkAAJkAAJkAAJkAAJkAAJkAAJkAAJCCJA8SIILMOSAAmQAAmQAAmQAAmQAAmQAAmQAAmQAMUL7wESIAESIAESIAESIAESIAESIAESIAESEESA4kUQWIYlARIgARIgARIgARIgARIgARIgARIgAYoX3gMkQAIkQAIkQAIkQAIkQAIkQAIkQAIkIIgAxYsgsAxLAiRAAiRAAiRAAiRAAiRAAiRAAiRAAhQvvAdIgARIgARIgARIgARIgARIgARIgARIQBABihdBYBmWBEiABEiABEiABEiABEiABEiABEiABCheeA+QAAmQAAmQAAmQAAmQAAmQAAmQAAmQgCACFC+CwDIsCZAACZAACZAACZAACZAACZAACZAACVC88B4gARIgARIgARIgARIgARIgARIgARIgAUEEKF4EgWVYEiABEiABEiABEiABEiABEiABEiABEqB44T1AAiRAAiRAAiRAAiRAAiRAAiRAAiRAAoIIULwIAsuwJEACJEACJEACJEACJEACJEACJEACJEDxwnuABEiABEiABEiABEiABEiABEiABEiABAQRoHgRBJZhSYAESIAESIAESIAESIAESIAESIAESIDihfcACZAACZAACZAACZAACZAACZAACZAACQgiQPEiCCzDkgAJkAAJkAAJkAAJkAAJkAAJkAAJkADFC+8BEiABEiABEiABEiABEiABEiABEiABEhBEgOJFEFiGJQESIAESIAESIAESIAESIAESIAESIAGKF94DJEACJEACJEACJEACJEACJEACJEACJCCIAMWLILAMSwIkQAIkQAIkQAIkQAIkQAIkQAIkQAIUL7wHSIAESIAESIAESIAESIAESIAESIAESEAQAYoXQWAZlgRIgARIgARIgARIgARIgARIgARIgAQoXngPkAAJkAAJkAAJkAAJkAAJkAAJkAAJkIAgAhQvgsAyLAmQAAmQAAmQAAmQAAmQAAmQAAmQAAlQvPAeIAESIAESIAESIAESIAESIAESIAESIAFBBCheBIFlWBIgARIgARIgARIg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",
      "text/html": [
       "<div>                            <div id=\"44c7b69e-b9e7-4ea1-8fa7-5aaed541b6d2\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"44c7b69e-b9e7-4ea1-8fa7-5aaed541b6d2\")) {                    Plotly.newPlot(                        \"44c7b69e-b9e7-4ea1-8fa7-5aaed541b6d2\",                        [{\"hovertemplate\":\"pm_conc_mean=%{x}\\u003cbr\\u003easthma_rate_first=%{y}\\u003cbr\\u003eLongitude_first=%{marker.color}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"\",\"marker\":{\"color\":[122.40469,122.40469,122.40469,122.40469,122.40469,122.40469,122.40469,122.4327,122.4327,122.4327,122.4327,122.4327,122.4327,122.4327,122.44095,122.44095,122.44095,122.44095,122.44095,122.44095,122.44095,122.46329,122.46329,122.46329,122.46329,122.46329,122.46329,122.46329,122.407,122.407,122.407,122.407,122.407,122.407,122.407,122.41898,122.41898,122.41898,122.41898,122.41898,122.41898,122.41898,122.40165,122.40165,122.40165,122.40165,122.40165,122.40165,122.40165,122.40707,122.40707,122.40707,122.40707,122.40707,122.40707,122.40707,122.41055,122.41055,122.41055,122.41055,122.41055,122.41055,122.41055,122.41844,122.41844,122.41844,122.41844,122.41844,122.41844,122.41844,122.45347,122.45347,122.45347,122.45347,122.45347,122.45347,122.45347,122.41276,122.41276,122.41276,122.41276,122.41276,122.41276,122.41276,122.44371,122.44371,122.44371,122.44371,122.44371,122.44371,122.44371,122.41611,122.41611,122.41611,122.41611,122.41611,122.41611,122.41611],\"coloraxis\":\"coloraxis\",\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"x\":[7.264545454545455,5.518636363636364,6.880909090909091,6.8986363636363635,6.0947619047619055,5.281818181818182,6.990952380952381,7.755,5.5275,7.056,7.2829999999999995,6.4575,5.318,7.6345,7.8255,5.562,7.232,7.419,6.547,5.4615,7.6325,6.9565,4.4975,6.619000000000001,7.133,5.2764999999999995,4.466,6.546,11.0975,8.3035,10.408,10.16,9.4805,7.9905,10.495,7.875,5.568181818181818,7.233636363636363,7.173181818181818,6.646666666666667,5.493181818181818,7.568095238095238,7.980499999999999,5.627000000000001,7.117999999999999,7.063,6.8745,5.6475,7.725,8.337272727272726,5.915,7.766363636363637,7.737272727272727,7.208571428571428,5.870909090909091,8.24,8.137727272727274,5.806818181818182,7.537272727272727,7.712272727272728,6.9452380952380945,5.634545454545455,7.954761904761905,6.65590909090909,5.116363636363636,6.540454545454545,6.573181818181817,5.5495238095238095,5.000909090909091,6.5928571428571425,7.3536363636363635,4.819545454545454,7.027727272727272,6.654090909090909,5.9261904761904765,4.960909090909091,6.808571428571429,10.790909090909091,8.782272727272728,10.792727272727273,10.190454545454545,9.0,8.702272727272726,10.902857142857142,6.957727272727273,4.879545454545455,6.575,6.5240909090909085,5.763809523809524,4.8136363636363635,6.568095238095238,8.580454545454545,6.393636363636364,8.035909090909092,8.124545454545455,7.322857142857143,6.208181818181818,8.13904761904762],\"xaxis\":\"x\",\"y\":[8.1,8.1,8.1,8.1,8.1,8.1,8.1,8.1,8.1,8.1,8.1,8.1,8.1,8.1,7.9,7.9,7.9,7.9,7.9,7.9,7.9,6.2,6.2,6.2,6.2,6.2,6.2,6.2,8.6,8.6,8.6,8.6,8.6,8.6,8.6,9.2,9.2,9.2,9.2,9.2,9.2,9.2,8.6,8.6,8.6,8.6,8.6,8.6,8.6,9.1,9.1,9.1,9.1,9.1,9.1,9.1,9.1,9.1,9.1,9.1,9.1,9.1,9.1,8.0,8.0,8.0,8.0,8.0,8.0,8.0,7.2,7.2,7.2,7.2,7.2,7.2,7.2,9.1,9.1,9.1,9.1,9.1,9.1,9.1,7.6,7.6,7.6,7.6,7.6,7.6,7.6,8.2,8.2,8.2,8.2,8.2,8.2,8.2],\"yaxis\":\"y\",\"type\":\"scatter\"}],                        {\"template\":{\"data\":{\"histogram2dcontour\":[{\"type\":\"histogram2dcontour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"choropleth\":[{\"type\":\"choropleth\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"histogram2d\":[{\"type\":\"histogram2d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmap\":[{\"type\":\"heatmap\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmapgl\":[{\"type\":\"heatmapgl\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"contourcarpet\":[{\"type\":\"contourcarpet\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"contour\":[{\"type\":\"contour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"surface\":[{\"type\":\"surface\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"mesh3d\":[{\"type\":\"mesh3d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"parcoords\":[{\"type\":\"parcoords\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolargl\":[{\"type\":\"scatterpolargl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"scattergeo\":[{\"type\":\"scattergeo\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolar\":[{\"type\":\"scatterpolar\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"scattergl\":[{\"type\":\"scattergl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatter3d\":[{\"type\":\"scatter3d\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattermapbox\":[{\"type\":\"scattermapbox\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterternary\":[{\"type\":\"scatterternary\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattercarpet\":[{\"type\":\"scattercarpet\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}]},\"layout\":{\"autotypenumbers\":\"strict\",\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"hovermode\":\"closest\",\"hoverlabel\":{\"align\":\"left\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"bgcolor\":\"#E5ECF6\",\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"ternary\":{\"bgcolor\":\"#E5ECF6\",\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]]},\"xaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"yaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"geo\":{\"bgcolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"subunitcolor\":\"white\",\"showland\":true,\"showlakes\":true,\"lakecolor\":\"white\"},\"title\":{\"x\":0.05},\"mapbox\":{\"style\":\"light\"}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"pm_conc_mean\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"asthma_rate_first\"}},\"coloraxis\":{\"colorbar\":{\"title\":{\"text\":\"Longitude_first\"}},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"legend\":{\"tracegroupgap\":0},\"margin\":{\"t\":60}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('44c7b69e-b9e7-4ea1-8fa7-5aaed541b6d2');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "px.scatter(graph, x = 'pm_conc_mean', y = 'asthma_rate_first', color = 'Longitude_first')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
