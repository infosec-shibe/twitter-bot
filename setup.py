from distutils.core import setup

setup(
	name="simple-twitter-bot",
	version="0.0.1",
	author="InfoSec Shibe",
	author_email="infosec_shibe@protonmail.com",
	packages=["simple-twitter-bot"],
	scripts=[],
	url="https://github.com/infosec_shibe/twitter-bot",
	license="LICENSE.txt",
	description="A simple Twitter bot that posts randomly from a list of Tweets on a user",
	long_description=open('README.md').read(),
	install_requires=[
		"configparser >= 3.0.0",
		"tweepy >= 0.0.1",
	],
)

