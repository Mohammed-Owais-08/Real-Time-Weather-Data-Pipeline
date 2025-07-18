from flask import Flask, request, render_template, jsonify
from extract import fetch_weather
from transform import transform_weather_data
from load import save_to_db, Weather
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# Database setup
engine = create_engine("sqlite:///weather.db")
Session = sessionmaker(bind=engine)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/weather", methods=["POST"])
def weather():
    city = request.form.get("city")
    raw = fetch_weather(city)
    
    if raw:
        clean = transform_weather_data(raw)
        save_to_db(clean)

        # Fetch last 5 saved entries
        session = Session()
        recent = session.query(Weather).order_by(Weather.date.desc()).limit(5).all()
        session.close()
        

        recent_data = [
            {
                "city": r.city,
                "temperature": r.temperature,
                "timestamp": r.timestamp.strftime("%Y-%m-%d %H:%M:%S")
                # "date":r.date.strftime("%H:%M:%S") to get the exact time 
                #once you fetch data for a city/place it gets updated after 10 minutes as openweathermap api takes time to update the live data
                # hence the 1st time you fetch the data, the data gets cached which will be returned when you are fetching data for the same city/place
            }
            for r in recent
        ]

        return jsonify({
            **clean,
            "message": "✅ Weather data has been saved to the database.",
            "recent": recent_data
        })

    return jsonify({"error": "Failed to fetch weather data"})

import os
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

