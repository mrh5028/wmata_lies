import datetime
import tweepy
import json
import analyze_tweet

#import Twitter auth info from config
from config import CONSUMER_KEY
from config import CONSUMER_SECRET
from config import ACCESS_TOKEN
from config import ACCESS_TOKEN_SECRET

class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        #Decode JSON format
        decoded = json.loads(data)

        #Get Text and Author
        tweet_author = decoded['user']['screen_name'].encode('ascii', 'ignore')
        tweet_text = decoded['text'].encode('ascii', 'ignore')
        tweet_time = decoded['created_at']
        tweet_id_str = decoded['id_str']
        
        analyze_tweet.analyze(tweet_author, tweet_text, tweet_time, tweet_id_str)
        
        return True

    def on_error(self, status):
        print status

#Get WMATA Tweets
if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    print "Showing all new tweets"

    stream = tweepy.Stream(auth, l)
    stream.filter(track=['wmata'], follow=['1522468057', '18938912']) #filter for wmata mentions and tweets from metrorailinfo and wmata
    #stream.filter(track=['orange']) #for testing