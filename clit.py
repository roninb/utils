# Written by Malik Butler on July 6th, 2015
# This is a command line twitter client for personal use.
# I will start by using OAuth and then, if possible, allow a user to input
# their credentials

# at first, it will only print to STDOUT the text of your last 5 tweets
# I plan on adding support to ask for a specific amount of tweets, a 
# tweet-by-tweet display mode that allows you to interact (retweet and
# favorite to start, with possible support for replying, checking who
# else has retweeted and favorited and direct messaging the user of the
# tweet) with tweets on your timeline, a way to check and send direct 
# messages.

import argparse
import twitter

api = twitter.Api(consumer_key='6Dy73JL5yIgC6oAfOwjQpHQYu',
	consumer_secret='7sbxr51R36ZZtpX9Idx7NwCNdgtzFlidk7fvDEWYwLjqRqZMhv',
	access_token_key='189396089-QhunfcJUhrMAyVxv2I7J9a2MmBERIrxDP3oZ0OH9',
	access_token_secret='kp6kmJ7fQiF7ZLkJH0qWgIuOsADdBu6g3HoOxUQSh6L8A')

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("-s", "--status", type=int, 
		help="display passed argument's amount of last tweets, up to 20")
	parser.add_argument("-t", "--tweet", help="tweet from the command line")
	opts = parser.parse_args()
	return opts


""" to get the home timeline for a given user (I know my own username) """
#statuses = api.GetUserTimeline(screen_name="_malikbutler")
#print [s.text for s in statuses]

""" prints a bunch of junk """
#print api.VerifyCredentials()

""" to post a status update """
# status = api.PostUpdate(raw_input("Status >> "))
# print status.text

def status(amount):
	timeline = api.GetHomeTimeline(count=amount, trim_user=True, 
		exclude_replies=True, contributor_details=False, 
		include_entities=False)
	#timeline.split('u[').split('],')

	for t in timeline:
		print t.text

def tweet(tweet):
	tweet = api.PostUpdate(tweet)
	print tweet.text

opts = parse_args()

if opts.status:
	status(opts.status)
elif opts.tweet:
	tweet(opts.tweet)
else:
	print "pointless"