import os
import requests
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY is missing from .env")

city = input("Enter a city name: ")


geo_response = requests.get(
    "https://geocoding-api.open-meteo.com/v1/search",
    params={"name": city, "count": 1},
    timeout=5
)

if geo_response.status_code != 200:
    print("Couldn't reach geocoding API.")
    exit()

geo_data = geo_response.json()

if not geo_data.get("results"):
    print(f"City '{city}' not found. Please check the name.")
    exit()

lat = geo_data["results"][0]["latitude"]
lon = geo_data["results"][0]["longitude"]
name = geo_data["results"][0]["name"]


weather_response = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={
        "latitude":        lat,
        "longitude":       lon,
        "current_weather": "true",
        "hourly":          "relativehumidity_2m"
    },
    timeout=5
)

if weather_response.status_code != 200:
    print("Couldn't reach weather API.")
    exit()

weather_data = weather_response.json()
current = weather_data["current_weather"]
temperature = current["temperature"]
windspeed = current["windspeed"]
humidity = weather_data["hourly"]["relativehumidity_2m"][0]


prompt = f"""
Here is the current weather for {name}:
- Temperature: {temperature}°C
- Windspeed: {windspeed} km/h
- Humidity: {humidity}%

Please give a short, friendly, human summary of this weather.
"""

groq_response = requests.post(
    "https://api.groq.com/openai/v1/chat/completions",
    headers={"Authorization": f"Bearer {groq_api_key}"},
    json={
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    },
    timeout=10
)

if groq_response.status_code != 200:
    print("Status code:", groq_response.status_code)
    print("Couldn't reach GROQ API.")
    exit()

answer = groq_response.json()["choices"][0]["message"]["content"]

print(f"\nWeather Summary for {name}:")
print(answer)