from flask import Flask, jsonify, request
from weather_service import WeatherService
from config import API_KEY, BASE_URL
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

weather_service = WeatherService(API_KEY, BASE_URL)

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy"}), 200

@app.route('/weather', methods=['GET'])
def get_weather():
    """Get weather for a city"""
    city = request.args.get('city')
    
    if not city:
        return jsonify({"error": "City parameter is required"}), 400
    
    try:
        weather_data = weather_service.get_weather(city)
        return jsonify(weather_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/weather/forecast', methods=['GET'])
def get_forecast():
    """Get weather forecast for a city"""
    city = request.args.get('city')
    days = request.args.get('days', 5)
    
    if not city:
        return jsonify({"error": "City parameter is required"}), 400
    
    try:
        forecast_data = weather_service.get_forecast(city, days)
        return jsonify(forecast_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/weather/history', methods=['POST'])
def get_weather_history():
    """Get historical weather data"""
    data = request.get_json()
    city = data.get('city')
    date = data.get('date')
    
    # Missing validation for date format
    weather_data = weather_service.get_historical_weather(city, date)
    return jsonify(weather_data), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

