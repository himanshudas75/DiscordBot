import discord
from discord.ext import commands

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
	async def on_command_error(self,ctx,error):
		await ctx.send(error)

	@commands.Cog.listener()
	async def on_member_join(self,member):
		await member.create_dm()
		await member.dm_channel.send(f'Hi {member.name}, welcome to my Discord Server!')
    
def setup(bot):
	bot.add_cog(Default(bot))