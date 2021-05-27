import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import os

queue={}

class VC(commands.Cog):

    def __init__(self,bot):
        self.bot=bot

    def check(self,ctx):
        bot=self.bot
        if not ctx.author.voice:
            error=discord.Embed(title=bot.user.name,description='Join a VC first!')
            return error
        if not ctx.voice_client:
            error=discord.Embed(title=bot.user.name,description='I am not in a VC!')
            return error
        return 'Passed'

    def get_list(self):
        li=[]
        for filename in os.listdir('./audios'):
            if filename=='.gitignore':
                continue
            li.append(filename)
        return li
    
    def add_queue(self,name,id):
        if id in queue:
            queue[id].append(name)
        else:
            queue[id]=[name]

    @commands.command(name='join',help='Make bot join a VC')
    async def join(self,ctx):
        bot=self.bot
        if ctx.author.voice:
            channel=ctx.author.voice.channel
            await channel.connect()
            emb=discord.Embed(title=bot.user.name,description=f'Joined VC **{channel}**')
            await ctx.send(embed=emb)
        else:
            emb=discord.Embed(title=bot.user.name,description='Join a VC first!')
            await ctx.send(embed=emb)
    
    @commands.command(name='leave',help='Make bot leave the VC')
    async def leave(self,ctx):
        bot=self.bot
        ch=self.check(ctx)
        if not isinstance(ch, str):
            await ctx.send(embed=ch)
            return

        vc=ctx.voice_client
        await vc.disconnect()
        emb=discord.Embed(title=bot.user.name,description='Disconnected from VC')
        await ctx.send(embed=emb)
        
    @commands.command(name='list',help='List the songs in directory')
    async def _list(self,ctx):
        bot=self.bot
        li=self.get_list()
        lis='The list of audios in the directory: \n'
        for i in range(len(li)):
            lis+=f'{i+1}. {li[i].split(".")[0]}\n'
        lis=lis.strip()
        emb=discord.Embed(title=bot.user.name,description=lis)
        await ctx.send(embed=emb)

    @commands.command(name='play',help='Play an audio')
    async def play(self,ctx,*,args):
        bot=self.bot
        ch=self.check(ctx)
        if not isinstance(ch, str):
            await ctx.send(embed=ch)
            return
        
        found=False
        li=self.get_list()
        if args.isnumeric():
            found=True
            if int(args)>len(li):
                toplay=len(li)
            else:
                toplay=int(args)
        else:
            for i in range(len(li)):
                if li[i].split('.')[0].lower() == args.lower():
                    toplay=i+1
                    found=True
                    break
            
        if not found:
            emb=discord.Embed(title=bot.user.name,description='Song not found')
            await ctx.send(embed=emb)
            return

        source=FFmpegPCMAudio(f'./audios/{li[toplay-1]}')
        voice=ctx.voice_client
        if voice.is_playing():
            self.add_queue(li[toplay-1].split(".")[0],ctx.message.guild.id)
            emb=discord.Embed(title=bot.user.name,description=f'**{li[toplay-1].split(".")[0]}** added to queue')
            await ctx.send(embed=emb)
        else:
            voice.play(source)
            emb=discord.Embed(title=bot.user.name,description=f'Now Playing **{li[toplay-1].split(".")[0]}**')
            await ctx.send(embed=emb)

    @commands.command(name='pause',help='Pause the player')
    async def pause(self,ctx):
        bot=self.bot
        ch=self.check(ctx)
        if not isinstance(ch, str):
            await ctx.send(embed=ch)
            return

        voice=ctx.voice_client
        if voice.is_playing():
            voice.pause()
            emb=discord.Embed(title=bot.user.name,description='Paused the player')
            await ctx.send(embed=emb)
        else:
            emb=discord.Embed(title=bot.user.name,description='No audio is playing')
            await ctx.send(embed=emb)

    @commands.command(name='resume',help='Resume the player')
    async def resume(self,ctx):
        bot=self.bot
        ch=self.check(ctx)
        if not isinstance(ch, str):
            await ctx.send(embed=ch)
            return
        
        voice=ctx.voice_client
        if voice.is_paused():
            voice.resume()
            emb=discord.Embed(title=bot.user.name,description='Resumed the player')
            await ctx.send(embed=emb)
        else:
            emb=discord.Embed(title=bot.user.name,description='Player is not paused')
            await ctx.send(embed=emb)

    @commands.command(name='stop',help='Stop the player')
    async def stop(self,ctx):
        bot=self.bot
        ch=self.check(ctx)
        if not isinstance(ch, str):
            await ctx.send(embed=ch)
            return
        
        voice=ctx.voice_client
        voice.stop()
        emb=discord.Embed(title=bot.user.name,description='Stopped the player')
        await ctx.send(embed=emb)
        
def setup(bot):
    bot.add_cog(VC(bot))