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

polarity=0
positive=0
neutral=0
negative=0

#clean up (get rid of 'RT' and '@' handles if a tweet has them)
for tweet in tweets.data:
    clean_text=tweet.id.text.replace('RT','')
    if clean_text.startswith(' @'):
        position=clean_text.index(':')
        clean_text=clean_text[position+2:]
    if clean_text.startswith('@'):
      position=clean_text.index(' ')
      clean_text=clean_text[position+2:]
    #get overall polarity (how positive or negative)
    analysis=TextBlob(clean_text)
    tweet_polarity=analysis.polarity
    if tweet_polarity>0.20:
       positive+=1
    elif tweet_polarity==0.00:
       neutral+=1
    elif tweet_polarity<0.20 :
       negative+=1

    polarity+=tweet_polarity

print("The overall sentiment from -1 to 1 (1 being positive. -1 being negitive) is: {polarity}")
   
