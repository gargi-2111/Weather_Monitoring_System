
from flask import Flask, render_template, jsonify
import config
import weather_api
import data_processing
import storage
import alerting
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather_updates')
def weather_updates():
    weather_data_list = []

    for city in config.LOCATIONS:
        weather_data = weather_api.get_weather_data(city)
        if weather_data:
            processed_data = data_processing.process_weather_data(weather_data)
            weather_data_list.append(processed_data)
            alerting.check_alerts(processed_data)

    # Process data and return as JSON for real-time updates
    return jsonify(weather_data_list)


@app.route('/daily_summary')
def daily_summary():
    # Fetch and return daily summaries from the database
    session = storage.initialize_db()()
    summaries = session.query(storage.DailySummary).all()
    session.close()

    summary_list = []
    for summary in summaries:
        summary_list.append({
            'city': summary.city,
            'avg_temp': summary.avg_temp,
            'max_temp': summary.max_temp,
            'min_temp': summary.min_temp,
            'avg_humidity': summary.avg_humidity,  # Added avg humidity
            'avg_wind_speed': summary.avg_wind_speed,  # Added avg wind speed
            'dominant_condition': summary.dominant_condition,
            'date': summary.date
        })

    return jsonify(summary_list)



@app.route('/plot')
def plot():
    visualization.plot_temperature_trends()
    return render_template('plot.html')


if __name__ == '__main__':
    app.run(debug=True)
