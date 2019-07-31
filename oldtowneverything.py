import tweepy
import urllib.request
import json

CONSUMER_KEY = "WDvB4FT1c67N2GBgijgC9a7tq"
CONSUMER_SECRET = "2bKGOMkGkFzJCVW25BIiRIzS6yurUwY0hiKVfYzp4i7uVRasMr"
ACCESS_TOKEN = "4560347689-eR1Jbr8XtKxrvS1ZzcqpBhfyV4OGHyxEj2jt171"
ACCESS_TOKEN_SECRET = "7IbI6zPdIZ74g334GcY4y9aZR4UhfhU6zfMtffhTleehW"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

req = urllib.request.urlopen("https://api.noopschallenge.com/wordbot?set=nouns").read()
word = req.decode("utf-8")
print(word[11:len(word)-3])
