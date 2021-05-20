import discord
import os
import requests
import json
import random
from dotenv import load_dotenv
from twilio.rest import Client
import re

#TOKEN=os.environ['DISCORD_TOKEN']
#GUILD=os.environ['DISCORD_GUILD']
load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')
GUILD=os.getenv('DISCORD_GUILD')
TWILIO_SID=os.getenv('TWILIO_SID')
TWILIO_TOKEN=os.getenv('TWILIO_TOKEN')
intents=discord.Intents().all()
client=discord.Client(intents=intents)
twilclient=Client(TWILIO_SID,TWILIO_TOKEN)

sad_words=['sad','unhappy','miserable','depressed','angry','depressing']

curse_words=['bhosdike','madarchod','bkl','bkc','behen ke lode','motherfucker','sisterfucker','harami','jhaantu','jhantu','chutiya','chutiye','bhnchod','behenchod''bhosadpappu','bakchod','kutta','kameena','chadarmod']

starter_encouragements=[
  'Cheer Up!',
  'Hang in there',
  'You ae a great person / bot!',
  'You are great buddy!',
  'Bot loves you',
  'Your day is gonna be super great!'
]

curse_replies=[
  'Aji Lund Mera!',
  'Gaand me goli lagegi ab',
  'Tu hoga chutiya',
  'Harami saala',
  'Jo bolta hai wohi hota hai',
  'Aur gaaliya nahi aati!',
  'Izzat se baat kar, bot hu mai',
  'Bot ke samne gaali nahi',
  'Lund pakar ke jhul jaa',
  'Ye kya chutiyapa kar rha hai',
  'Nikalna hai idhr se?',
  'Chadarmod']
  
def get_quote():
	response=requests.get("https://zenquotes.io/api/random")
	json_data=json.loads(response.text)
	quote=json_data[0]['q'] + " - " + json_data[0]['a']
	return quote

@client.event
async def on_ready():
	for guild in client.guilds:
		if guild.name == GUILD:
			break
	print(f'{client.user} is connected to the following guild:')
	print(f'{guild.name} (id: {guild.id})')

	members='\n - '.join([member.name for member in guild.members])
	print(f'Guild Members:\n - {members}')
	
	channel=client.get_channel(841739053312901163)
	await channel.send("Quiz ke time gussa aye to gaali dena")

@client.event
async def on_message(message):

	if message.author==client.user:
		return

	msg=message.content

	if msg.startswith('$inspire'):
		quote=get_quote()
		await message.channel.send(quote)

	if any(word in msg.lower() for word in sad_words):
		await message.channel.send(random.choice(starter_encouragements))
	
	if any(word in msg.lower() for word in curse_words):
		await message.channel.send(random.choice(curse_replies))

	if msg.startswith('$send'):
		text=msg.split()
		#phone=text[1]
		body=' '.join(text[1:])
		tosend=twilclient.messages.create(
			from_='whatsapp:+14155238886',
			body=body,
			to='whatsapp:+919939795774')
		print(tosend.sid)

client.run(TOKEN)