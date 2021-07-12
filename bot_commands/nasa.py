import requests
import json
import os
from dotenv import load_dotenv

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
load_dotenv(f'{FILE_PATH}/../env')

NASA_KEY=os.getenv('NASA_KEY')

def apod(date):
    if date=="":
        url=f'https://api.nasa.gov/planetary/apod?count=1&api_key={NASA_KEY}'
    else:
        url=f'https://api.nasa.gov/planetary/apod?count=1&date={date}&api_key={NASA_KEY}'
    r=requests.get(url)
    json_data=json.loads(r.text)
    toret={
        "date": json_data['date'],
        "explanation": json_data['explanation'],
        "hdurl": json_data['hdurl'],
        "title": json_data['title']
    }
    return toret
