from secret import client_secret
import discord
from discord.ext import commands
import sys, traceback
from os import listdir
from os.path import isfile, join
import asyncio
import time

description = '''Built to be a functioning auction bot'''
bot = commands.Bot(command_prefix='>', description=description)
client = discord.Client()

cmd_dir = "commands"

#permission int 93280
@bot.command(pass_context=True)
async def invite(ctx):
	await ctx.message.author.send("**Invite me here: \nhttps://discordapp.com/oauth2/authorize?client_id=746823384519802921&scope=bot&permissions=93280**")

if __name__ == "__main__":
	for extension in [f.replace('.py', '') for f in listdir(cmd_dir) if isfile(join(cmd_dir, f))]:
		try:
			bot.load_extension(cmd_dir + "." + extension)
		except Exception as e:
			print('Failed to load extension {extension}')
			traceback.print_exc()

@bot.event
async def on_command_error(ctx, error):
	author = ctx.message.author
	authorm = ctx.message.author.mention
	channel = ctx.message.channel
	if isinstance(error, commands.CommandOnCooldown):
		await channel.send(content="**:x: This command is on a %.2fs cooldown {}**".format(author) % error.retry_after, delete_after=3)	
		return
	if isinstance(error, commands.CommandNotFound):
		await channel.send(content="**:x: {} Command not found**".format(authorm), delete_after=3)
		return
	if isinstance(error, commands.MissingRequiredArgument):
		await channel.send(content="**:x: {} Missing Arguments**".format(authorm), delete_after=3)
		return
	print(error)
	error=discord.Embed(description="**:x: Got an Error**\n```py\n{}\n```".format(error), colour=discord.Colour(value=0xff0707))
	error.add_field(name="User", value="{}".format(authorm), inline=True)
	error.add_field(name="Command+Content", value="{}".format(ctx.message.content), inline=True)
	await channel.send(embed=error)
	return

bot.run(client_secret)