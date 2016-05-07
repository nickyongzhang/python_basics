import urllib.request as ure
import urllib.parse as urp
import re

url = 'http://pythonprogramming.net'
values = {'s':'basics',
          'submit': 'search'}
data = urp.urlencode(values)
data = data.encode('utf-8')
req  = ure.Request(url,data)
resp = ure.urlopen(req)
respData = resp.read()

print(respData)

paragraphs = re.findall(r'<p>(.&?)</p>', str(respData))

for eachP in paragraphs:
	print(eachP)

input('press any key to exist!')