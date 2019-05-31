from bs4 import BeautifulSoup

#import re

with open("resp.txt", "r") as f:
    resp=f.read()
soup = BeautifulSoup(resp, "html.parser")#find songs places
r=soup.findAll("li")

r_songs=[]

for a in range(len(r)): #retrieve songs
    for b in r[a].findAll("div"):
        if(b["class"][0]=='song'):
            #print(b.text)
            r_songs.append(b.text)

#norm = re.compile('\n([A-Za-z0-9]+[\., ]{0,3})+\-')
#norm = re.compile('(([A-Za-z0-9]+)[^A-Za-z0-9]+)+')

songs=[]

for i in range(len(r_songs)):#normalize song names
    ll=""
    song=""
    for l in r_songs[i]:
        #print("DEBUG: l =", l, "ll", ll)
        if(l!='\n' and(l!=' ' or ll!=' ')):
            song+=l
        ll=l
    if(len(song)>4): songs.append(song)

with open("songs.txt", "w") as f:#display and output to file
    for song in songs:
        f.write(song+'\n')
        print(song)
