from datetime import datetime
from meteostat import Point, Hourly
import pandas as pd

cities = {
    "Tijuana_MX": (32.5149, -117.0382),       # Your base (Semi-arid)
    "Londres_UK": (51.5074, -0.1278),         # Europe (Oceanic/Rainy)
    "Tokio_JP": (35.6762, 139.6503),          # Asia (Humid Subtropical)
    "Sydney_AU": (-33.8688, 151.2093),        # Oceania (Southern Hemisphere/Inverted Seasons)
    "ElCairo_EG": (30.0444, 31.2357),         # Africa (Arid Desert)
    "SaoPaulo_BR": (-23.5505, -46.6333),      # South America (Subtropical)
    "Moscu_RU": (55.7558, 37.6173),           # Europe/Asia (Cold Continental)
    "Singapur_SG": (1.3521, 103.8198),        # Asia (Equatorial/Rainy Tropical)
    "Reikiavik_IS": (64.1466, -21.9426),      # Europe (Subpolar Oceanic)
    "Vancouver_CA": (49.2827, -123.1207)      # North America (Temperate Rainy)
}

start = datetime(2020, 1, 1)
finish = datetime(2024, 1, 1)

dfs = []

print("--- Starting Data Mining ---")

for name, coords in cities.items():
    print(f"Downloading data from {name}...")
    
    location = Point(coords[0], coords[1])
    
    data = Hourly(location, start, finish)
    data = data.fetch()
    
    # Cleaning: Selecting only relevant columns and dropping NaNs
    df_ciudad = data[['temp', 'rhum', 'pres', 'coco']].dropna()
    
    # Ensure datetime index
    df_ciudad.index = pd.to_datetime(df_ciudad.index)
    
    # Extract time features
    df_ciudad['year'] = df_ciudad.index.year
    df_ciudad['month'] = df_ciudad.index.month
    df_ciudad['day'] = df_ciudad.index.day
    df_ciudad['hour'] = df_ciudad.index.hour
    
    # Add city name and longitude
    df_ciudad['city'] = name
    df_ciudad['longitude'] = coords[1]
    df_ciudad['latitude'] = coords[0]
    
    dfs.append(df_ciudad)

# Unifying all data
df_final = pd.concat(dfs)

# Creating weather condition text
def translate_weather(code):
    if code in [1, 2]: return "Clear"
    elif code in [3, 4]: return "Cloudy"
    elif code in [5, 6]: return "Fog"
    elif code in [7, 8, 9, 10, 11, 17, 18]: return "Rain"
    elif code in [12, 13, 14, 15, 16, 19, 20, 21, 22, 24]: return "Snow"
    elif code in [23, 25, 26, 27]: return "Storm"
    else: return "Other"

# Filtering unwanted weather conditions
df_final['weather_label'] = df_final['coco'].apply(translate_weather)
df_final = df_final[df_final['weather_label'] != "Other"]

# Saving
df_final.to_csv('weather_dataset.csv', index=False)
print(f"\nDataset generated with {len(df_final)} registers of {len(cities)} cities.")