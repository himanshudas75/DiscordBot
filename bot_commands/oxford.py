import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()
app_id=os.getenv('OXFORD_APPID')
app_key=os.getenv('OXFORD_APPKEY')
'''
app_id=os.environ['OXFORD_APPID']
app_key=os.environ['OXFORD_APPKEY']
'''

def word_id_find(word_id,language='en'):
	url='https://od-api.oxforddictionaries.com:443/api/v2/lemmas/' + language + '/' + word_id.lower()
	r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
	status=r.status_code
	if status==200:
		json_data=json.loads(r.text)
		word=json_data['results'][0]['lexicalEntries'][0]['inflectionOf'][0]['id']
		return word
	else:
		return -1

def meaning(word,language='en-gb',fields='definitions',strictMatch='false'):
	word_id=word_id_find(word,language)
	if word_id==-1:
		return -1
	url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + language + '/' + word_id.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch
	r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
	if r.status_code==200:
		json_data=json.loads(r.text)
		json_data=json_data['results'][0]
		deflist=json_data['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions']
		mean={
		"id":json_data['id'],
		"language":json_data['language'],
		"definition":deflist[0]
		}
		return mean
	else:
		return -1