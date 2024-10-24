
$(document).ready(function() {
    // Function to fetch real-time weather data
    function fetchWeatherData() {
        $.ajax({
            url: "/weather_updates",
            method: "GET",
            success: function(data) {
                let html = '<table border="1"><tr><th>City</th><th>Temp (°C)</th><th>Feels Like (°C)</th><th>Humidity (%)</th><th>Wind Speed (m/s)</th><th>Main</th><th>Timestamp</th></tr>';
                data.forEach(item => {
                    html += `<tr>
                        <td>${item.city}</td>
                        <td>${item.temp}</td>
                        <td>${item.feels_like}</td>
                        <td>${item.humidity}</td>
                        <td>${item.wind_speed}</td>
                        <td>${item.main}</td>
                        <td>${item.dt}</td>
                    </tr>`;
                });
                html += '</table>';
                $('#weather_data').html(html);
            }
        });
    }

    // Function to fetch daily summaries
    function fetchDailySummary() {
        $.ajax({
            url: "/daily_summary",
            method: "GET",
            success: function(data) {
                let html = '<table border="1"><tr><th>City</th><th>Avg Temp (°C)</th><th>Max Temp (°C)</th><th>Min Temp (°C)</th><th>Avg Humidity (%)</th><th>Avg Wind Speed (m/s)</th><th>Dominant Condition</th><th>Date</th></tr>';
                data.forEach(item => {
                    html += `<tr>
                        <td>${item.city}</td>
                        <td>${item.avg_temp}</td>
                        <td>${item.max_temp}</td>
                        <td>${item.min_temp}</td>
                        <td>${item.avg_humidity}</td>
                        <td>${item.avg_wind_speed}</td>
                        <td>${item.dominant_condition}</td>
                        <td>${item.date}</td>
                    </tr>`;
                });
                html += '</table>';
                $('#daily_summary').html(html);
            }
        });
    }

    // Set intervals to fetch weather data and summaries every 5 minutes (300000 milliseconds)
    setInterval(fetchWeatherData, 300000);
    setInterval(fetchDailySummary, 300000);

    // Initial fetch on page load
    fetchWeatherData();
    fetchDailySummary();
});
