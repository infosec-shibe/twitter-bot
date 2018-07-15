# Simple Twitter Bot
A simple Twitter bot written in Python 3 using Tweepy. Posts randomly from a list of Tweets on a user-specified timer.
## Usage
#### Tweets File
The Tweets file should be a plaintext file that contains a list of Tweets to post. Tweets should take up exactly one line.
#### Config File
The configuration file contains your Twitter API keys. Your keys can be found at https://developer.twitter.com/ and https://apps.twitter.com/. 
#### Run the Bot
The bot can be ran using
`$ python3 twitter-bot.py -t tweets.txt` 
Where `tweets.txt` is the Tweets file. See the `-h` or `--help` command line arguments for more details
