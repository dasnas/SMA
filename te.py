import tweepy
import numpy as np
import time
import json
from sys import argv

start = 0.0

pathname = argv[1]
f = open(pathname,'r')

CK = []
CS = []
AT = []
AS = []

def Exit(x):
	print (time.time() - start)
	x.close()
	

def fetchUserTweets(x):
	ft = open(str(x)+'tweets.json','w',encoding='utf-8')
	try:
		#json.dump([status._json for status in tweepy.Cursor(api.user_timeline,user_id = x,tweet_mode='extended').items()],ft,indent =4)
		
		alltweets = []
		for page in tweepy.Cursor(api.user_timeline,user_id = str(x),tweet_mode='extended',count=200,trim_user=True).pages(2):
			alltweets.extend([status._json for status in page])
		json.dump(alltweets,ft,indent = 4)
		ft.close()
		
    	# process status here
    	#process_status(status)
		'''
		alltweets = []
		new_tweets = api.user_timeline(user_id = x,count=200,tweet_mode = 'extended')
		if len(new_tweets) != 0:
			alltweets.extend(new_tweets)
			oldest = alltweets[-1].id - 1
			while True:
				#print ("getting tweets for  before %s" % (oldest))
				
				
					
					#all subsiquent requests use the max_id param to prevent duplicates
				new_tweets = api.user_timeline(user_id = x,count=200,max_id=oldest,tweet_mode= 'extended')
				if len(new_tweets) == 0:
						break
					#save most recent tweets
				alltweets.extend(new_tweets)
					
					#update the id of the oldest tweet less one
				oldest = alltweets[-1].id - 1
			#save alltweets in suitable format
		json.dump([status._json for status in alltweets],ft,indent = 4)
			
		ft.close()
		'''
	except tweepy.RateLimitError as Rl:
		print (Rl.reason)
		Exit(ft)
	except tweepy.error.TweepError as Ue:
		print (Ue.reason)
		Exit(ft)

		


access_data = f.readline()
while access_data != '':
	temp = access_data[:-1].split(';')
	#print temp
	CK.append(temp[0])
	CS.append(temp[1])
	AT.append(temp[2])
	AS.append(temp[3])
	access_data = f.readline()

auth = tweepy.OAuthHandler(CK[0], CS[0])
auth.set_access_token(AT[0], AS[0])

api = tweepy.API(auth)
f.close()
'''
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
'''    
#users = np.genfromtxt('/home/sanket/Desktop/Sanket/news_followers/htTweets.txt', delimiter=';', dtype=str)
with open(argv[2],'rb') as fp:
	users = [key for key  in json.load(fp)]
iterusers = iter(users)
next(iterusers)
start = time.time()
I = 0
for user in iterusers:
	fetchUserTweets(user)
	I+=1
	if I == 1:
		print (time.time() - start)
		break
	print (user, "done")



