# Import required modules
import os
import sys
import time
import tweepy

# Define the post_tweet() function
def post_tweet(twitter_api, tweet):
	# Function: post_tweet()
	# Purpose: Post a given Tweet
	# Arguments:
	#	twitter_api - The Twitter API object
	#	tweet - The Tweet to post
	
	# Display a status message
	print("[{0}][S] Posting Tweet: {1}...".format(time.asctime(time.localtime(time.time())), tweet))
	
	# Update the status
	twitter_api.update_status(status=tweet)
