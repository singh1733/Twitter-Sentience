from textblob import TextBlob
import tweepy
import sys

my_keys=open('api_key.txt','r').read().splitlines()
api_key=my_keys[0]
api_key_secret=my_keys[2]
access_token=my_keys[4]
access_token_secret=my_keys[6]

#build a connection to the app
auth_handler=tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
auth_handler.set_access_token(access_token, access_token_secret)
api=tweepy.API(auth_handler)