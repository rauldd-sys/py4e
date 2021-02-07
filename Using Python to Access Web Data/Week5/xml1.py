import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1113518.xml"
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)

counts = tree.findall('.//count')

x = 0
nums = []
for item in counts:
    x += 1
    num = item.text
    #print(num)
    nums.append(int(num))
print("Sum:", sum(nums))
print("Count:", x)
