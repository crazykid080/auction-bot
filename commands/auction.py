import sys

import discord
import sqlalchemy
from discord.ext import commands
import importlib

sys.path.insert(1, 'E:\\Coding\\Auction bot\\commands\\local_utils')
from db import dbc # pylint: disable=import-error
import checks # pylint: disable=import-error

class auction(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.db = dbc()
        self.db.setup()

    @commands.command(hidden=True)
    @checks.is_owner()
    async def closedb(self, ctx):
        await self.db.close

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_guild=True)
    async def setup(self, ctx):
        channel = ctx.message.channel
        guildid = ctx.message.guild.id
        result = await self.db.add_guild(guildid)
        if(result == True):
            await channel.send("Successfully initialized")
        else:
            await channel.send("Already initialized")
        return

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_guild=True)
    async def add_funds(self, ctx):
        channel = ctx.message.channel
        await channel.send("Not Implemented")
        return
    
    @commands.command(pass_context=True)
    @commands.has_permissions(manage_guild=True)
    async def set_funds(self, ctx):
        guild = ctx.message.guild # pylint: disable=unused-variable # Will use soon
        user_list = ctx.message.mentions
        channel = ctx.message.channel
        if len(user_list != 1):
            channel.send("Must specify one user.")
            return
        return

def setup(bot):
    bot.add_cog(auction(bot))
