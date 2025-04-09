def decide_action(query: str) -> str:
    weather_keywords = [
        "weather", "temperature", "forecast", "humidity", "rain", "snow",
        "sunny", "wind", "storm", "climate", "conditions", "air quality"
    ]
    query_lower = query.lower()
    return "weather" if any(word in query_lower for word in weather_keywords) else "pdf"
