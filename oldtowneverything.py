import tweepy
import urllib.request
import json

CONSUMER_KEY = "dZVaXOw7japUrPNlfce4TApWI"
CONSUMER_SECRET = "OHZrtcT1xgSJIokPL1QegpAFWbx7hFVJL9HB6vvg6sy7hEZWrR"
ACCESS_TOKEN = "1156645481193377792-La6scf0bT1izzMkR7ez7BtTpaBEIdp"
ACCESS_TOKEN_SECRET = "SDGmaw3oIwoDatYCEyeomTB7yAdnHiRnIAhbyNhGuf7dZ "

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

req = urllib.request.urlopen("https://api.noopschallenge.com/wordbot?set=nouns").read()
word = req.decode("utf-8")[11:len(word)-3]

api.update_status("I got the ", word[11:len(word)-3], "in the back")
