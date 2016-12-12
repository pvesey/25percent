# This is a spider/scraper implemented in Python 3.4.  To make it work
# you will need python 3.4 and a library call Beautiful Soup installed.
# Beautiful Soup will need to be converted to Python 3 using 2to3.
# I take no responsibility for its use, or any problems it may cause you.
# Be very careful with this; it can cause problems for SysAdmins and hence
# you if you mess with it.

import sys
import urllib
from urllib.parse import urlparse
from urllib.parse import urljoin
from urllib.request import urlopen
from html.parser import HTMLParser
# from html import HTML  #not under normal python distro.
import html
import htmlconv
import sitestructure
from Ofile import Ofile
import argparse
from bs4 import BeautifulSoup

commandLine = argparse.ArgumentParser(description='Run HTML5 Scan on Website, Paul Vesey 2014')
commandLine.add_argument('URL', help='full URL, including http:// of site to scan')

inputs = commandLine.parse_args()
url = inputs.URL

#url = commandLine.parse_args()

#first check is the structure.
filename = url[:-1]
filename = filename.split('/')
filename = str(filename[-1]) + '.html'

output = Ofile(filename, '')


urls = [url] 
visited = [url]
svgs = []
canvas = []
head = []
article = []
footer = []
nav = []
meta = []
links = []

numSVG = 0
numCanvas = 0
numBR = 0
numI = 0
numB = 0
numIMG = 0
numIFRAME = 0
numVIDEO = 0
numAUDIO =0
numMouseOvers = 0
numMouseouts =0
numOnclick = 0
numOnmouseDown =0
numOnmouseUp =0
numOnBlur = 0


def printImages(images):
	for image in images:
		output.append(htmlconv.imageHandler(image))

output.append(htmlconv.style())

output.seed25()


output.append(htmlconv.h1('Site Folder Structure'))
output.append(sitestructure.folder(url, 'style'))
output.append(sitestructure.folder(url, 'stylesheet'))
output.append(sitestructure.folder(url, 'css'))
output.append(sitestructure.folder(url, 'js'))
output.append(sitestructure.folder(url, 'img'))
output.append(sitestructure.folder(url, 'images'))
output.append(sitestructure.folder(url, 'pics'))

output.append(sitestructure.folder(url, 'font'))
output.append(sitestructure.folder(url, 'fonts'))
output.append(sitestructure.folder(url, 'audio'))
output.append(sitestructure.folder(url, 'video'))

output.append(htmlconv.h1('Specific Site Files'))
output.append(htmlconv.p(sitestructure.file(url, 'index.html')))
output.append(htmlconv.p(sitestructure.file(url, 'favicon.ico')))


