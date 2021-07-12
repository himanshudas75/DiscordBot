import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
load_dotenv(f'{FILE_PATH}/env')

TOKEN=os.getenv('DISCORD_TOKEN')

intents=discord.Intents().all()
bot=commands.Bot(command_prefix='.',intents=intents)

def is_guild_owner():
	def predicate(ctx):
		return ctx.guild is not None and ctx.guild.owner_id==ctx.author.id
	return commands.check(predicate)

@bot.command(name='load',help='Load a cog')
@commands.check_any(commands.is_owner(),is_guild_owner())
async def load(ctx,extension):
	bot.load_extension(f'cogs.{extension}')
	await ctx.send(f'Extension {extension} has been loaded')

@bot.command(name='unload',help='Unload a cog')
@commands.check_any(commands.is_owner(),is_guild_owner())
async def unload(ctx,extension):
	bot.unload_extension(f'cogs.{extension}')
	await ctx.send(f'Extension {extension} has been unloaded')

@bot.command(name='reload',help='Reload a cog')
@commands.check_any(commands.is_owner(),is_guild_owner())
async def reload(ctx,extension):
	bot.unload_extension(f'cogs.{extension}')
	bot.load_extension(f'cogs.{extension}')
	await ctx.send(f'Extension {extension} has been reloaded')

for filename in os.listdir(f'{FILE_PATH}/cogs'):
	if filename.endswith('.py'):
		bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)