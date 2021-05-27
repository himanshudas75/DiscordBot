import discord
from discord.ext import commands
import json

class Default(commands.Cog):

	def __init__(self,bot):
		self.bot=bot

	@commands.Cog.listener()
	async def on_ready(self):
		bot=self.bot
		print(f'{bot.user} is connected to the following guild(s):')
		for guild in bot.guilds:
			print(f' - {guild.name} : {guild.id}')
			for channel in guild.channels:
				if channel.name=='general':
					await channel.send('Hey! I am online.')
					#print('Hello')
	
	@commands.Cog.listener()
	async def on_guild_join(self,guild):
		with open('queue_list.json','r') as f:
			queuelist=json.load(f)
		queuelist[str(guild.id)]=[]
		with open('queue_list.json','w') as f:
			json.dump(queuelist,f,indent=4)
	
	@commands.Cog.listener()
	async def on_guild_remove(self,guild):
		with open('queue_list.json','r') as f:
			queuelist=json.load(f)
		queuelist.pop(str(guild.id))
		with open('queue_list.json','w') as f:
			json.dump(queuelist,f,indent=4)

	@commands.Cog.listener()
	async def on_command_error(self,ctx,error):
		from error_handling import get_error
		er=get_error(error)
		await ctx.send(er)

	@commands.Cog.listener()
	async def on_member_join(self,member):
		await member.create_dm()
		await member.dm_channel.send(f'Hi {member.name}, welcome to my Discord Server!')
    
def setup(bot):
	bot.add_cog(Default(bot))