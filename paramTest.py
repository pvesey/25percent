import htmlconv
from bs4 import BeautifulSoup as _BeautifulSoup

def tagTest(htmlText, tag, condition, value, message):
	soup = _BeautifulSoup(htmlText)

	print('IN PARAMTEST *************')
	if len(soup.findAll(tag, condition=True))>0:
		images = soup.findAll('img', height=True)
		print (htmlconv.h3(message))
		for image in images:
			print (htmlconv.imageHandler(image))
		return True
	else:
		return False
