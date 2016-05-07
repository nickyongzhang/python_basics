import urllib.request, urllib.error, urllib.parse

try:
	x = urlib2.urlopen('http://pythonprogramming.net')

	print(x)
except Exception as e:
	print((str(e)))