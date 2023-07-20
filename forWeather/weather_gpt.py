import requests
import os
from dotenv import load_dotenv

load_dotenv("api.env")

API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather_data_by_location(city, country_code):
    params = {
        "q": f"{city},{country_code}",
        "appid": API_KEY,
        "units": "imperial"  # You can change this to "metric" for Celcius
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data["cod"] == 200:
        weather_info = {
            "location": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
        }
        return weather_info
    else:
        print("Failed to fetch weather data.")
        return None

# Example usage
city = "Istanbul"
country_code = "TR"  # Country code (e.g., "US" for United States, "GB" for United Kingdom)

weather_data = get_weather_data_by_location(city, country_code)
if weather_data:
    print("Weather Information:")
    print(f"Location: {weather_data['location']}")
    print(f"Temperature: {weather_data['temperature']}°C")
    print(f"Description: {weather_data['description']}")
