import html

def style():
	return("<style> .error{color: red;} </style>")


def h1(msg):
	return '<h1>' + msg + '</h1>'
def h1error(msg):
	return '<h1 class="error">' + msg + '</h1>'


def h2(msg):
	return '<h2>' + msg + '</h2>'
def h2error(msg):
	return '<h2 class="error">' + msg + '</h2>'


def h3(msg):
	return '<h3>' + msg + '</h3>'
def h3error(msg):
	return '<h3 class="error">' + msg + '</h3>'


def h4(msg):
	return '<h4>' + msg + '</h4>'

def h4error(msg):
	return '<h4 class="error">' + msg + '</h4>'


def p(msg):
	return '<p>' + msg + '</p>'

def perror(msg):
	return '<p class="error">' + msg + '</p>'

def imageHandler(image):
	return '<p><code>' + html.escape(str(image)) + '</code></p>'

def siteCounts(tagtype, count):
	return '<p>Number of <code>&lt' + tagtype + '&gt</code> tags found in site: ' + str(count) + '</p>'

def siteEventCounts(eventType, count):
	return '<p>Number of <code>' + eventType + '</code> tags found in site: ' + str(count) + '</p>'