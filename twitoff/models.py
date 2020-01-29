'''SQLAlchemy models for TwitOff'''
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class User(DB.Model):
    '''Twitter users that we query and store historical tweets'''
    id = DB.Column(DB.BigInteger, primary_key=True)
    username = DB.Column(DB.String(15), unique=True, nullable=False)
    # Can store image / followers / total tweets etc

class Tweets(DB.Model):
    '''stores tweets'''
    id = DB.Column(DB.Integer, primary_key=True)
    text = DB.Column(DB.Unicode(280))