# Follow users from a list using Tweepy
# MIT License
# March 2017
# [] indicates user entry

import tweepy

# Find keys and tokens @ apps.twitter.com
consumer_key = '[insert consumer key here]'
consumer_secret = '[insert consumer secret here]'
access_token = '[insert access token here]'
access_token_secret = '[insert access token secret here]'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Paste in a comma separate list of usernames - e.g. ["tcampbelltweets","nickelcommerce","DFWStartupWeek","LaunchDFW"] 
follow_this_list = ["[insert twitter username here]","[insert twitter username here]","[insert twitter username here]"]
list_to_follow = list(set(follow_this_list))
list_length = len(list_to_follow)

# Confirm you want to follow this list
answer = raw_input("Follow " + str(list_length) + " users? [Y/n]").lower()
if answer and answer[0] != "y":
    sys.exit()

# Add usernames to account and count as you go
count = 0
for i in list_to_follow:
    api.create_friendship(i)
    count += 1

# Confirm when users have actually been followed
print "Congrats, you just added %s users" % list_length
