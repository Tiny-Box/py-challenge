import pickle
import urllib

urllib.urlretrieve('http://www.pythonchallenge.com/pc/def/banner.p', 'banner.p')
reader = pickle.load(open('banner.p', 'rb'))
print reader
