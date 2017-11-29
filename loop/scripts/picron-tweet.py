import tweepy
import requests
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)
consumer_key = r.get('twitter_consumer_key')
consumer_secret = r.get('twitter_consumer_secret')
access_token = r.get('twitter_access_token')
access_token_secret = r.get('twitter_access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
tapi = tweepy.API(auth)

status_message = ""

response = requests.get('http://picron.local:5000/')
status_message += "Current time: {}".format(response.text)

chaperon_lock = r.get('chaperon_lock')
status_message += "\n There: {}".format(chaperon_lock)

response = requests.get('http://picron.local:5000/now/playing/')
status_message += "\n Now playing: {}".format(response.text)

tapi.update_status(status_message)
