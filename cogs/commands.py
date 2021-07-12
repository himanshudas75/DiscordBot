import discord
from discord.ext import commands

class Commands(commands.Cog):

	def __init__(self,bot):
		self.bot=bot

	@commands.command(name='define',help='Shows the definition of a word')
	async def define(self,ctx,*,arg):		#Dictionary
		from bot_commands import oxford
		mean=oxford.meaning(arg)
		if mean==-1:
			await ctx.send('Definition Not Found')
		else:
			defembed=discord.Embed(title=mean["id"],color=0x00ff00)
			defembed.add_field(name="Language",value=mean["language"],inline=False)
			defembed.add_field(name="Definition",value=mean["definition"],inline=False)
			await ctx.send(embed=defembed)

	@commands.command(name='ping',help='Checks the ping of the bot')
	async def ping(self,ctx):
		bot=self.bot
		await ctx.send(f'Pong! : {round(bot.latency*1000)}ms')

	@commands.command(name='maths',help='+, -, /, //, *, **, ^ -> 2 numbers')
	async def maths(self,ctx,*,args):		#Mathematical Calculations
		from bot_commands import maths
		ans=maths.solve(args)
		await ctx.send(ans)

	@commands.command(name='movie',help='Get details of movie,series, or episode')
	async def det(self,ctx,*,args):		#Movie Details
		from bot_commands import omdb
		details=omdb.search(args)
		if(isinstance(details,str)):
			await ctx.send(details)
		else:
			detembed=discord.Embed(title='Title',description=details['Title'],color=0x0000ff)
			li=['Year','Rated','Released','Runtime','Genre','Director','Actors','Plot','Language','Country']
			for field in li:
				detembed.add_field(name=field,value=details[field],inline=False)

			if 'imdbRating' in details:
				detembed.set_footer(text='IMDB Rating: '+details['imdbRating'])

			if not details['Poster']=='N/A':
				detembed.set_image(url=details['Poster'])

			await ctx.send(embed=detembed)
		
def setup(bot):
	bot.add_cog(Commands(bot))