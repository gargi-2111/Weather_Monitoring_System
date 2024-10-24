import config

def check_alerts(weather_data):
    if weather_data['temp'] > config.TEMP_THRESHOLD:
        trigger_alert(weather_data)

def trigger_alert(weather_data):
    print(f"ALERT: {weather_data['city']} exceeds {config.TEMP_THRESHOLD}°C with {weather_data['temp']}°C")
