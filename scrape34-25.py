# This is a spider/scraper implemented in Python 3.4.  To make it work
# you will need python 3.4 and a library call Beautiful Soup installed.
# Beautiful Soup will need to be converted to Python 3 using 2to3.
# I take no responsibility for its use, or any problems it may cause you.
# Be very careful with this; it can cause problems for SysAdmins and hence
# you if you mess with it.

import sys

from urllib.parse import urlparse
from urllib.parse import urljoin
from urllib.request import urlopen
from html.parser import HTMLParser
# from html import HTML  #not under normal python distro.
import html
import paramTest
import htmlconv
import sitestructure
import argparse
from bs4 import BeautifulSoup

commandLine = argparse.ArgumentParser(description='Run HTML5 Scan on Website, Paul Vesey 2014')
commandLine.add_argument('URL', help='full URL, including http:// of site to scan')

inputs = commandLine.parse_args()
url = inputs.URL

#url = commandLine.parse_args()

# YOU WILL NEED TO CHANGE THIS TO YOUR URL

#first check is the structure.





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
		print (htmlconv.imageHandler(image))



print (htmlconv.h1('Report 40%'))
print (htmlconv.h2('Wireframes 10%'))
print (htmlconv.p('********'))
print (htmlconv.h2('Report 30%'))
print (htmlconv.p('********'))
print (htmlconv.h1('Website 60%'))
print (htmlconv.h2('Usability et. al. 15%'))
print (htmlconv.p('********'))
print (htmlconv.h2('Design Aesthetic 10%'))
print (htmlconv.p('********'))
print (htmlconv.h2('Responsive Design 15%'))
print (htmlconv.p('********'))
print (htmlconv.h2('Professional Chrome 10%'))
print (htmlconv.p('********'))
print (htmlconv.h2('HTML Validation 5%'))
print (htmlconv.p('********'))
print (htmlconv.h2('CSS Validation 5%'))
print (htmlconv.p('********'))


print (htmlconv.h1('Site Folder Structure'))
print(htmlconv.p(sitestructure.folder(url, 'style')))
print(htmlconv.p(sitestructure.folder(url, 'js')))
print(htmlconv.p(sitestructure.folder(url, 'stylesheet')))
print(htmlconv.p(sitestructure.folder(url, 'img')))
print(htmlconv.p(sitestructure.folder(url, 'font')))

print(htmlconv.p(sitestructure.indexfile(url)))












