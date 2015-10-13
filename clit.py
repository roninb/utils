# Written by Malik Butler on July 6th, 2015
# This is a command line twitter client for personal use.
# I will start by using OAuth and then, if possible, allow a user to input
# their credentials

# at first, it will only print to STDOUT the text of your last 5 tweets
# I plan on adding support for a tweet-by-tweet display mode that allows you to
# interact (retweet and favorite to start, with possible support for replying,
# checking who else has retweeted and favorited and direct messaging the user of
# the tweet)

import argparse
import twitter

# establishes connection to twitter api
api = twitter.Api(consumer_key='<ROLL>',
	consumer_secret='<YOUR>',
	access_token_key='<OWN>',
	access_token_secret='<KEYS>')

# parses commandline arguments and delivers help messages
def parse_args():
	parser = argparse.ArgumentParser()
	group = parser.add_mutually_exclusive_group()
	group.add_argument("-f", "--feed", type=int,
		help="display passed argument's amount of last tweets, up to 20")
	group.add_argument("-t", "--tweet", help="tweet from the command line")
	group.add_argument("-d", "--directmessage",
		help="directmessage a user from the command line")
	group.add_argument("-u", "--user",	help="display last 5 tweets from user")
	group.add_argument("-3", "--hashtag", help="display last 5 tweets with the same hashtag")
	opts = parser.parse_args()
	return opts

# grabs a certain amount of tweets from feed
def feed(amount=5):
	if amount > 20:
		amount = 20
	elif amount < 1:
		amount = 1
	timeline = api.GetHomeTimeline(count=amount, contributor_details=False,
		include_entities=False)
	for t in timeline:
		print "%s: %s\n" % (t.GetUser().GetScreenName().encode("utf-8"), t.GetText().encode("utf-8"))

# posts a tweet
def tweet(tweet):
	tweet = api.PostUpdate(tweet)
	print "You just tweeted: %s" % tweet.GetText().encode("utf-8")

# direct messages a user
def direct_message(user):
	message = raw_input("Enter your message: ")
	dm = api.PostDirectMessage(text=message, screen_name=user)
	print "Sent: %s" % dm.GetText().encode("utf-8")
	print "To: @%s" % user

# grabs a user's last 5 tweets
def read_user(user):
	timeline = api.GetUserTimeline(screen_name=user, count=5, trim_user=False)
	for t in timeline:
		print "%s: %s" % (t.GetUser().GetScreenName().encode("utf-8"), t.GetText().encode("utf-8"))

# grabs a hashtags last 5 usages
def hashtag(query):
	query = "#" + query
	hashtag = api.GetSearch(term=query, count=5)
	print "Showing results for %s\n" % query
	for h in hashtag:
		print "%s: %s\n" % (h.GetUser().GetScreenName().encode("utf-8"), h.GetText().encode("utf-8"))


opts = parse_args()

if opts.feed:
	feed(opts.feed)
elif opts.tweet:
	tweet(opts.tweet)
elif opts.directmessage:
	direct_message(opts.directmessage)
elif opts.user:
	read_user(opts.user)
elif opts.hashtag:
	hashtag(opts.hashtag)
else:
	print "You didn't enter an argument!!"
