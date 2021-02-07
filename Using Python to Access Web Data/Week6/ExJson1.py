import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

x = 0
tsum = list()

url = "http://py4e-data.dr-chuck.net/comments_1113519.json"
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
info = json.loads(data)
for i in info["comments"]:
    tsum.append(int(i["count"]))
    x += 1

print("Sum:", sum(tsum))
print("Count:", x)
