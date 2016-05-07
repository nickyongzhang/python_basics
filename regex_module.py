'''
Identifiers:
\d any number
\D anything but a number
\s space
\S anything but a space
\w any character
\W anything but a character
. any character, except for a newline
\b the white space around words
\. a period

Modifiers: 
{1, 3} we're expecting 1-3 
+ Match 1 or more
? Mathch 0 or 1
* Mathch 0 or more
$ Mathch the end of a string
^ Mathch the beginning of a string
| either or
[] range of "variance" [A-Za-q1-5]
{x} expecting "x" amount

white Space characters:
\n newline
\s space
\t tab
\e escape
\f form feed
\r return

DONT FORGET:
. + * ? [ ] $ ^ ( ) { } | \

'''

import re

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar, is 102.
'''

ages = re.findall(r'\d{1,3}', exampleString)
names = re.findall(r'[A-Z][a-z]*',exampleString)

print(ages)
print(names)

ageDict = {}

x = 0
for eachName in names:
	ageDict[eachName] = ages[x]
	x+=1

print(ageDict)













