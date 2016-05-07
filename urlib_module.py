import urllib.request as ure
import urllib.parse as urp 
# x = ure.urlopen('https://www.google.com')

# print(x.read())

url = 'http://pythonprogramming.net'

values = {'s': 'basic', 'submit': 'search'}

data = urp.urlencode(values)
data = data.encode('utf-8')
req  = ure.Request(url,data)
resp = ure.urlopen(req)
respData = resp.read()

print(respData)


try:
	x = ure.urlopen('https://www.google.com/search?q=test')
	print(x.read())

except Exception as e:
	print(str(e))
