import tweepy
from keys import keys

auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
auth.set_access_token(keys['access_token'], keys['access_token_secret'])

api = tweepy.API(auth, wait_on_rate_limit=True)