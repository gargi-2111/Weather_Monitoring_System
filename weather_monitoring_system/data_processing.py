from datetime import datetime

def process_weather_data(weather_data):
    return {
        'city': weather_data['city'],
        'main': weather_data['main'],
        'temp': weather_data['temp'],
        'feels_like': weather_data['feels_like'],
        'humidity': weather_data['humidity'],  # Added humidity
        'wind_speed': weather_data['wind_speed'],  # Added wind speed
        'dt': datetime.utcfromtimestamp(weather_data['dt']).strftime('%Y-%m-%d %H:%M:%S')
    }

def calculate_daily_summary(weather_records):
    temps = [record['temp'] for record in weather_records]
    humidities = [record['humidity'] for record in weather_records]  # Added humidity
    wind_speeds = [record['wind_speed'] for record in weather_records]  # Added wind speed

    return {
        'avg_temp': sum(temps) / len(temps),
        'max_temp': max(temps),
        'min_temp': min(temps),
        'avg_humidity': sum(humidities) / len(humidities),  # Added avg humidity
        'avg_wind_speed': sum(wind_speeds) / len(wind_speeds),  # Added avg wind speed
        'dominant_condition': get_dominant_weather_condition(weather_records)
    }

def get_dominant_weather_condition(weather_records):
    condition_count = {}
    for record in weather_records:
        condition = record['main']
        condition_count[condition] = condition_count.get(condition, 0) + 1
    return max(condition_count, key=condition_count.get)  # Dominant condition by count
