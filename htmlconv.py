import html


def toH1(msg):
	return '<h1>' + msg + '</h1>'

def toH2(msg):
	return '<h2>' + msg + '</h2>'

def toH3(msg):
	return '<h3>' + msg + '</h3>'

def toH4(msg):
	return '<h4>' + msg + '</h4>'

def toP(msg):
	return '<p>' + msg + '</p>'

def imageHandler(image):
	return '<p><code>' + html.escape(str(image)) + '</code></p>'

def siteCounts(tagtype, count):
	return '<p>Number of <code>&lt' + tagtype + '&gt</code> tags found in site: ' + str(count) + '</p>'

def siteEventCounts(eventType, count):
	return '<p>Number of <code>' + eventType + '</code> tags found in site: ' + str(count) + '</p>'