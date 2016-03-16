from __future__ import division
import time
from time import strftime, gmtime
import csv
import tweepy
import random
from random import randint

from tweepy import OAuthHandler

# connect to the database parameters are: [hostname], [username], [password], [databasename]
# planned to run on the server with address 178.62.59.61 (http://cgds.me)
# db = MySQLdb.connect("localhost","fatima","fatimarulez9","fatima" )
 
# twitter api credentials for fatima
consumer_key = 'pMdGMeuNDVQhmW65NCCp6X5Pz'
consumer_secret = 'fSUajJoqZj31eq5p7tyOuwkerdypRXqJ9ewzHLqrWfM68ElxOQ'
access_key = '705756931923845120-vrYJPDiDUyd6QtIkSls8XB12bZsaxra'
access_secret = 'yAssSsjVE1id9LbJNry0GBVkmGY5oXWfTtUGf6aW52rzf'

# authorize the application to use twitter apai
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# BELOVED FUNCTIONS
# @find_followers returns the list of users that follow the user with the given username
# both parameters set to none by default to enable the usage of the function with either of them
# flow_window will be a varying duration in case fatima gets timeouts (CS421 SPOOF)
def find_followers(screen_name = None, twitter_id = None, flow_window=10):
	followers = []

	for page in tweepy.Cursor(api.followers_ids, screen_name=screen_name).pages():
		followers.extend(page)
    	time.sleep(flow_window)
    
	return followers

# @find_follows returns the list of users that are followed by the user with the given username
def find_follows(screen_name = None, twitter_id = None, flow_window=10):
	follows = []
	for page in tweepy.Cursor(api.friends_ids, screen_name=screen_name).pages():
		follows.extend(page)
		time.sleep(flow_window)
	return follows

def is_active(screen_name = None, twitter_id = None, flow_window=10):
    tweet = api.user_timeline(id = twitter_id, count = 1)[0]
    
    # users are assumed to be active if they have tweeted in 2016
    return str(tweet.created_at)[:4] == '2016'

# id for calkan_cs
potential_users = [1234176577]

i = 0

# close file only to reopen with each iteration to constantly update the file
f = open("fatima.txt", "a")
f.write("\n##### RUN AT ##### " + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " #####\n")
f.close()

congestion_window = 50
flow_window = 10

while(i < len(potential_users)):
	
	# open and close the file with each iteration to see the updates of the file
	f = open("fatima.txt", "a")

	try:
		currentID = potential_users[i]
		current = api.get_user(currentID).screen_name

		followers = find_followers(screen_name=current)
		follows = find_follows(screen_name=current)

		# number of followers and followed by
		num_followers = len(followers)
		num_follows = len(follows)

		#find the people that follow AND are followed by the given user
		mutual_ids = list(set(follows).intersection(followers))
		num_mutual = len(mutual_ids)

		cgds_coefficient = num_mutual/num_follows

		# print the current user's ratio and follow her if ratio is greater than 0.66 and has been active in 2016
		print "User with name " + current + " has ratio: " + str(cgds_coefficient) + " Time: " + strftime("%Y-%m-%d %H:%M:%S", gmtime())
		f.write("User with name " + current + " has ratio: " + str(cgds_coefficient) + " Time: " + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "\n")
		if(cgds_coefficient > 0.66 and is_active(twitter_id=currentID)):
			print "Followed user " + current + " with id " + str(currentID) + " Time: " + strftime("%Y-%m-%d %H:%M:%S", gmtime())
			f.write("Followed user " + current + " with id " + str(currentID) + " Time: " + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "\n")
			api.create_friendship(currentID)

		# add the mutual followers to the potential users list
		# stop adding people to the list if list already contains enough people
		for k in mutual_ids:
			r = randint(0,9)
			# add some non-determinism, 1/10 chance to add a user to potential users list or not
			if k not in potential_users and len(potential_users) < 1000 and r == 4:
				potential_users.append(k)

		f.write("Potential users length: " + str(len(potential_users)) + " currently iterating index: " + str(i) + " Time: " + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "\n")
		print "Potential users length: " + str(len(potential_users)) + " currently iterating index: " + str(i) + " Time: " + strftime("%Y-%m-%d %H:%M:%S", gmtime())

		i += 1
		# set the increased durations to sleep to their default values
		congestion_window = 50
		flow_window = 10

		
	except Exception, e:
		print "Exception raised, sleeping."
		f.write("Exception raised. Sleeping.\n")
		time.sleep(congestion_window)
		congestion_window += 1
		flow_window += 1

	f.close()
