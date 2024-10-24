Real-Time Weather Monitoring System
Overview
This project implements a real-time weather monitoring system using the OpenWeatherMap API. It retrieves and processes weather data for major Indian cities: Delhi, Mumbai, Chennai, Bangalore, Kolkata, and Hyderabad. The system provides real-time weather updates, 5-day forecasts, and generates daily summaries of weather conditions. Additionally, it supports user-configurable alerts (e.g., temperature threshold-based alerts) and can visualize historical weather trends.

Key Features:
Real-time weather data: Fetched every 5 minutes for multiple cities.
Weather forecasting: Retrieves and processes 5-day weather forecasts (3-hour intervals).
Rollups and aggregates: Calculates average, maximum, minimum temperatures, humidity, and wind speed.
User-configurable alerts: Alerts trigger when temperature exceeds a certain threshold (e.g., 35°C).
Interactive UI: Real-time weather updates and forecasts, refreshed via AJAX.
Daily summaries: Summarizes weather conditions at the end of each day.
Forecast summaries: Summarizes predicted weather conditions for upcoming days.
Design Choices
1. Modular Architecture:
The system is designed with clear separation of concerns, making it easy to maintain and extend:

API communication is handled by weather_api.py.
Data processing (conversion, aggregation, rollups) is managed by data_processing.py.
Alert handling is separated into alerting.py.
Database operations (storing summaries) are handled by storage.py.
Real-time weather data updates and forecasts are integrated into app.py.
2. Real-Time Updates:
AJAX enables real-time updates on the frontend, ensuring a smooth user experience without page reloads.
3. User Interaction:
Users can define custom thresholds for triggering alerts, such as alerts for when the temperature exceeds 35°C.
4. Containerization:
The entire application can run in a Docker container, ensuring consistency and making it easy to deploy across different environments.
Prerequisites
Before running the application, make sure you have the following:

OpenWeatherMap API Key:
Get a free API key by signing up at OpenWeatherMap.
This key will be used to fetch weather data.
Docker:
Install Docker from here if you don't have it already.
Docker is used to containerize the application for consistency across environments.

Dependencies
The following dependencies are required for the application to run, and will be installed automatically if using Docker:
Flask: Web framework to serve the application.
requests: For making API calls to OpenWeatherMap.
SQLAlchemy: ORM for interacting with the SQLite database.
Matplotlib: For generating visualizations.
Pytest: For running unit tests.
All dependencies are listed in the requirements.txt file.

Installation and Setup Instructions
1. Clone the Repository
First, clone this repository to your local machine:
git clone https://github.com/yourusername/weather-monitoring-system.git
cd weather-monitoring-system
2. Set Up API Key and Configurations
Open the config.py file and update it with your OpenWeatherMap API Key:
API_KEY = "your_openweathermap_api_key_here"  # Replace with your actual API key
LOCATIONS = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
POLL_INTERVAL = 300  # Poll every 5 minutes
TEMP_THRESHOLD = 35.0  # Trigger alert if temperature exceeds 35°C
DATABASE_URI = "sqlite:///weather_data.db"  # SQLite database for persistent storage
3. Running the Application Using Docker
Option 1: Using Docker (Recommended)
Build the Docker image:
docker build -t weather-monitoring-system .
Run the Docker container:
docker run -p 5000:5000 weather-monitoring-system
The Flask app will now be running inside the Docker container. Visit http://localhost:5000/ in your browser to view the app.

Option 2: Using Docker Compose (For Multi-Container Setup)
If you need a more complex setup (e.g., using a PostgreSQL database), you can use Docker Compose.

Run the app with Docker Compose:

docker-compose up --build
This will start both the Flask app and any other services you define in the docker-compose.yml file.

4. Running the Application Locally (Without Docker)
If you prefer to run the application without Docker, follow these steps:

Install dependencies:

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install the required Python packages
pip install -r requirements.txt
Run the Flask application:

python app.py
The application will now be running at http://localhost:5000/.

Usage
Real-Time Weather Monitoring:

The app will automatically fetch real-time weather data every 5 minutes.
Weather data includes temperature, humidity, wind speed, and main weather condition.
Daily Weather Summaries:

The app calculates daily summaries (average, max, min temperatures, humidity, wind speed, and dominant weather condition).
Weather Forecasting:

The app provides a 5-day forecast, with weather conditions for every 3-hour interval.
Alerts:

Alerts are triggered if the temperature exceeds the configured threshold (35°C by default).
Visualization:

Weather trends can be visualized using matplotlib (e.g., temperature trends over time).
Testing
To run the unit tests, you can use pytest. All test cases are located in the tests/ directory.

# Run tests using pytest
pytest tests/
Tests cover:

Data parsing and temperature conversion.
Rollup and aggregation calculations.
Alert functionality.
Forecast data processing.
Extending the Application
Additional Features Implemented:
Humidity and Wind Speed Support: The system processes and displays additional weather parameters like humidity and wind speed.
Weather Forecasting: 5-day weather forecasts are fetched and displayed in the application.
Real-Time Updates: The UI is updated in real-time using AJAX, ensuring smooth data updates without page reloads.
Future Extensions:
Email Alerts: Add functionality to send email notifications when a temperature threshold is breached.
Cloud Deployment: Deploy the app to platforms like AWS or Heroku for a production-grade system.
Build Design and Efficiency Considerations
API Requests:

Weather data and forecast data are fetched asynchronously from OpenWeatherMap at configurable intervals.
The system uses AJAX to update the UI without refreshing the entire page, improving user experience and reducing the load on the backend.
Real-Time Data Processing:

The system processes and converts weather data in real-time (temperature, humidity, wind speed).
Aggregate calculations (average, min, max) are efficiently computed and stored daily.
Alert Mechanism:

Alerts are triggered based on user-configurable temperature thresholds and can be extended to include email notifications.
Docker and Containerization
Docker is used to containerize the application to ensure consistent environments across different setups.
The application can also be deployed using Docker Compose for a more complex multi-container setup (e.g., with a PostgreSQL database).
Docker Setup
The Dockerfile defines the build process for the application, while docker-compose.yml (optional) can be used to define multi-container setups.

bash
Copy code
# Build the Docker image
docker build -t weather-monitoring-system .

# Run the application in Docker
docker run -p 5000:5000 weather-monitoring-system
