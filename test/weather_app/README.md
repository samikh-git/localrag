# Weather App Backend

A simple Flask-based weather API backend.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Copy `.env.example` to `.env` and add your API key:
```bash
cp .env.example .env
```

3. Run the application:
```bash
python main.py
```

## API Endpoints

- `GET /health` - Health check
- `GET /weather?city=<city_name>` - Get current weather
- `GET /weather/forecast?city=<city_name>&days=<num_days>` - Get forecast
- `POST /weather/history` - Get historical weather data

## Example Usage

```bash
curl "http://localhost:5000/weather?city=Paris"
```

