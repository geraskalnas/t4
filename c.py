from subprocess import call as s

with open("songs.txt") as f:
    li=f.read().split('\n')
print(li)
s(["spotdl", li])
