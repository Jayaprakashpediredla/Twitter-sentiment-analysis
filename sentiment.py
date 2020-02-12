import tweepy
from textblob import textblob

consumer_key='XDsPC3y9JMQrT4t9xrJf8gp6o'
consumer_secret='S3PD0a8F4DZg959k1D8kpQer0eWoFscs129ka4pCZxOqi7wQni'

access_token='581756115-sljf6KFrUxXdd0VIdzWiULtfIkDBpjqkb4oKVj7u'
acces_token_secret='dlG3pHAiYIHMe4Sl2skA0qbKClkFzUuQhVdm6mwZzcQRo'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,acces_token_secret)

api=tweepy.API(auth)

public_tweets=api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis=TextBlob(tweet.text)
	print(analysis.sentiment)
