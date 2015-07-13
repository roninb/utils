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
	group = parser.add_mutually_exclusive_group()
	group.add_argument("-f", "--feed", type=int,
		help="display passed argument's amount of last tweets, up to 20")
	group.add_argument("-t", "--tweet", help="tweet from the command line")
	group.add_argument("-d", "--directmessage",
		help="directmessage a user from the command line")
#	group.add_argument("-rm", "--readmessage", type=int,
#		help="display passed argument's amount of last DMs")
	group.add_argument("-u", "--user",	help="display last 5 tweets from user")
	group.add_argument("-3", "--hashtag", help="display last 5 tweets with the same hashtag")
	opts = parser.parse_args()
	return opts

def feed(amount=5):
	if amount > 20:
		amount = 20
	elif amount < 1:
		amount = 1
	timeline = api.GetHomeTimeline(count=amount, contributor_details=False,
		include_entities=False)
	for t in timeline:
		print "%s: %s\n" % (t.GetUser().GetScreenName(), t.GetText())

def tweet(tweet):
	tweet = api.PostUpdate(tweet)
	print "You just tweeted: %s" % tweet.GetText()

def direct_message(user):
	message = raw_input("Enter your message: ")
	dm = api.PostDirectMessage(text=message, screen_name=user)
	print "Sent: %s" % dm.GetText()
	print "To: @%s" % user

#def read_message(amount):
#	messages = api.GetDirectMessages(count=amount, include_entities=False)
#	for m in messages:
#		print m.text

def read_user(user):
	timeline = api.GetUserTimeline(screen_name=user, count=5, trim_user=False)
	for t in timeline:
		print "%s: %s" % (t.GetUser().GetScreenName(), t.GetText())

def hashtag(query):
	query = "#" + query
	hashtag = api.GetSearch(term=query, count=5)
	print "Showing results for %s\n" % query
	for h in hashtag:
		print "%s: %s\n" % (h.GetUser().GetScreenName(), h.GetText())


opts = parse_args()

if opts.feed:
	feed(opts.feed)
elif opts.tweet:
	tweet(opts.tweet)
elif opts.directmessage:
	direct_message(opts.directmessage)
#elif opts.readmessage:
#	read_message(opts.readmessage)
elif opts.user:
	read_user(opts.user)
elif opts.hashtag:
	hashtag(opts.hashtag)
else:
	print "pointless"
