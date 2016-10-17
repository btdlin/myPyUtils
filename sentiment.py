import tweepy
from textblob import TextBlob

consumer_key = 'CM3SnbFGkNAJv5HzBaeL4nOqU'
consumer_secret = '6VsZ5FUoQKvZ7m7Lt7peEhFwlBi8OJjBG7SnvUNVG7Tsc0DFyD'

access_token = '15273080-1fz4d4Spk1CD0XaqFgegsVPYUH3tPZ1QJ3AzgcGDC'
access_token_secret = 'w2mZFywXgkp59sOOjasvvazdViVP6jyNHBcp9lEMY3nQG'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
public_tweets = api.search('新垣結衣')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)

