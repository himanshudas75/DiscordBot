import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import os
import re

class VC(commands.Cog):

    def __init__(self,bot):
        self.bot=bot

    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice:
            channel=ctx.author.voice.channel
            await channel.connect()
            await ctx.send(f'Joined VC {channel}')
        else:
            await ctx.send('Join a VC first!')
    
    @commands.command()
    async def leave(self,ctx):
        if ctx.voice_client:
            vc=ctx.voice_client
            await vc.disconnect()
            await ctx.send(f'Disconnected from VC')
        else:
            await ctx.send('I am not in a VC!')
    
    @commands.command()
    async def play(self,ctx,*,args):
        bot=self.bot
        if not ctx.author.voice:
            await ctx.send('Join a VC first!')
            return
        if not ctx.voice_client:
            await ctx.send('I am not in a VC!')
            return

        found=False
        for filename in os.listdir('./audios'):
            name=re.findall('\w+',filename)[0]
            if args.lower() == name.lower():
                found=filename
                break
        if not found:
            await ctx.send('Song not found')
            return

        source=FFmpegPCMAudio(f'./audios/{filename}')
        voice=discord.utils.get(bot.voice_clients,guild=ctx.guild)
        voice.play(source)
    
    @commands.command()

			
def setup(bot):
	bot.add_cog(VC(bot))