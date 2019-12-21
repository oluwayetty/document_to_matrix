<<<<<<< HEAD
import tweepy
import csv
import pandas as pd
import re
import numpy as np
import os

####input your credentials here
consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

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
        matrix_row[index] += 1
    return matrix_row

sentiment_matrix =  map(tweet_to_matrix_row, tweet_list)
print "sentiment_matrix[0]: ", sentiment_matrix[0]
# import pdb; pdb.set_trace()
=======
import re, math
from collections import Counter
import numpy as np

text1 = 'How can I be a geologist?'
text2 = 'What should I do to be a geologist?'

class Similarity():
    def compute_cosine_similarity(self, string1, string2):
         # intersects the words that are common
         # in the set of the two words
         intersection = set(string1.keys()) & set(string2.keys())
         # dot matrix of vec1 and vec2
         numerator = sum([string1[x] * string2[x] for x in intersection])

         # sum of the squares of each vector
         # sum1 is the sum of text1 and same for sum2 for text2
         sum1 = sum([string1[x]**2 for x in string1.keys()])
         sum2 = sum([string2[x]**2 for x in string2.keys()])

         # product of the square root of both sum(s)
         denominator = math.sqrt(sum1) * math.sqrt(sum2)
         if not denominator:
            return 0.0
         else:
            return round(numerator/float(denominator),4)

    def text_to_vector(self,text):
        WORD = re.compile(r'\w+')
        words = WORD.findall(text)
        return Counter(words)

    # Jaccard Similarity
    def tokenize(self,string):
        return string.lower().split(" ")

    def jaccard_similarity(self, string1, string2):
        intersection = set(string1).intersection(set(string2))
        union = set(string1).union(set(string2))
        return len(intersection)/float(len(union))

similarity = Similarity()

# vector space
vector1 = similarity.text_to_vector(text1)
vector2 = similarity.text_to_vector(text2)

# split words into tokens
token1 = similarity.tokenize(text1)
token2 = similarity.tokenize(text2)

cosine = similarity.compute_cosine_similarity(vector1, vector2)
print 'Cosine Similarity:', cosine

jaccard = similarity.jaccard_similarity(token1,token2)
print 'Jaccard Similarity:', jaccard
>>>>>>> similarity-index/master
