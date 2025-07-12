#step 1 Extraxt the data
import requests 
import config
def fetch_weather(city):
    url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={config.API_KEY}&units=metric"
    response=requests.get(url)
    if response.status_code==200:
        return response.json()
    else:
        print(f'failed to fetch data :{response.status_code}')
        return None

from transform import transform_weather_data

#step 3 load data
from load import save_to_db

if __name__=='__main__':
    city=input('Enter the city name\n')
    raw=fetch_weather(city)
    if raw:
        from pprint import pprint
        clean_data=transform_weather_data(raw)
        pprint(clean_data)
        save_to_db(clean_data)