while len(urls) > 0:
	try:
		htmltext = urlopen(urls[0]).read()
	except urllib.error.HTTPError as err:
		output.append(htmlconv.h1error('Link Scan Error: '))
		output.append(htmlconv.p(urls[0] + ' ' + str(err)))
		urls.pop(0)
		continue
	except:
		output.append(htmlconv.h1('Unknown Program Error'))
		continue

	soup = BeautifulSoup(htmltext, "html.parser")

	output.append(htmlconv.h1(('Scanning URL ' + str(urls[0]))))

	urls.pop(0)

	# DO NOT MESS WITH THIS FOR LOOP; IF YOU GET IT WRONG IT CAN ESCAPE YOUR URL AND 
	# GO INTO THE WILD.  YOU ARE WARNED..
	for tag in soup.findAll('a', href=True):
		tag['href'] = urljoin(url, tag['href'])
		if url in tag['href'] and tag['href'] not in visited:
			urls.append(tag['href'])
			visited.append(tag['href'])

	output.append(htmlconv.h2('HTML Structure'))

	if len(soup.findAll('head')) == 0:
		output.append(htmlconv.perror('You should have a <code>&lthead&gt</code> section in your HTML5'))
	elif len(soup.findAll('head')) == 1:
		output.append(htmlconv.psuccess('Single <code>&lthead&gt</code> section found for page; &#10004'))
	else:
		output.append(htmlconv.perror('You should only have a single <code>&lthead&gt</code> section per page.  You have used more than one on this page'))

	output.append(htmlconv.p(('Meta:' + str(len(soup.findAll('meta'))))))
	output.append(htmlconv.p(('Links:' + str(len(soup.findAll('link', href=True))))))

	if len(soup.findAll('nav')) == 0:
		output.append(htmlconv.perror('You should have a nav section in your HTML5'))
	elif len(soup.findAll('nav')) == 1:
		output.append(htmlconv.psuccess('Single <code>&ltnav&gt</code> section found for page; &#10004'))
	else:
		output.append(htmlconv.perror('You should only have a single <code>&ltnav&gt</code> tag per page.  You have used more than one on this page') )


	if len(soup.findAll('article')) == 0:
		output.append(htmlconv.perror('You should have <code>&ltarticle&gt</code> tags in your HTML5'))
	elif len(soup.findAll('article')) > 0:
		output.append(htmlconv.p(((str(len(soup.findAll('article'))) + ' HTML5 <code>&ltarticle&gt</code> tags found'))))


	if len(soup.findAll('section')) == 0:
		output.append(htmlconv.perror('You should have <code>&ltsection&gt</code> tags in your HTML5'))
	elif len(soup.findAll('section')) > 0 and len(soup.findAll('article')) == 0:
		output.append(htmlconv.perror('You should not have <code>&ltsection&gt</code> without <code>&ltarticle&gt</code>'))
	else:
		output.append(htmlconv.p(((str(len(soup.findAll('section'))) + ' HTML5 <code>&ltsection&gt</code> tags found'))))

	if len(soup.findAll('footer')) == 0:
		output.append(htmlconv.perror('You should have a <code>&ltfooter&gt</code> section in your HTML5'))
	elif len(soup.findAll('footer')) == 1:
		output.append(htmlconv.psuccess('Single <code>&ltfooter&gt</code> section found for page; &#10004'))
	else:
		output.append(htmlconv.perror('You should only have a single <code>&ltfooter&gt</code> section per page.  You have used more than one on this page'))


	numBR += len(soup.findAll('br'))
	numB += len(soup.findAll('b'))
	numI += len(soup.findAll('i'))


	output.append(htmlconv.h2('Images and Iframes'))

	if len(soup.findAll('img', title=False))>0:
		images = soup.findAll('img', title=False)
		output.append(htmlconv.h3error('NO TITLE FOUND ON THE FOLLOWING IMAGES'))
		printImages(images)

	if len(soup.findAll('img', alt=False))>0:	
		images = soup.findAll('img', alt=False)
		output.append(htmlconv.h3error('NO ALT FOUND ON THE FOLLOWING IMAGES'))
		printImages(images)

	if len(soup.findAll('img', src=False))>0:		
		images = soup.findAll('img', src=False)
		output.append(htmlconv.h3error('NO SOURCE FOUND ON THE FOLLOWING IMAGES'))
		printImages(images)

	if len(soup.findAll('img', width=True))>0:
		images = soup.findAll('img', width=True)
		output.append(htmlconv.h3error('WIDTH SET ON THE FOLLOWING IMAGES'))
		printImages(images)

	if len(soup.findAll('img', height=True))>0:	
		images = soup.findAll('img', height=True)
		output.append(htmlconv.h3error('HEIGHT SET ON THE FOLLOWING IMAGES'))
		printImages(images)

	if len(soup.findAll('iframe', width=True))>0:
		images = soup.findAll('iframe', width=True)
		output.append(htmlconv.h3error('IFRAME WIDTH SET ON THE FOLLOWING'))
		printImages(images)

	if len(soup.findAll('iframe', height=True))>0:	
		images = soup.findAll('iframe', height=True)
		output.append(htmlconv.h3error('IFRAME HEIGHT SET ON THE FOLLOWING'))
		printImages(images)

	numSVG += len(soup.findAll('svg'))
	numCanvas += len(soup.findAll('canvas'))
	numIMG += len(soup.findAll('img'))
	numVIDEO += len(soup.findAll('video'))
	numIFRAME += len(soup.findAll('iframe'))
	numAUDIO += len(soup.findAll('audio'))
	numMouseOvers += len(soup.findAll(onmouseover=True))
	numMouseouts += len(soup.findAll(onmouseout=True))
	numOnclick += len(soup.findAll(onclick=True))
	numOnmouseDown += len(soup.findAll(onmousedown=True))
	numOnmouseUp += len(soup.findAll(onmouseup=True))
	numOnBlur += len(soup.findAll(onblur=True))

output.append(htmlconv.h1('Site Wide Results'))

output.append(htmlconv.h2('Amalgamated Results for other Items'))

output.append(htmlconv.siteCounts('br', numBR))
output.append(htmlconv.siteCounts('i', numI))
output.append(htmlconv.siteCounts('b', numB))
output.append(htmlconv.siteCounts('svg', numSVG))
output.append(htmlconv.siteCounts('canvas', numCanvas))
output.append(htmlconv.siteCounts('img', numIMG))
output.append(htmlconv.siteCounts('iframe', numIFRAME))
output.append(htmlconv.siteCounts('video', numVIDEO))
output.append(htmlconv.siteCounts('audio', numAUDIO))

output.append(htmlconv.h2('Listeners implemented in HTML'))
output.append(htmlconv.siteEventCounts('onmouseover', numMouseOvers))
output.append(htmlconv.siteEventCounts('onmouseout', numMouseouts))
output.append(htmlconv.siteEventCounts('onclick', numOnclick))
output.append(htmlconv.siteEventCounts('onmousedown', numOnmouseDown))
output.append(htmlconv.siteEventCounts('onmouseup', numOnmouseUp))
output.append(htmlconv.siteEventCounts('onblur', numOnBlur))


output.append(htmlconv.h1('End of Report'))


output.writeout()


# need to be very careful with this.  If it hits something like facebook, it is gone!!!
