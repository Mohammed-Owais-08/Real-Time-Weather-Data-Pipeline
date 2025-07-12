from datetime import datetime
def transform_weather_data(raw_data):
    if not raw_data:
        return None
    transformed={
        'city':raw_data.get('name'),
        'temperature':raw_data['main'].get('temp'),
        'humidity':raw_data['main'].get('humidity'),
        'wind_speed':raw_data['wind'].get('speed'),
        'weather':raw_data['weather'][0].get('description') if raw_data['weather'] else None,
        'timestamp':datetime.utcfromtimestamp(raw_data.get('dt')).strftime('%Y-%m-%d %H:%M:%S')
    }
    return transformed