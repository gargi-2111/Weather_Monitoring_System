
import time
import weather_api
import data_processing
import alerting
import storage
from datetime import datetime
import config

def main():
    daily_weather_data = []
    last_summary_date = None

    while True:
        for city in config.LOCATIONS:
            weather_data = weather_api.get_weather_data(city)
            if weather_data:
                processed_data = data_processing.process_weather_data(weather_data)
                daily_weather_data.append(processed_data)

                # Check for alerts
                alerting.check_alerts(processed_data)

        # Roll up and store daily summaries at the end of the day
        current_date = datetime.utcnow().strftime('%Y-%m-%d')
        if last_summary_date != current_date:
            summary = data_processing.calculate_daily_summary(daily_weather_data)
            storage.store_daily_summary(summary)
            daily_weather_data = []  # Reset for the next day
            last_summary_date = current_date

        time.sleep(config.POLL_INTERVAL)

if __name__ == "__main__":
    main()
