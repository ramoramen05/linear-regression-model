import requests
import pandas as pd
from datetime import datetime

# API URL and Parameters
url = "https://air-quality-api.open-meteo.com/v1/air-quality"
params = {
    "latitude": 52.52,  # Latitude for Berlin
    "longitude": 13.41,  # Longitude for Berlin
    "hourly": "pm10,pm2_5,carbon_monoxide,nitrogen_dioxide,sulphur_dioxide,ozone,dust",  # Requested hourly data
    "domains": "cams_global"
}

# Fetch Data from Open-Meteo API
response = requests.get(url, params=params)
if response.status_code != 200:
    print("Failed to fetch data:", response.status_code, response.text)
    exit()

data = response.json()

# Process hourly data
hourly = data.get("hourly", {})
timestamps = hourly.get("time", [])
pm10 = hourly.get("pm10", [])
pm2_5 = hourly.get("pm2_5", [])
carbon_monoxide = hourly.get("carbon_monoxide", [])
nitrogen_dioxide = hourly.get("nitrogen_dioxide", [])
sulphur_dioxide = hourly.get("sulphur_dioxide", [])
ozone = hourly.get("ozone", [])
dust = hourly.get("dust", [])

# Create DataFrame
hourly_data = {
    "timestamp": [datetime.fromisoformat(ts) for ts in timestamps],
    "pm10": pm10,
    "pm2_5": pm2_5,
    "carbon_monoxide": carbon_monoxide,
    "nitrogen_dioxide": nitrogen_dioxide,
    "sulphur_dioxide": sulphur_dioxide,
    "ozone": ozone,
    "dust": dust
}
hourly_dataframe = pd.DataFrame(hourly_data)

# Display the DataFrame
print(hourly_dataframe)

# Save to CSV for GitHub
csv_filename = "hourly_air_quality.csv"
hourly_dataframe.to_csv(csv_filename, index=False)
print(f"Data saved to {csv_filename}")
