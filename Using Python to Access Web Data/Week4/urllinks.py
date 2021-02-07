import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter - ")
#url = "http://data.pr4e.org/romeo.txt"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

#Retrieve all of anchor tags
tags = soup("a")
for tag in tags:
    print(tag.get("href", None))
