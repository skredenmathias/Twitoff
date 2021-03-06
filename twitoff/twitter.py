# import tweepy
# import basilica
# from decouple import config
# from twitoff.models import User, DB, Tweet

# # Tweepy API code
# TWITTER_AUTH = tweepy.OAuthHandler(config('TWITTER_CONSUMER_API_KEY'), config('TWITTER_CONSUMER_API_SECRET'))
# TWITTER_AUTH.set_access_token(config('TWITTER_ACCESS_TOKEN'), config('TWITTER_ACCESS_TOKEN_SECRET'))
# TWITTER = tweepy.API(TWITTER_AUTH)
# # Basilica code
# BASILICA = basilica.Connection(config('BASILICA_KEY'))


# def add_or_update_user(name):
#   '''
#   Add or update a user and their Tweets.
#   Return an error if user does not exist or is private.
#   '''
#   try:
#     twitter_user = TWITTER.get_user(name)
#     db_user = (User.query.get(twitter_user.id) or User(id=twitter_user.id, name=name))
#     DB.session.add(db_user)
#     tweets = twitter_user.timeline(count = 200, exclude_replies=True,
#                                include_rts=False, tweet_mode='extended',
#                                since_id=db_user.newest_tweet_id)
#     if tweets:
#       db_users.newest_tweet_id = tweets[0].id
    
#     for tweet in tweets:
#       embedding = BASILICA.embed_sentence(tweet.text, model='twitter')
#       db_tweet = Tweet(id=tweet.id, text=tweet.text, embedding=embedding)
#       db_user.tweets.append(db_tweet)
#       DB.session.add(db_tweet)
#   except Exception as e:
#     print(f'Encountered error while processing {name}: {e}')
#     raise e
#   else:
#     DB.session.commit()

import basilica
import tweepy
from decouple import config

from twitoff.models import User, DB, Tweet

TWITTER_AUTH = tweepy.OAuthHandler(config('TWITTER_CONSUMER_API_KEY'), config('TWITTER_CONSUMER_API_SECRET'))
TWITTER_AUTH.set_access_token(config('TWITTER_ACCESS_TOKEN'), config('TWITTER_ACCESS_TOKEN_SECRET'))
TWITTER = tweepy.API(TWITTER_AUTH)
BASILICA = basilica.Connection(config("BASILICA_KEY"))


def add_or_update_user(name):
    """
    Add or update a user and their Tweets.
    Throw an error if user doesn't exist or private.
    """
    try:
        twitter_user = TWITTER.get_user(name)
        db_user = (User.query.get(twitter_user.id) or User(id=twitter_user.id, name=name))
        DB.session.add(db_user)
        tweets = twitter_user.timeline(count=200,
                                       exclude_replies=True,
                                       include_rts=False,
                                       since_id=db_user.newest_tweet_id)
        if tweets:
            db_user.newest_tweet_id = tweets[0].id

        for tweet in tweets:
            embedding = BASILICA.embed_sentence(tweet.text, model='twitter')
            db_tweet = Tweet(id=tweet.id, text=tweet.text, embedding=embedding)
            db_user.tweets.append(db_tweet)
            DB.session.add(db_tweet)
    except Exception as e:
        print(f'Error processing {name}: {e}')
        raise e
    else:
        DB.session.commit()


def update_all_users():
    """Update all Tweets for all Users in the User table."""
    for user in User.query.all():
        add_or_update_user(user.name)