import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import os
import re

class VC(commands.Cog):

    def __init__(self,bot):
        self.bot=bot

    @commands.command(name='join',help='Make bot join a VC')
    async def join(self,ctx):
        if ctx.author.voice:
            channel=ctx.author.voice.channel
            await channel.connect()
            emb=discord.Embed(title=f'Joined VC {channel}')
            await ctx.send(embed=emb)
        else:
            await ctx.send('Join a VC first!')
    
    @commands.command(name='leave',help='Make bot leave the VC')
    async def leave(self,ctx):
        if ctx.voice_client:
            vc=ctx.voice_client
            await vc.disconnect()
            emb=discord.Embed(title='Disconnected from VC')
            await ctx.send(embed=emb)
        else:
            await ctx.send('I am not in a VC!')
    
    @commands.command(name='play',help='Play an audio')
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
            if name=='gitignore':
                continue
            if args.lower() == name.lower():
                found=filename
                break
        if not found:
            await ctx.send('Song not found')
            return

        source=FFmpegPCMAudio(f'./audios/{filename}')
        voice=discord.utils.get(bot.voice_clients,guild=ctx.guild)
        voice.play(source)
    
    @commands.command(name='list',help='List the songs in directory')
    async def _list(self,ctx):
        li=[]
        for filename in os.listdir('./audios'):
            name=re.findall('\w+',filename)[0]
            if name=='gitignore':
                continue
            li.append(name)
        li=', '.join(li)
        await ctx.send(li)

def setup(bot):
    bot.add_cog(VC(bot))