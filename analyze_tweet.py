import datetime

#keywords
lines = ['orange', 'red', 'silver', 'blue', 'green', 'yellow']
problems = ['single tracking', 'delays', 'disabled', 'track work', 'delayed', 'track problem']
status = ['continue', 'normal service']
#tweet_text = "Orange/red normal service"

#general search
def word_find(word_list, string):
    cstring = clean_string(string)
    result = filter(lambda x: x in cstring, word_list)
    return result

#main method
def analyze(author, tweet, time, tweet_id):
    
    parsed_tweet = {'line': word_find(lines, tweet), 'problem': word_find(problems, tweet), 'status': word_find(status, tweet)}
    print tweet
    print parsed_tweet

#clean it
def clean_string(string):
    string = string.replace(r"/", " ")
    return string.lower()

#print analyze(tweet_text)
#for word in word_find(lines, tweet_text):
 #   print(word)