import os
import wolframalpha

from dotenv import load_dotenv
load_dotenv()
APPID=os.getenv('WOLFRAM_APPID')


#APPID=os.environ['WOLFRAM_APPID']

def solve(query):
	client=wolframalpha.Client(APPID)
	res=client.query(query)
	answer=[]
	c=0
	for ans in res.pods:
		answer.append({"title":ans['@title'], "text":[],"image":[]})
		ans=ans['subpod']
		if isinstance(ans,list):
			for i in ans:
				answer[c]['text'].append(i['plaintext'])
				answer[c]['image'].append(i['img']['@src'])
		else:
			answer[c]['text'].append(ans['plaintext'])
			answer[c]['image'].append(ans['img']['@src'])
		c+=1
	return answer