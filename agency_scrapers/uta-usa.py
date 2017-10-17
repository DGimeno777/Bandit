from lxml import html
import requests

dbFile = open("C:\\Users\\Danny\\Desktop\\Computer Science\\Bandit\\agency_scrapers\\output\\uta-usa-output.txt", "w")


page = requests.get('http://music.utatouring.com/usa-roster/', headers={'User-Agent':'test'})
tree = html.fromstring(page.content)

#Creates a list of artists:
artists = tree.xpath('//div[@class="ut-one-third"]/div/a/text()')
artistsScrubbed = "";
for artist in artists:
    if len(artist) > 1:
        dbFile.write(artist+"\n");

dbFile.close()