while len(urls) > 0:
	try:
		htmltext = urlopen(urls[0]).read()
	except:

		print ('Problem with Code')
		print (urls[0])

	soup = BeautifulSoup(htmltext)

	print (htmlconv.h1(('Scanning URL ' + str(urls[0]))))

	urls.pop(0)

	# DO NOT MESS WITH THIS FOR LOOP; IF YOU GET IT WRONG IT CAN ESCAPE YOUR URL AND 
	# GO INTO THE WILD.  YOU ARE WARNED..
	for tag in soup.findAll('a', href=True):
		tag['href'] = urljoin(url, tag['href'])
		if url in tag['href'] and tag['href'] not in visited:
			urls.append(tag['href'])
			visited.append(tag['href'])

	print (htmlconv.h2('HTML Structure'))

	if len(soup.findAll('head')) == 0:
		print (htmlconv.p('You should have a <code>&lthead&gt</code> section in your HTML5'))
	elif len(soup.findAll('head')) == 1:
		print (htmlconv.p('Single <code>&lthead&gt</code> section found for page; &#10004'))
	else:
		print (htmlconv.p('You should only have a single <code>&lthead&gt</code> section per page.  You have used more than one on this page'))

	print (htmlconv.p(('Meta:' + str(len(soup.findAll('meta'))))))
	print (htmlconv.p(('Links:' + str(len(soup.findAll('link', href=True))))))

	if len(soup.findAll('nav')) == 0:
		print (htmlconv.p('You should have a nav section in your HTML5'))
	elif len(soup.findAll('nav')) == 1:
		print (htmlconv.p('Single <code>&ltnav&gt</code> section found for page; &#10004'))
	else:
		print (htmlconv.p('You should only have a single <code>&ltnav&gt</code> tag per page.  You have used more than one on this page') )


	if len(soup.findAll('article')) == 0:
		print (htmlconv.p('You should have <code>&ltarticle&gt</code> tags in your HTML5'))
	elif len(soup.findAll('article')) > 0:
		print (htmlconv.p(((str(len(soup.findAll('article'))) + ' HTML5 <code>&ltarticle&gt</code> tags found'))))


	if len(soup.findAll('section')) == 0:
		print (htmlconv.p('You should have <code>&ltsection&gt</code> tags in your HTML5'))
	elif len(soup.findAll('section')) > 0 and len(soup.findAll('article')) == 0:
		print (htmlconv.p('You should not have <code>&ltsection&gt</code> without <code>&ltarticle&gt</code>'))
	else:
		print (htmlconv.p(((str(len(soup.findAll('section'))) + ' HTML5 <code>&ltsection&gt</code> tags found'))))

	if len(soup.findAll('footer')) == 0:
		print (htmlconv.p('You should have a <code>&ltfooter&gt</code> section in your HTML5'))
	elif len(soup.findAll('footer')) == 1:
		print (htmlconv.p('Single <code>&ltfooter&gt</code> section found for page; &#10004'))
	else:
		print (htmlconv.p('You should only have a single <code>&ltfooter&gt</code> section per page.  You have used more than one on this page'))


	numBR += len(soup.findAll('br'))
	numB += len(soup.findAll('b'))
	numI += len(soup.findAll('i'))


	print (htmlconv.h2('Images and Iframes'))

	if len(soup.findAll('img', title=False))>0:
		images = soup.findAll('img', title=False)
		print (htmlconv.h3('NO TITLE FOUND ON THE FOLLOWING IMAGES'))
		printImages(images)

	if len(soup.findAll('img', alt=False))>0:	
		images = soup.findAll('img', alt=False)
		print (htmlconv.h3('NO ALT FOUND ON THE FOLLOWING IMAGES'))
		printImages(images)

	if len(soup.findAll('img', src=False))>0:		
		images = soup.findAll('img', src=False)
		print (htmlconv.h3('NO SOURCE FOUND ON THE FOLLOWING IMAGES'))
		printImages(images)

	if len(soup.findAll('img', width=True))>0:
		images = soup.findAll('img', width=True)
		print (htmlconv.h3('WIDTH SET ON THE FOLLOWING IMAGES'))
		printImages(images)

	if len(soup.findAll('img', height=True))>0:	
		images = soup.findAll('img', height=True)
		print (htmlconv.h3('HEIGHT SET ON THE FOLLOWING IMAGES'))
		printImages(images)
	
	print('*****************************************')
	result = paramTest.tagTest(htmltext, 'img', 'height', True, 'HEIGHT SET ON THE FOLLOWING IMAGES')
	print(result)
	print('*****************************************')


	if len(soup.findAll('iframe', width=True))>0:
		images = soup.findAll('iframe', width=True)
		print (htmlconv.h3('IFRAME WIDTH SET ON THE FOLLOWING'))
		printImages(images)

	if len(soup.findAll('iframe', height=True))>0:	
		images = soup.findAll('iframe', height=True)
		print (htmlconv.h3('IFRAME HEIGHT SET ON THE FOLLOWING'))
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




print (htmlconv.h1('Site Wide Results'))

print (htmlconv.h2('Amalgamated Results for other Items'))

print (htmlconv.siteCounts('br', numBR))
print (htmlconv.siteCounts('i', numI))
print (htmlconv.siteCounts('b', numB))
print (htmlconv.siteCounts('svg', numSVG))
print (htmlconv.siteCounts('canvas', numCanvas))
print (htmlconv.siteCounts('img', numIMG))
print (htmlconv.siteCounts('iframe', numIFRAME))
print (htmlconv.siteCounts('video', numVIDEO))
print (htmlconv.siteCounts('audio', numAUDIO))

print (htmlconv.h2('Listeners implemented in HTML'))
print (htmlconv.siteEventCounts('onmouseover', numMouseOvers))
print (htmlconv.siteEventCounts('onmouseout', numMouseouts))
print (htmlconv.siteEventCounts('onclick', numOnclick))
print (htmlconv.siteEventCounts('onmousedown', numOnmouseDown))
print (htmlconv.siteEventCounts('onmouseup', numOnmouseUp))
print (htmlconv.siteEventCounts('onmblur', numOnBlur))


print (htmlconv.h1('End of Report'))


# need to be very careful with this.  If it hits something like facebook, it is gone!!!
