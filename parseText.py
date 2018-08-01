import re, string
from newTweet import newTweet
#coding: utf8
tweet = ''


def parseTweet(tweet):
	tweetList = tweet.split()
	if checkIfOffer(tweetList) == True:
		tweetList = tweet.split()
		playerYear = findYear(tweetList)
		playerHS = findHS(tweet)
		playerPosition = findPosition(tweet)
		playerName = findName(tweetList)
		playerOffer = findOffer(tweetList)
		createdTweet = playerOffer + " has offered " + playerYear + " (" + playerPosition + ") " + playerName
		print(createdTweet)
		newTweet(createdTweet)
	else:
		print("This is not an offer Tweet")
##    
##    
##    
##    nameList = str (playerPositionList)
##    playername = nameList.split("has")
##    print(playername[0])
##    tweetFindOffer = tweet.split("from ")
##    playerOfferString = str (tweetFindOffer[1])
##    newString = playerOfferString.replace(".","")
##    8("School: " + newString)
##    myPlayer = Player(playerYear, playerSchool, playerPosition, player)
##
def checkIfOffer(tweet):
	global index
	index = 0
	for x in tweet:
		index+= 1
		word = str (x)
		length = len(word)
		if word == "offer":
			return True
	return False
			

def findYear(tweet):
	playerYear = tweet[0]
#	print("Year: " + playerYear)
	return playerYear

def findHS(tweet):
	tweetFindSchool = tweet.split(")")
	playerSchoolString = str (tweetFindSchool[0])
	playerSchool = playerSchoolString[5:]
#	print("HS: " + playerSchool +")")
	return playerSchool

def findPosition(tweet):
	playerPositionList = tweet.split(")")
	playerPositionString = str (playerPositionList[1])
	playerPositionText = playerPositionString.split()
	playerPosition = playerPositionText[0]
#	print("Position: " + playerPosition)
	return playerPosition

def findOffer(tweet):
	global schoolList
	schoolList = []
	global beginOfSchool
	global endOfSchool
	global index
	index2 = 0
	index = 0
	beginOfSchool = 0
	endOfSchool = 0
	for x in tweet:
		index+= 1
		word = str (x)
		length = len(word)
		if word == "from":
			beginOfSchool = index	
		if beginOfSchool > 1:
			if word[length-1] == ".":
				endOfSchool = index + 1
				endOfSchool - 1
	for x in tweet:
		index2+= 1
		if beginOfSchool < index2 < endOfSchool:
			word = str (x)
			schoolList.append([word])
	Str1 =''.join([str(i) for i in schoolList])
	schoolName = Str1.replace("[", "")
	schoolName = schoolName.replace("]", " ")
	schoolName = schoolName.replace("'", "")
	x = len(schoolName) - 2
#	print("Offer: " + schoolName[0:x])
	return schoolName[0:x]


def findName(tweet):
	global nameList
	nameList = []
	global beginOfName
	global endOfName
	global index
	index = 0
	index2 = 0
	beginOfName = 0
	endOfName = 0
	for x in tweet:
		index+= 1
		word = str (x)
		if word[0] == "(":
			beginOfName = index	+ 1		
		if word == "has":
			endOfName = index
			endOfName - 1
	for x in tweet:
		index2+= 1
		if beginOfName < index2 < endOfName:
			word = str (x)
			nameList.append([word])
	Str1 =''.join([str(i) for i in nameList])
	playerName = Str1.replace("[", "")
	playerName = playerName.replace("]", " ")
	playerName = playerName.replace("'", "")
#	print("Name: " + playerName)
	return playerName
parseTweet(tweet)

# class Player:
#      def __init__(self, year, hs, position, name, offer):
#          self.year = year
#          self.hs = hs
#          self.position = position
#          self.name = name
#          self.offer = offer
#     