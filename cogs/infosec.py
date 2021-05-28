import discord
from discord.ext import commands
import json

com={}

class Infosec(commands.Cog):

    def __init__(self,bot):
        self.bot=bot
	
    def load(self):
        with open('./lists/infosec.json','r') as f:
            global com
            com=json.load(f)
    
    @commands.command(name='infosec',help='Shows some commonly used commands')
    async def infosec(self,ctx):
        self.load()
        global com
        for title in com:
            emb=discord.Embed(title=title,color=0xff0000)
            for subtitle in com[title]:
                emb.add_field(name=subtitle,value=com[title][subtitle],inline=False)
            await ctx.send(embed=emb)


def setup(bot):
	bot.add_cog(Infosec(bot))