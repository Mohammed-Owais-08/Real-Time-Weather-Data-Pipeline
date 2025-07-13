from datetime import datetime, timedelta

def transform_weather_data(raw_data):
    if not raw_data:
        return None

    # Convert to IST (UTC + 5 hours 30 minutes)
    utc_time = datetime.utcfromtimestamp(raw_data.get('dt'))
    ist_time = utc_time + timedelta(hours=5, minutes=30)

    transformed = {
        'city': raw_data.get('name'),
        'temperature': raw_data['main'].get('temp'),
        'humidity': raw_data['main'].get('humidity'),
        'wind_speed': raw_data['wind'].get('speed'),
        'weather': raw_data['weather'][0].get('description') if raw_data['weather'] else None,
        'timestamp': ist_time.strftime('%Y-%m-%d %H:%M:%S')
    }
    return transformed
