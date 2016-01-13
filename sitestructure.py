import urllib
import htmlconv

def folder(url, dirname):
	location = url + dirname
	msg = (htmlconv.h3(('>-- ' + dirname)))
	try:
		f = urllib.request.urlopen(location).getcode()
	except urllib.error.HTTPError as err:
		return (msg + htmlconv.perror(dirname + ' ' + str(err))) 

	return (msg + htmlconv.p('found at ' + location))

def file(url, filename):
	location = (url + filename)
	msg = (htmlconv.h3('>-- ' + filename + ' File'))
	try:
		f = urllib.request.urlopen(location).getcode()
	except urllib.error.HTTPError as err:
		return (msg + htmlconv.perror(filename + ' ' + str(err)))

	return (msg + htmlconv.p('found at ' + url))