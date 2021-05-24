import requests
import os

'''
from dotenv import load_dotenv
load_dotenv()
APPID=os.getenv('WOLFRAM_APPID')
'''

APPID=os.environ['WOLFRAM_APPID']

def solve(query):
	url=f'http://api.wolframalpha.com/v2/query?appid={APPID}&input={query}%3F'
	r=requests.get(url)

	if r.status_code=='501':
		return 'Unable to process that query'

	return r.text