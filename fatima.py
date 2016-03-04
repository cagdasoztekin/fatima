import time
import csv
import tweepy
from tweepy import OAuthHandler
 
# credentials for fatima
consumer_key = 'wD7jjVIpW0SpYEPxuPehukOaf'
consumer_secret = 'Y4skkJua0b4CbePUWxo4H2WnslBvCZpH1Ahja7eVVnfiuxVAtw'
access_key = '4288397860-tZLJKo5N6DQsXBA8gWwNWWRPWqCfnPUgtQwtcYr'
access_secret = 'UzMPsIpuXYbJx62raTsNTrorVgyEopQ0gGnSocplSmYaR'

# authorize the application
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# both parameters set to none by default to enable the usage of the function with either of them
def find_followers(screen_name = None, twitter_id = None):

	# if only screen name is provided, find the user id here
	if (twitter_id == None):
		u = api.get_user(screen_name)
		twitter_id = u.id

	# id's of the followers are added to ids
	ids = []
	for page in tweepy.Cursor(api.followers_ids, id=twitter_id).pages():
	    ids.extend(page)
	
	return ids

def find_follows(screen_name = None, twitter_id = None):

	# if only screen name is provided, find the user id here
	if (twitter_id == None):
		u = api.get_user(screen_name)
		twitter_id = u.id

	users = []
	page_count = 0

	for user in tweepy.Cursor(api.friends, id=twitter_id).pages():
		page_count += 1
	# print 'Getting page {} for friends'.format(page_count)
		users.extend(user)
		# time.sleep(10)
	return users

# Show the rate Limits
# print api.rate_limit_status()

follows = find_follows("cagd_ass")

# for i in follows:
	# print i


followers = find_followers("cagd_ass")

# for i in followers:
	# print i

mutual_ids = list(set(follows).intersection(followers))

mutual_count = len(mutual_ids)

print mutual_count

print "Printing mutual users:"

users = api.lookup_users(user_ids=mutual_ids)
for i in ids:
    print ids.screen_name



