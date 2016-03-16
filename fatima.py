from __future__ import division
import time
import csv
import tweepy

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
def find_followers(screen_name = None, twitter_id = None):
	followers = []

	for page in tweepy.Cursor(api.followers_ids, screen_name=screen_name).pages():
		followers.extend(page)
    	time.sleep(10)
    
	return followers

# @find_follows returns the list of users that are followed by the user with the given username
def find_follows(screen_name = None, twitter_id = None):
	follows = []
	for page in tweepy.Cursor(api.friends_ids, screen_name=screen_name).pages():
		follows.extend(page)
		time.sleep(10)
	return follows

# id for calkan_cs
potential_users = [1234176577]

i = 0

while(i < len(potential_users)):

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

	# print the current user's ratio and follow her if ratio is greater than 0.66
	print "User with name " + current + " has ratio: " + str(cgds_coefficient)
	if(cgds_coefficient > 0.66):
		print "Followed user " + current + " with id " + str(currentID)
		api.create_friendship(currentID)

	# add the mutual followers to the potential users list
	for k in mutual_ids:
		if k not in potential_users:
			potential_users.append(k)

	print "Potential users length: " + str(len(potential_users)) + " currently iterating index: " + str(i)

	i += 1
