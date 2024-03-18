from textblob import TextBlob
import tweepy
import sys

my_keys=open('api_key.txt','r').read().splitlines()


# Authenticate to Twitter
client = tweepy.Client(
    bearer_token=my_keys[8],
    consumer_key=my_keys[0],
    consumer_secret=my_keys[2],
    access_token=my_keys[4],
    access_token_secret=my_keys[6]
)

#gather tweets
search_term='Ohio'
tweet_amount=100

tweets = client.search_recent_tweets(query=search_term, max_results=tweet_amount)

for tweet in tweets.data:
    print(tweet.id)
