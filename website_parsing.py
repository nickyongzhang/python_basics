import urllib
import urllib2
import re, time

url = 'http://pythonprogramming.net'
values = {'s':'basics',
          'submit': 'search'}
data = urllib.urlencode(values)
data = data.encode('utf-8')
req  = urllib2.Request(url,data)
resp = urllib2.urlopen(req)
respData = resp.read()

# print(respData)

# use (.&?) to match all the content
paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))

for eachP in paragraphs:
	print(eachP)

# this is for user to see the output when excuting the executable
time.sleep(15)