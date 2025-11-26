from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class WeatherCondition:
    text: str
    icon: str
    code: int

@dataclass
class CurrentWeather:
    temp_c: float
    temp_f: float
    condition: WeatherCondition
    humidity: int
    wind_kph: float
    wind_mph: float
    feelslike_c: float

@dataclass
class Location:
    name: str
    region: str
    country: str
    lat: float
    lon: float
    tz_id: str
    localtime: str

@dataclass
class WeatherResponse:
    location: Location
    current: CurrentWeather
    timestamp: datetime
    
    # Missing validation methods
    def to_dict(self):
        return {
            "location": {
                "name": self.location.name,
                "country": self.location.country
            },
            "temperature": self.current.temp_c,
            "condition": self.current.condition.text
        }

@dataclass
class ForecastDay:
    date: str
    day: dict
    astro: dict
    hour: List[dict]

@dataclass
class ForecastResponse:
    location: Location
    current: CurrentWeather
    forecast: List[ForecastDay]
    
    # Incomplete implementation
    def get_daily_forecast(self):
        # Missing return statement
        daily = []
        for day in self.forecast:
            daily.append({
                "date": day.date,
                "max_temp": day.day["maxtemp_c"]
            })

