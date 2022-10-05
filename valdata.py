# importing the requests library
from datetime import datetime
import requests
import csv
from prettytable import PrettyTable
import aspose.words as aw
from PIL import Image
from selenium import webdriver
from time import *
from webdriver_manager.chrome import ChromeDriverManager
import pywhatkit


matchHistoryURL="https://api.henrikdev.xyz/valorant/v3/matches/ap/Dypr/Dypr?filter=competitive"
m=requests.get(url=matchHistoryURL)



matchHistoryData=m.json()
matchID=((matchHistoryData.get("data"))[0]).get("metadata").get("matchid")
matchURL="https://api.henrikdev.xyz/valorant/v2/match/"+matchID

md=requests.get(url=matchURL)
matchData=md.json()

with open('matchResult.txt', 'w') as f:
    t=PrettyTable(["NAME","CHAR","RANK","K","D","A","HSP"])
    t.align='c'
    t.border=False
    for i in matchData.get("data").get("players").get("all_players"):

        if i.get("team")=="Blue":
            stats=[i.get("name"),i.get("character"),i.get("currenttier_patched"),(i.get("stats")).get("kills"),i.get("stats").get("deaths"),i.get("stats").get("assists"),round(i.get("stats").get("headshots")*100/(i.get("stats").get("headshots")+i.get("stats").get("legshots")+i.get("stats").get("bodyshots")))]
            t.add_row(stats)
    t.add_row(['-','-','-','-','-','-','-'])
    for i in matchData.get("data").get("players").get("all_players"):
        if i.get("team")=="Red":
            stats=[i.get("name"),i.get("character"),i.get("currenttier_patched"),(i.get("stats")).get("kills"),i.get("stats").get("deaths"),i.get("stats").get("assists"),round(i.get("stats").get("headshots")*100/(i.get("stats").get("headshots")+i.get("stats").get("legshots")+i.get("stats").get("bodyshots")))]
            t.add_row(stats)
    string = t.get_string(border=True) 
    f.write(string)
f.close()

doc = aw.Document("matchResult.txt")      
for page in range(0, doc.page_count):
    extractedPage = doc.extract_pages(page, 1)
    extractedPage.save(f"Output_{page + 1}.jpg")
im=Image.open(r"Output_1.jpg")
width, height = im.size

left = 90
top = height / 9
right = width-170
bottom =  height / 3

im1 = im.crop((left, top, right, bottom))

im1= im1.save("Output_1.jpg")

pywhatkit.sendwhats_image("E1To2eki3PzGGzDMlDNP0w","C:\Coding\Python\KAMIValStats\Output_1.jpg","Match Stats",15,True,3)