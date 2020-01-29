'''SQLAlchemy models for TwitOff'''
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()


class User(DB.Model):
    '''Twitter users that we query and store historical tweets'''
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), unique=True, nullable=False)
    newest_tweet_id = DB.Column(DB.BigInteger)
    # Can store image / followers / total tweets etc

    def __repr__(self):
        return '<User {}>'.format(self.name)


class Tweet(DB.Model):
    '''stores tweets'''
    id = DB.Column(DB.Integer, primary_key=True)
    text = DB.Column(DB.Unicode(280))
    embedding = DB.Column(DB.PickleType, nullable=False)
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationship("User", backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return '<Tweets {}'.format(self.text)