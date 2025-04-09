import os
import requests
from dotenv import load_dotenv

load_dotenv()

def fetch_weather(city: str) -> str:
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if "main" in data:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            return f"The temperature in {city} is {temp}°C with {desc}."
        else:
            return "City not found."
    except Exception as e:
        return f"Error fetching weather: {e}"
