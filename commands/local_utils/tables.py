from gino import Gino

db = Gino()

class Server(db.Model):
    __tablename__ = 'server'
    guildid = db.Column(db.Integer(), primary_key=True) # pylint: disable=no-member


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True) # pylint: disable=no-member
    funds = db.Column(db.Integer()) # pylint: disable=no-member
