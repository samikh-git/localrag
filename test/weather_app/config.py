import os
from typing import Optional

# Configuration loading with potential issues

# Missing check if environment variable exists
API_KEY = os.getenv("WEATHER_API_KEY")

# Hardcoded default - security issue
DEFAULT_API_KEY = "1234567890abcdef"

# Logic error - will always use DEFAULT_API_KEY if WEATHER_API_KEY is not set
# but should probably raise an error instead
if not API_KEY:
    API_KEY = DEFAULT_API_KEY

BASE_URL = os.getenv("WEATHER_API_BASE_URL", "https://api.weatherapi.com/v1")

# Missing validation for URL format
TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "30"))

# Type issue - could be None
MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))

# Configuration that's defined but never used
CACHE_ENABLED = os.getenv("CACHE_ENABLED", "false").lower() == "true"
CACHE_TTL = int(os.getenv("CACHE_TTL", "300"))

# Missing validation
ALLOWED_CITIES = os.getenv("ALLOWED_CITIES", "").split(",")

# This will be an empty list if env var not set, but logic might expect None
if ALLOWED_CITIES == [""]:
    ALLOWED_CITIES = []

