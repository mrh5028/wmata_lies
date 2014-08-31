#WMATA Lies#

This python app pulls tweets from the official WMATA accounts and WMATA riders to create issues in a database and link the tweets to each issue.

For example: A rider tweets that there is an issue on the Orange Line. This is captured and an issue is created and linked to that tweet. Five minutes later the official WMATA account tweets about the same issue. This tweet is then tied to the existing issue.

##Why?##
Often riders report issues that are never reported by the official WMATA accounts. This program is meant to catch these lies by omission.

For now this is just the backend portion to write to database. I will make a Flask powered website to pull from the database and display all the issues and related tweets.

##Config##
A config.py is required containing:

CONSUMER_KEY = *Your Twitter API Consumer Key*
CONSUMER_SECRET = *Your Twitter API Consumer Secret*
ACCESS_TOKEN = *Your Twitter API Access Token*
ACCESS_TOKEN_SECRET = *Your Twitter API Access Token Secret*

##Needed##
Things I still need to implement:
* Database
* Robust wordlists
* Issue creation & compare to prevent duplicates