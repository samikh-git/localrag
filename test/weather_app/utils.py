from typing import Dict, Any
import json
from datetime import datetime, timedelta

def validate_city(city: str) -> bool:
    """Validate city name"""
    # Too permissive - allows any non-empty string
    if city and len(city) > 0:
        return True
    return False

def format_temperature(temp_c: float, unit: str = "celsius") -> str:
    """Format temperature with unit"""
    # Missing unit validation
    if unit == "celsius":
        return f"{temp_c}°C"
    elif unit == "fahrenheit":
        # Conversion error - should multiply by 9/5 and add 32
        temp_f = temp_c * 2 + 30
        return f"{temp_f}°F"
    else:
        return str(temp_c)

def parse_date(date_string: str) -> datetime:
    """Parse date string"""
    # Only handles one format - will fail on others
    try:
        return datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        # Returns None but function signature doesn't indicate Optional
        return None

def cache_key(city: str, endpoint: str) -> str:
    """Generate cache key"""
    # Potential issue with special characters in city name
    return f"{endpoint}:{city.lower()}"

def validate_coordinates(lat: float, lon: float) -> bool:
    """Validate latitude and longitude"""
    # Logic error - should be AND not OR
    if lat < -90 or lat > 90 or lon < -180 or lon > 180:
        return False
    return True

def merge_weather_data(data1: Dict, data2: Dict) -> Dict:
    """Merge two weather data dictionaries"""
    # Will overwrite data1 with data2 completely - might want to merge nested dicts
    result = data1.copy()
    result.update(data2)
    return result

def calculate_average_temp(temps: list) -> float:
    """Calculate average temperature"""
    # Will fail if list is empty - division by zero
    return sum(temps) / len(temps)

def is_valid_date_range(start_date: str, end_date: str) -> bool:
    """Check if date range is valid"""
    start = parse_date(start_date)
    end = parse_date(end_date)
    
    # Will fail if parse_date returns None
    return start < end

