
import matplotlib.pyplot as plt
from storage import initialize_db, DailySummary

def plot_temperature_trends():
    session = initialize_db()()
    summaries = session.query(DailySummary).all()
    session.close()

    dates = [summary.date for summary in summaries]
    temps = [summary.avg_temp for summary in summaries]

    plt.plot(dates, temps)
    plt.title('Temperature Trends')
    plt.xlabel('Date')
    plt.ylabel('Average Temperature (°C)')
    plt.savefig('static/temp_trends.png')
    plt.close()
