import requests
import json

def random_quote():
	url='https://zenquotes.io/api/random'
	r=requests.get(url)
	json_data=json.loads(r.text)
	quote={
	"q":json_data[0]['q'],
	"a":json_data[0]['a']
	}
	return quote