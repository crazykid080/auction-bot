from discord.ext import commands

def is_owner_check(message):
	async def predicate(message):
		return message.author.id == 316026178463072268
	return commands.check(predicate(message))

def is_owner():
    return commands.check(lambda ctx: is_owner_check(ctx.message))