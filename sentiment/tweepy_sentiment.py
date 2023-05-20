from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import tweepy
import numpy as np
import pandas as pd

class Import_tweet_sentiment:

	consumer_key="1OJRulwZ0aWbzwxMMW1Rslqhl"
	consumer_secret="5PqvUvyvHiwOYKoh0OCikUjflym0LmuizGwVfzCC7Hh5l2S6Bi"
	access_token="1162976157525929985-jVgz9FODDoO0bBWA2u8GS0QvLvyPGd"
	access_token_secret="tgiSHGKuRhGtJu9x9O9q2Zbu2OC4VwCe7pUHvlHVB2DTG"

	def tweet_to_data_frame(self, tweets):
		df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
		return df

	def get_tweets(self, handle):
		auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)
		auth_api = API(auth)

		account = handle
		item = auth_api.user_timeline(id=account,count=20)
		df = self.tweet_to_data_frame(item)

		all_tweets = []
		for j in range(20):
			all_tweets.append(df.loc[j]['Tweets'])
		return all_tweets

	def get_hashtag(self, hashtag):
		auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)
		auth_api = API(auth)

		account = hashtag
		all_tweets = []

		for tweet in tweepy.Cursor(auth_api.search_tweets, q=account, lang='en').items(20):
			all_tweets.append(tweet.text)

		return all_tweets
