# Import required modules
import os
import sys
import configparser
import tweepy

# Define the authenticate() function
def authenticate(config_file):
	# Function: authenticate()
	# Purpose: Authenticate with Twitter via OAuth
	# Arguments:
	#	config_file - The configuration file
	
	# Create a new configuration file parser
	config = configparser.ConfigParser()
	
	# Read the configuration file
	config.read(config_file)
	
	# Get the authentication token
	auth = tweepy.OAuthHandler(config["TWITTER"]["consumer_key"],
	                                 config["TWITTER"]["consumer_secret"])
	                                 
	# Set the access token
	auth.set_access_token(config["TWITTER"]["access_token"],
	                      config["TWITTER"]["access_token_secret"])
	                      
	# Return the Tweepy API object
	return tweepy.API(auth)
	
	
