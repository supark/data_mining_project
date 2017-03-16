try:
    import json
except ImportError:
    import simplejson as json

tweets_filename = 'collect.json'
tweet_file = open(tweets_filename, "r")

for line in tweet_file:
    try:
        tweet = json.loads(line.strip())
        if 'text' in tweet:
            print (tweet['text'])

    except:
        continue
