from twython import Twython

def newTweet(tweet):
	twitter = Twython('6wR5l7KwDSDFmb6swY1seW5MP', 'RTg9GlOPcX0YCCkodKzMzUw7z1iOdVy5fwJlD5JxbqW33XKNmL',
									'562520337-IWHslct3vqnZq9DPLHKKF7xlYrQrf5Nolatbm52T'
	, 'BmbHCJgoTTlhX99PjgRiN6uWqle6xJCepHvFDtNSfEHLy')

	twitter.update_status(status=tweet)
