import tweepy
import os
import time
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
#twitter application credentials
consumer_key="6wR5l7KwDSDFmb6swY1seW5MP"
consumer_secret="RTg9GlOPcX0YCCkodKzMzUw7z1iOdVy5fwJlD5JxbqW33XKNmL"

#twitter user credentials
access_token="562520337-IWHslct3vqnZq9DPLHKKF7xlYrQrf5Nolatbm52T"
access_token_secret="BmbHCJgoTTlhX99PjgRiN6uWqle6xJCepHvFDtNSfEHLy"
playerList = list();

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

tweepyapi = tweepy.API(auth)

count=0

filename = "players.csv"
# f = open(filename, "w")
# Headers = "Name, Year, Position, Height, State, Stars, Offers, AAU\n"
# f.write(Headers)
my_url = 'http://www.verbalcommits.com/'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("tr")
for container in containers:
    if count != 4:
        playerContainer = container.find("td",{"class":"name"})
        
        if playerContainer is None:
            count += 1            
        else:
            if count == 1:
                playerList.append(playerContainer)
                schoolContainer = container.find("td",{"class":"school"})
                positionContainer = container.find("td",{"class":"position"})

                print("2018 " + positionContainer.text + " " + playerContainer.text + " has committed to " + schoolContainer.text )
            elif count == 2:
                playerList.append(playerContainer)
                schoolContainer = container.find("td",{"class":"school"})
                print("2019 " + positionContainer.text + " " + playerContainer.text + " has committed to " + schoolContainer.text )
            elif count == 3:
                playerList.append(playerContainer)
                schoolContainer = container.find("td",{"class":"school"})
                print("2020 " + positionContainer.text +  " " + playerContainer.text + " has committed to " + schoolContainer.text )   

    # .replace(":", "|")
    # print(musclesTargeted)
    # print(equipmentType)
    # f.write(workout + "," + mainMuscleGroup + "," + equipment + "\

# f.close()
