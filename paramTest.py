from bs4 import BeautifulSoup as _BeautifulSoup

def tagTest(htmlText, tag, condition, value, message):
	soup = _BeautifulSoup(htmlText)
	
	if len(soup.findAll(tag, condition=value))>0:
		images = soup.findAll('img', height=True)
		print (htmlconv.toH3(message))
		printImages(images)
		return True
	else:
		return False
