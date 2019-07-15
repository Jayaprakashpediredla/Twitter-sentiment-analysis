import tweepy
from textblob import textblob

consumer_key='alh3JMDgGXDjtWWshSxU7l048'
consumer_secret='FlCZQVjp7WuD6UfWhr6JlQGaOPqxh9uS56oWPfIM2Bk1EPPzff'

access_token='581756115-QPC9CgAIOTkN3LLCkulMnE0Swir0FB5RAo6Ad0gi'
acces_token_secret='jvl3Ih0tmPDONgweAqDcs780FMeIgwJunpOyIu2I9j2xA'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,acces_token_secret)

api=tweepy.API(auth)

public_tweets=api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis=TextBlob(tweet.text)
	print(analysis.sentiment)