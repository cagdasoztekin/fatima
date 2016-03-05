import time
import csv
import tweepy
from tweepy import OAuthHandler

import json
 
# credentials for fatima
consumer_key = 'pMdGMeuNDVQhmW65NCCp6X5Pz'
consumer_secret = 'fSUajJoqZj31eq5p7tyOuwkerdypRXqJ9ewzHLqrWfM68ElxOQ'
access_key = '705756931923845120-vrYJPDiDUyd6QtIkSls8XB12bZsaxra'
access_secret = 'yAssSsjVE1id9LbJNry0GBVkmGY5oXWfTtUGf6aW52rzf'

# authorize the application
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#get Location based trends
ttt =api.trends_place(3369)#ottawas location code
#print api.trends_available()
t = ttt[0]
tname = ''
for i in t[u'trends']:
	
	if 'fashion' in i[u'name'].lower():#if contains a spesific word join that trend
		tname = i[u'name']

if tname is not '':
	print tname
#api.update_status( "Hello Everyone #mbcthevoicekids")#Tweet here




