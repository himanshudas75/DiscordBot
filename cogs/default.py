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

	@commands.Cog.listener()
	async def on_message(self,message):
		bot=self.bot
		if message.author.id == bot.user.id:
			return
		if message.author.bot:
			message.channel.send("Tum bot ho")
		await bot.process_commands(message)

def setup(bot):
	bot.add_cog(Default(bot))