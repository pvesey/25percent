import html

def makeHTML(tag, msg, style = ''):
	if style != '':
		style = 'class="' + style + '"'
		return('<' + tag + ' ' + style +  '>' + msg + '</' + tag + '>')
	else:
		return('<' + tag + '>' + msg + '</' + tag + '>')


def style():
	return('<style> .error{color: red;} .success{color: green;}</style><link href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">')


def h1(msg):
	return '<h1>' + msg + '</h1>'
def h1error(msg):
	return '<h1 class="error">' + msg + '</h1>'
def h1success(msg):
	return '<h1 class="success">' + msg + '</h1>'

def h2(msg):
	return '<h2>' + msg + '</h2>'
def h2error(msg):
	return '<h2 class="error">' + msg + '</h2>'
def h2success(msg):
	return '<h2 class="success">' + msg + '</h2>'

def h3(msg):
	return '<h3>' + msg + '</h3>'
def h3error(msg):
	return '<h3 class="error">' + msg + '</h3>'
def h3success(msg):
	return '<h3 class="success">' + msg + '</h3>'

def h4(msg):
	return '<h4>' + msg + '</h4>'
def h4error(msg):
	return '<h4 class="error">' + msg + '</h4>'
def h4success(msg):
	return '<h4 class="success">' + msg + '</h4>'

def p(msg):
	return '<p>' + msg + '</p>'
def perror(msg):
	return '<p class="error">' + msg + '</p>'
def psuccess(msg):
	return '<p class="success">' + msg + '</p>'

def imageHandler(image):
	return '<p><code>' + html.escape(str(image)) + '</code></p>'

def siteCounts(tagtype, count):
	return '<p>Number of <code>&lt' + tagtype + '&gt</code> tags found in site: ' + str(count) + '</p>'

def siteEventCounts(eventType, count):
	return '<p>Number of <code>' + eventType + '</code> tags found in site: ' + str(count) + '</p>'
