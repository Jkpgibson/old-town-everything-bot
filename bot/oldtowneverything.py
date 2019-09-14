import tweepy
import urllib.request
import json
import os
import time

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")


# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

req = urllib.request.urlopen("https://api.noopschallenge.com/wordbot?set=nouns").read()
word = req.decode("utf-8")
shell = "I got the {0} in the back"
phrase = shell.format(word[11:len(word)-3])

api.update_status(phrase)

time.sleep(3600)
