from weather import fetch_weather

def test_valid_city():
    result = fetch_weather("London")
    assert "temperature" in result.lower() or "°c" in result.lower()

def test_invalid_city():
    result = fetch_weather("NotARealCity")
    assert "City not found" in result or "Error" in result
