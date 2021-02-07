import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def readweb(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup("a")
    return tags

url = input("Enter: ")
count = int(input("Enter count: "))
pos = int(input("Enter position: "))
tags = readweb(url)

pageurl = list()
print("Retrieving:", url)
while count>0:
    pageurl.clear()
    for tag in tags:
        url2 = tag.get("href", None)
        if url2 == None: continue
        pageurl.append(url2)
    print("Retrieving:", pageurl[pos-1])
    tags = readweb(pageurl[pos-1])
    if count>0:
        count = count-1
        continue
