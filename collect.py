try:
    import json
except ImportError:
    import simplejson as json

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

access_token = "841163774983884800-7MKXWJE5AZrfEGZ7GxupUl7iL35a7VE"
access_secret = "VlinyeyHnEBHTUwZ9RCCLCaUBO9C7F99NddEgRfbVxovf"
consumer_key = "QiUIFH5wLD1xoTy2KnAVS8J6y"
consumer_secret = "cw7gtMfHxFrxuHr1zzPlxiSpTt80TXHXxCWbrcPKUg9RKRSgY8"

oauth = OAuth(access_token, access_secret, consumer_key, consumer_secret)

twitter_stream = TwitterStream(auth=oauth, domain="userstream.twitter.com")

iterator = twitter_stream.statuses.filter(track="walmart")


tweet_count = 10000
for tweet in iterator:
    tweet_count -= 1
    print (json.dumps(tweet))

    if tweet_count <= 0:
        break
