# urllib and urllib2 are both Python modules that do URL request 
# related stuff but offer different functionalities. Their two most 
# significant differences are listed below:

# urllib2 can accept a Request object to set the headers for a URL 
# request, urllib accepts only a URL. That means, you cannot 
# masquerade your User Agent string etc.

# urllib provides the urlencode method which is used for the 
# generation of GET query strings, urllib2 doesn't have such a
# function. This is one of the reasons why urllib is often used along
#  with urllib2.
import urllib2
import urllib

# both urllib and urllib2 can be used to open a url
x = urllib.urlopen('https://www.google.com')

print(x.read())

# use a request to vist a webpage
url = 'http://pythonprogramming.net'

values = {'s': 'basic', 'submit': 'search'}

data = urllib.urlencode(values)
data = data.encode('utf-8')
request  = urllib2.Request(url,data)
response = urllib2.urlopen(request)
respData = response.read()

print(respData)

# Visting some websites from python will be declined without using request
try:
	x = urllib2.urlopen('https://www.google.com/search?q=test')
	print(x.read())

except Exception as e:
	print(str(e))
