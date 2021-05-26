import requests
import os
import re
import json
import urllib.parse


from dotenv import load_dotenv
load_dotenv()
KEY=os.getenv('OMDB_KEY')

#KEY=os.environ['OMDB_KEY']

def omdb(t,y,typ):
	u='http://www.omdbapi.com/'+t+y+typ+'&apikey='+KEY
	url=urllib.parse.quote_plus(u,safe='/:?&=')
	r=requests.get(url)
	json_data=json.loads(r.text)
	if json_data['Response']=='False':
		return json_data['Error']
	else:
		return json_data

def search(args):
	typ=re.findall('type=\w+',args)
	year=re.findall('year=\d+',args)
	if not year==[]:
		y='&y='+year[0][5:]
	else:
		y=''

	if not typ==[]:
		ty='&type='+typ[0][5:]
	else:
		ty=''

	if not (year==[] and typ==[]):
		title='?t='+re.findall('.+year=|.+type=',args)[0][:-5].strip()
	else:
		title='?t='+args

	details=omdb(title,y,ty)
	return details