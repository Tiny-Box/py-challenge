# coding:utf-8
import urllib2
import re

url = 'http://www.pythonchallenge.com/pc/def/equality.html'

s = urllib2.urlopen(url).read().encode('utf-8')
text = re.findall('[A-Z]{3}([a-z])[A-Z]{3}', s)
text = ''.join(text)
print text

def translate(s):
	b = []

	for i in range (0, len(s)):
		a = s[i]
		if ord(a) >= 97 and ord(a) <= 122:
			if ord(a) >= 121:
				a = chr(2 + ord(a) - 28)
			a = chr(2 + ord(a))
		
		b.append(a)

	b = ''.join(b)
	return b

print translate(text)
