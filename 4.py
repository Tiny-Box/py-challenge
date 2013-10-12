# coding:utf-8
import urllib2
import re

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'

s = urllib2.urlopen(url).read().encode('utf-8')
text = re.findall('[a-z]+', s)
l = len(text)
word = []

for i in range (0, l):
	if len(text[l-1-i]) == 1:
		word.append(text[l-1-i])
	else :
		break

word = ''.join(word)
word = word[::-1]

print word

