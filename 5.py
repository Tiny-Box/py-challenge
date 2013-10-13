# coding:utf-8
import urllib2
import re

url = 'http://www.pythonchallenge.com/pc/def/equality.html'

s = urllib2.urlopen(url).read().encode('utf-8')
text = re.findall('[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]', s)
text = ''.join(text)
print text


