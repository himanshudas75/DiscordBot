import discord
from discord.ext import commands
from discord import FFmpegPCMAudio

class VC(commands.Cog):

    def __init__(self,bot):
        self.bot=bot

    @commands.command()
    async def join(self,ctx):
        try:
            channel=ctx.author.voice.channel
            await channel.connect()
            await ctx.send(f'Joined VC {channel}')
        except AttributeError:
            await ctx.send('Join a VC first!')
    
    @commands.command()
    async def leave(self,ctx):
        try:
            vc=ctx.voice_client
            await vc.disconnect()
            await ctx.send(f'Disconnected from VC')
        except AttributeError:
            await ctx.send('I am not in a VC!')
			
def setup(bot):
	bot.add_cog(VC(bot))