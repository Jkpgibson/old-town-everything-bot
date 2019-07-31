import tweepy
import urllib.request
import json

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

req = urllib.request.urlopen("https://api.noopschallenge.com/wordbot?set=nouns").read()
word = req.decode("utf-8")
print(word[11:len(word)-3])

api.update_status("I got the ", word, "in the back")
