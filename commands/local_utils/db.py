import asyncio
import traceback

from gino import Gino
from sqlalchemy import ForeignKey

dbo = Gino()

class Server(dbo.Model):
    __tablename__ = 'server'
    guildid = dbo.Column(dbo.Integer(), primary_key=True) # pylint: disable=no-member


class User(dbo.Model):
    __tablename__ = 'users'
    id = dbo.Column(dbo.Integer(), primary_key=True) # pylint: disable=no-member
    guild = dbo.Column(dbo.Integer(),None, ForeignKey('Server.guildid')) # pylint: disable=no-member
    funds = dbo.Column(dbo.Integer()) # pylint: disable=no-member

class dbc:
    async def add_guild(self, id):
        queryRes = Server.query.where(Server.guildid == id)
        #print(queryRes) #THIS BREAKS INITIALIZATION SOMEHOW! 
        if(queryRes == None):
            await Server.create(guildid=id)
            return True
        else:
            return False
    
    async def set_funds(self, guild, userid, amount):
        queryRes = User.query.where(User.id == userid and User.guild == guild).first()
        guild_db = Server.query.where(Server.guildid == guild)
        if(guild_db == None):
            return False, "Need setup"
        if(queryRes == None):
            await User.create(id=userid, guild=guild_db.id, funds=amount)
        else:
            await queryRes.update(funds=amount)

    async def close(self):
        await dbo.pop_bind().close()

    async def setup(self):
        try:
            await dbo.set_bind('postgresql://auction.db')
            await dbo.gino.create_all()
        except Exception as e:
            traceback.print_exc()
            print(f"unable to connect. {e}")
