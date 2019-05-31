import requests

url = "http://www.europeanhitradio.lt/top/ehr-top-40/"
response = requests.get(url)
print(response)
with open("resp.txt", "w") as f:
    f.write(response.text)

#write page html source code to file
