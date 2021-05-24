import discord
from discord.ext import commands

class Naughty(commands.Cog):

	def __init__(self,bot):
		self.bot=bot

	@commands.command(name='nsfw',help='Not Safe For Work')
	@commands.is_nsfw()
	async def nsfw(self,ctx,arg1='',arg2=''):
		from bot_commands import hentai
		li=hentai.hentai(arg1,arg2,True)
		if isinstance(li,str):
			await ctx.send(li)
		else:
			for i in li:
				emb=discord.Embed()
				emb.set_image(url=i)
				await ctx.send(embed=emb)

	@commands.command(name='sfw',help='Safe For Work')
	async def sfw(self,ctx,arg1='',arg2=''):
		from bot_commands import hentai
		li=hentai.hentai(arg1,arg2,False)
		if isinstance(li,str):
			await ctx.send(li)
		else:
			for i in li:
				emb=discord.Embed()
				emb.set_image(url=i)
				await ctx.send(embed=emb)

def setup(bot):
	bot.add_cog(Naughty(bot))