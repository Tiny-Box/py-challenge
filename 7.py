import pickle
import urllib

urllib.urlretrieve('http://www.pythonchallenge.com/pc/def/banner.p', 'banner.p')
reader = pickle.load(open('banner.p', 'rb'))
for i in reader:
	line = ""
	for j in i:
		line += j[0]*j[1]
	print line
