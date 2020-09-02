import discord
from discord.ext import commands

import sys
sys.path.insert(1, 'E:\\Coding\\Auction bot\\commands\\local_utils')

import checks # pylint: disable=import-error

class admincmd(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, hidden=True)
    @checks.is_owner()
    async def stop(self, ctx):
        channel = ctx.message.channel
        try:
            await channel.send('Alright! See ya!')
            await self.bot.close()
            exit()
        except:
            exit()
    
    @commands.command(name='reload', hidden=True)
    @checks.is_owner()
    async def _reload(self, ctx : str):
        content = ctx.message.content
        channel = ctx.message.channel
        r_cog = content.split(' ')[1]
        self.bot.unload_extension(r_cog)
        self.bot.load_extension(r_cog)
        await channel.send(f"{r_cog} reloaded")
        return

    @commands.command(name='load', hidden=True)
    @checks.is_owner()
    async def _load(self, ctx : str):
        content = ctx.message.content
        channel = ctx.message.channel
        r_cog = content.split(' ')[1]
        self.bot.load_extension(r_cog)
        await channel.send(f"{r_cog} loaded")
        return

def setup(bot):
    bot.add_cog(admincmd(bot))