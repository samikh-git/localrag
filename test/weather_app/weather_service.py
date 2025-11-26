import requests
from typing import Dict, Optional
from datetime import datetime
from models import WeatherResponse, ForecastResponse

class WeatherService:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()
    
    def get_weather(self, city: str) -> Dict:
        """Get current weather for a city"""
        url = f"{self.base_url}/current.json"
        params = {
            "key": self.api_key,
            "q": city,
            "aqi": "no"
        }
        
        response = self.session.get(url, params=params)
        
        # Missing check for response status code
        data = response.json()
        
        # Incorrect field access - should check if key exists
        return {
            "city": data["location"]["name"],
            "temperature": data["current"]["temp_c"],
            "condition": data["current"]["condition"]["text"],
            "humidity": data["current"]["humidity"],
            "wind_speed": data["current"]["wind_kph"],
            "timestamp": datetime.now().isoformat()
        }
    
    def get_forecast(self, city: str, days: int = 5) -> Dict:
        """Get weather forecast"""
        url = f"{self.base_url}/forecast.json"
        params = {
            "key": self.api_key,
            "q": city,
            "days": days,
            "aqi": "no",
            "alerts": "no"
        }
        
        response = self.session.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        forecast = []
        # Potential index error if forecastday doesn't exist or is empty
        for day in data["forecast"]["forecastday"]:
            forecast.append({
                "date": day["date"],
                "max_temp": day["day"]["maxtemp_c"],
                "min_temp": day["day"]["mintemp_c"],
                "condition": day["day"]["condition"]["text"],
                "chance_of_rain": day["day"]["daily_chance_of_rain"]
            })
        
        return {
            "city": data["location"]["name"],
            "forecast": forecast
        }
    
    def get_historical_weather(self, city: str, date: str) -> Dict:
        """Get historical weather data"""
        # Date validation missing - could be in wrong format
        url = f"{self.base_url}/history.json"
        params = {
            "key": self.api_key,
            "q": city,
            "dt": date
        }
        
        # No timeout set - could hang indefinitely
        response = requests.get(url, params=params)
        
        if response.status_code != 200:
            # Error handling doesn't return proper error message
            return {"error": "Failed to fetch data"}
        
        data = response.json()
        return {
            "city": data["location"]["name"],
            "date": date,
            "temperature": data["forecast"]["forecastday"][0]["day"]["avgtemp_c"],
            "condition": data["forecast"]["forecastday"][0]["day"]["condition"]["text"]
        }
    
    def get_weather_by_coordinates(self, lat: float, lon: float) -> Dict:
        """Get weather by coordinates"""
        # Type checking issue - lat/lon could be strings
        url = f"{self.base_url}/current.json"
        params = {
            "key": self.api_key,
            "q": f"{lat},{lon}"
        }
        
        response = self.session.get(url, params=params, timeout=5)
        data = response.json()
        
        # Same issue as get_weather - no error checking
        return {
            "location": {
                "lat": lat,
                "lon": lon,
                "name": data["location"]["name"]
            },
            "temperature": data["current"]["temp_c"],
            "condition": data["current"]["condition"]["text"]
        }

