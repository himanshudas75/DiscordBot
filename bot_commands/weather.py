import requests
import json
import os
from dotenv import load_dotenv

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
load_dotenv(f'{FILE_PATH}/../env')

OPENWEATHER_KEY=os.getenv('OPENWEATHER_KEY')

URL=f'https://api.openweathermap.org/data/2.5/weather'

def weather(city):
    url=f'{URL}?q={city}&appid={OPENWEATHER_KEY}'
    print(url)
    r=requests.get(url)
    print(r.text)

weather('mihijam')