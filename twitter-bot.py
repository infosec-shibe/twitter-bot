# Twitter Bot
# Version 0.0.1
# By InfoSec Shibe

# Import required modules
import os
import sys
import time
import getopt
import random
import tweepy

from core import authenticate
from core import tweet

# Set the version and author
__version__ = "0.0.1"
__author__ = "InfoSec Shibe"

# Define the main() function
def main():
	# Function: main()
	# Purpose: Process command line arguments
	# Arguments: None
	
	# Attempt to process command line arguments with getopt()
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hvc:t:d:", ("help", "version", "config=", "tweets=", "delay="))
	except getopt.GetoptError as err_msg:
		# Display an error message and exit
		print("[time.asctime(time.localtime(time.time()))][E] Error processing command line arguments: {}!".format(err_msg))
		exit(0)
		
	# Define important variables with their default values
	config_file = "config.cfg"
	tweets_file = None
	delay = 3600
		
	# Build a for loop to process command line arguments
	for opt, arg in opts:
		# If the -h or --help arguments were specified
		if opt in ("-h", "--help"):
			# Display the help message and exit
			print("USAGE:")
			print("\t{} [-h] [-v] [-c CONFIG] [-t TWEETS] [-d DELAY]")
			print("")
			print("A simple Twitter bot that posts regularly at a user specified interval")
			print("")
			print("REQUIRED ARGUMENTS:")
			print("\t-t, --tweets TWEETS\tThe list of Tweets to post")
			print("")
			print("OPTIONAL ARGUMENTS:")
			print("\t-h, --help\tDisplay the help message and exit")
			print("\t-v, --version\tDisplay the version message and exit")
			print("\t-c, --config CONFIG\tThe configuration file. Default is 'config.cfg'")
			print("\t-d, --delay DELAY\tThe delay, in seconds, to wait between posting. Default is 1 hour (3600)")
			exit(0)
			
		# If the -v or --version arguments were specified
		elif opt in ("-v", "--version"):
			# Display the version message and exit
			print("Twitter Bot")
			print("Version {}".format(__version__))
			print("By {}".format(__author__))
			exit(0)
			
		# If the -c or --config arguments were specified
		elif opt in ("-c", "--config"):
			# Set the configuration file
			config_file = arg
			
		# If the -t or --tweets arguments were specified
		elif opt in ("-t", "--tweets"):
			# Set the tweets file
			tweets_file = arg
			
		# If the -d or --delay arguments were specidied
		elif opt in ("-d", "--delay"):
			# Set the delay
			delay = int(arg)
	
	# Authenticate with Twitter and get an API object
	twitter_api = authenticate.authenticate(config_file)
	
	# Attempt to open the tweets file
	try:
		tweets = open(tweets_file, "r").readlines()
	except IOError as err_msg:
		# Display error message and exit
		print("[time.asctime(time.localtime(time.time()))][E] Error opening Tweets: {}!".format(err_msg))
		exit(0)
		
	# Create a loop to post all Tweets
	while len(tweets) > 0:
		# Select a random Tweet
		random_tweet = random.choice(tweets)
		
		# Tweet the Tweet
		tweet.post_tweet(twitter_api, random_tweet)
		
		# Remove the Tweet from the list
		tweets.remove(random_tweet)
		
		# Sleep
		time.sleep(delay)
		
	# Display a final status message and exit
	print("[time.asctime(time.localtime(time.time()))][S] Posted all Tweets! Exiting...")
	exit(0)
	
# Make sure not running as a module and call main
if __name__ == "__main__":
	main()	
