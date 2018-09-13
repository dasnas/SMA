import multiprocessing as mp

untwq = mp.Queue()
uq = mp.Queue()
#download unprocessed tweets
def dwut(q1,q2,v,l):
	while True:
		try:
			x = q1.get()
			alltweets = []
			for page in tweepy.Cursor(api.user_timeline,user_id = x,tweet_mode='extended',count=200).pages():
				alltweets.extend(page)
			q2.put(alltweets)
		except mp.Queue.Empty:
			with l:
				v.value+=1
			break


#process tweet queue
