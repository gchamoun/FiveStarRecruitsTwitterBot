from twython import Twython, TwythonError
import schedule
import time
import datetime
from parseText import parseTweet

latestTweet = 0

twitter = Twython('6wR5l7KwDSDFmb6swY1seW5MP', 'RTg9GlOPcX0YCCkodKzMzUw7z1iOdVy5fwJlD5JxbqW33XKNmL',
									'562520337-IWHslct3vqnZq9DPLHKKF7xlYrQrf5Nolatbm52T'
, 'BmbHCJgoTTlhX99PjgRiN6uWqle6xJCepHvFDtNSfEHLy')

def job():	
						try:
								user_timeline = twitter.get_user_timeline(screen_name='VerbalCommits', count=1)
						except TwythonError as e:
							 print (e)

						for tweets in user_timeline:
								tweet = int (tweets['id'])
								if checkIfNew(tweet):
										print("True")
										tweetText = tweets['text'].encode('utf-8')
										newTweet(tweetText)
								else:
										print("False")
								 
										
def checkIfNew(id):
		global latestTweet
		print(id)
		#If new tweet
		if id != latestTweet:
				latestTweet = id 
				return True
		#No new
		else:
				print("No new tweet")
				return False
				
def newTweet(tweet):
	from twilio.rest import Client
	import random
	import json
	import datetime
	import codecs
	from io import open
	account_sid = 'AC9ac3d4a208aed65de2c6a94503b2f29b'
	auth_token = '9b24e7f673c9c1cc22af43cd9820057b'
	# client = Client(account_sid, auth_token)
	# message = client.messages.create(
	# 			body=tweet,
	# 																from_='+18645394733',
	# 																to='2054758001'
	# 														)
	print("Newest Tweet:" + tweet.decode('utf-8'))

	parseTweet(tweet.decode('utf-8'))
	# print("text sent")
					

print (datetime.datetime.utcnow())    
job()
schedule.every(60).seconds.do(job)
while 1:
    schedule.run_pending()
    time.sleep(5)
