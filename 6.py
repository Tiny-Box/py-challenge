import re
import urllib

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
num = '12345'
num2 = '16044'
num3 = '82682'
url2 = url + '?nothing=' + num

for i in range (400):
	html = urllib.urlopen(url2).read()
	numlist = re.findall('[0-9]+', html)
	num = numlist[0]
	url2 = url + '?nothing=' + num
	print html
