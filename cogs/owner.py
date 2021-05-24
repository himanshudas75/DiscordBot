import discord
from discord.ext import commands
import re

class Owner(commands.Cog):

	def __init__(self,bot):
		self.bot=bot

	def is_guild_owner():
		def predicate(ctx):
			return ctx.guild is not None and ctx.guild.owner_id==ctx.author.id
		return commands.check(predicate)

	@commands.command(name='clear',help='Clears the specified number of messages')
	@commands.check_any(commands.is_owner(),is_guild_owner())
	async def clear(self,ctx,amount=2):
		await ctx.channel.purge(limit=amount)

	@commands.command(name='kick',help='Kick a user')
	@commands.check_any(commands.is_owner(),is_guild_owner())
	async def kick(self,ctx,member:discord.Member,*,reason=None):
		await member.kick(reason=reason)
		await ctx.send(f'Kicked {member.mention}\nReason: {reason}')

	@commands.command(name='ban',help='Ban a user')
	@commands.check_any(commands.is_owner(),is_guild_owner())
	async def ban(self,ctx,member:discord.Member,*,reason=None):
		await member.ban(reason=reason)
		await ctx.send(f'Banned {member.mention}\nReason: {reason}')

	@commands.command(name='unban',help='Unban a user')
	@commands.check_any(commands.is_owner(),is_guild_owner())
	async def unban(self,ctx,*,member):
		banned_users=await ctx.guild.bans()
		member_name,member_discriminator=member.split('#')
		for ban_entry in banned_users:
			user=ban_entry.user
			if (user.name,user.discriminator)==(member_name,member_discriminator):
				await ctx.guild.unban(user)
				await ctx.send(f'Unbanned {user.mention}')
				return
		await ctx.send(f"User {member} is not banned")

	@commands.command(name='status',help='Unban a user')
	@commands.check_any(commands.is_owner(),is_guild_owner())
	async def status(self,ctx,status,*,game=None):
		bot=self.bot
		status=status.lower()
		game=discord.Game(game)
		if status == 'online':
			await bot.change_presence(status=discord.Status.online,activity=game)
		elif status == 'idle':
			await bot.change_presence(status=discord.Status.idle,activity=game)
		elif status == 'offline':
			await bot.change_presence(status=discord.Status.offline,activity=game)
		elif status == 'invisible':
			await bot.change_presence(status=discord.Status.invisible,activity=game)
		elif status == 'dnd':
			await bot.change_presence(status=discord.Status.dnd,activity=game)
		elif status == 'do_not_disturb':
			await bot.change_presence(status=discord.Status.do_not_disturb,activity=game)
		else:
			await ctx.send('Please enter correct status')
			
def setup(bot):
	bot.add_cog(Owner(bot))