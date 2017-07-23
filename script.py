import tweepy
import csv
import pandas as pd
import re
import numpy as np

####input your credentials here
consumer_key = '2bC3YFasI97knhI8orLF2Hco2'
consumer_secret = 'Yrh5yqze4LiuetVIC5m6RahpKdNfZTnASQHFW4Eewe8kNV3LAo'
access_token = '162357846-Nx0AreahmxYHGAEJm9EejOktvHGgSWwHxrmQVSQJ'
access_token_secret = 'WBzS2DsHAe4v9O00DpW0z8DnBqtz0kpkCw1E22pW9Tf3r'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# The search term you want to find
query = "Andela Nigeria"

# Language code (follows ISO 639-1 standards)
language = "en"

# Number of tweets to pull
tweetCount = 20

# Calling the user_timeline function with our parameters
results = api.search(q=query, lang=language, count=tweetCount)

# util functions:
def clean_tweet(tweet_text):
    # remove any 'RT' at the beginning of the tweet_text
    tweet_text = re.sub(r'^RT\s{1}', '', tweet_text)
    # convert www.* or https?://* to URL
    tweet_text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))',' ',tweet_text)
    # convert @username to AT_USER
    tweet_text = re.sub('@[^\s]+',' ',tweet_text)
    # remove additional white spaces
    tweet_text = re.sub('[\s]+', ' ', tweet_text)
    # remove every 'hash' from words
    tweet_text = re.sub(r'#([^\s]+)', r'\1', tweet_text)
    #r emove quotes
    tweet_text = tweet_text.strip('\'"')
    # remove punctuation
    tweet_text = re.sub(r'[\.\,\-,\!,\?]', '', tweet_text)
    # remove preceeding and trailing whitespace
    tweet_text = tweet_text.strip()
    return tweet_text

def get_vocabulary(tweet_list):
    # join all words in each dataset row into one string
    joined_tweets = " ".join(tweet_list)
    vocabulary = list(set(joined_tweets.split(' ')))
    return vocabulary

# start processing tweets
def process_tweets(results):
    # foreach through all tweets pulled
    processed_tweets = []
    for result in results:
        # grab the main tweet
        tweet_text = clean_tweet(result.text)
        processed_tweet = {'text': tweet_text}
        processed_tweets.append(processed_tweet)
    return processed_tweets

# ---------------------------------------------------

tweet_list = pd.read_csv('data/tweets.csv')['text'].tolist()
vocabulary = get_vocabulary(tweet_list)

print "tweet_list[0]: ", tweet_list[0]
print "vocabulary: ", vocabulary

def tweet_to_matrix_row(tweet):
    tweet_words = tweet.split(' ')
    matrix_row = [0] * len(vocabulary)
    for word in tweet_words:
        index = vocabulary.index(word)
        matrix_row[index] = 1
    return matrix_row

sentiment_matrix =  map(tweet_to_matrix_row, tweet_list)
print "sentiment_matrix[0]: ", sentiment_matrix[0]
# import pdb; pdb.set_trace()
