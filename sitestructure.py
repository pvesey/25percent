import urllib
import htmlconv

def folder(url, dirname):
	location = url + dirname
	print (htmlconv.h3(('>-- ' + dirname)))
	try:
		f = urllib.request.urlopen(location).getcode()
	except urllib.error.HTTPError as err:
		return (dirname + ' ' + str(err)) 

	return('found at ' + location)

def indexfile(url):
	location = (url + 'index.html')
	print (htmlconv.h3('>-- index.html File'))
	try:
		f = urllib.request.urlopen(location).getcode()
	except urllib.error.HTTPError as err:
		return ('index.html ' + str(err)) 

	return('found at ' + url)	

def favicon(url):
	location = (url + 'favicon.ico')
	print (htmlconv.h3('>-- favicon.ico File'))
	try:
		f = urllib.request.urlopen(location).getcode()
	except urllib.error.HTTPError as err:
		return ('favicon.ico ' + str(err)) 

	return('found at ' + url)	