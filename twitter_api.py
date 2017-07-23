
# get processed tweets write them to CSV file.
processed_tweets = process_tweets(results)
df = pd.DataFrame(processed_tweets)
filename = 'data/tweets.csv'
df.to_csv(filename, index=False, encoding='utf-8')
