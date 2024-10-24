
import requests
import config

API_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city):
    params = {
        'q': city,
        'appid': config.API_KEY,
        'units': 'metric'  # Fetch temperature in Celsius
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        weather_data = response.json()
        return {
            'city': city,
            'main': weather_data['weather'][0]['main'],
            'temp': weather_data['main']['temp'],
            'feels_like': weather_data['main']['feels_like'],
            'humidity': weather_data['main']['humidity'],  # Added humidity
            'wind_speed': weather_data['wind']['speed'],  # Added wind speed
            'dt': weather_data['dt']
        }
    else:
        print(f"Error fetching weather data for {city}")
        return None
