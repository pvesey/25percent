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
from assignmentTests import assignmentTests

import types
from soupHelper import soupHelper

from sel_tests import selenium_tests

commandLine = argparse.ArgumentParser(description='Run HTML5 Scan on Website, Paul Vesey 2014')
commandLine.add_argument('URL', help='full URL, including http:// of site to scan')
commandLine.add_argument('assignment', help='50 or 25 depending on assignment')
commandLine.add_argument('--debug ', help='debug mode')


inputs = commandLine.parse_args()
url = inputs.URL
assignmentCode = inputs.assignment

#first check is the structure.
filename = url[:-1]
filename = filename.split('/')
imageName = str(filename[-1])
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

# Set to either seed25() or seed50() to setup the marking scheme

if assignmentCode == 50:
	output.seed50()
elif assignmentCode == 25:
	output.seed25()
else:
	print("Invalid option for Assignment")
	quit()

output.append(htmlconv.makeHTML('h1', 'Site Folder Structure'))
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

output.append(htmlconv.makeHTML('h1', 'Specific Site Files'))
output.append(htmlconv.p(sitestructure.file(url, 'index.html')))
output.append(htmlconv.p(sitestructure.file(url, 'favicon.ico')))


while len(urls) > 0:
	try:
		htmltext = urlopen(urls[0]).read()

	except urllib.error.HTTPError as err:
		output.append(htmlconv.makeHTML('h1', 'Link Scan Error: ', 'error'))
		output.append(htmlconv.p(urls[0] + ' ' + str(err)))
		urls.pop(0)
		continue
	except:
		output.append(htmlconv.makeHTML('h1', 'Unknown Program Error'))
		continue

	soup = BeautifulSoup(htmltext, "html.parser")
	# adding a bunch of methods to the BeautifulSoup object
	soup.countHead = types.MethodType(soupHelper.countHead, soup)
	soup.countNav = types.MethodType(soupHelper.countNav, soup)
	soup.countArticle = types.MethodType(soupHelper.countArticle, soup)
	soup.countSection = types.MethodType(soupHelper.countSection, soup)
	soup.countFooter = types.MethodType(soupHelper.countFooter, soup)
	soup.imageTitle = types.MethodType(soupHelper.imageTitle, soup)
	soup.imageAlt = types.MethodType(soupHelper.imageAlt, soup)
	soup.imageSource = types.MethodType(soupHelper.imageSource, soup)
	soup.imageWidth = types.MethodType(soupHelper.imageWidth, soup)
	soup.imageHeight = types.MethodType(soupHelper.imageHeight, soup)

	# Adding some selenium in here for a future check on Forms
	# note that the driver needs to be on your path

	output.append(htmlconv.h1(('Scanning URL ' + str(urls[0]))))

	#assert "Astronomy Ireland" in driver.title
	#if "Astronomy Ireland" in driver.title:
#	if EC.alert_is_present():
#		print('Alert Detected ' + str(urls[0]))
#		try:
			#driver.switch_to.accept()
#			driver.switch_to.alert.accept()
#			print('Alert Accepted ' + str(urls[0]))
			#driver.sendkeys('Text Sent')
			#driver.accept()
#		except Exception as e:
#			print('Alert Exception')

#	print(driver.get_cookies())
#	#print(driver.log_types)
#	print(driver.get_log('browser'))


	stest = selenium_tests(str(urls[0]))
	stest.test_contact_page()
	print("Cookies Found") if stest.test_has_cookies() else print("No Cookies")
	print("localStorage Found") if stest.test_has_localStorage() else print("No localStorage")

	stest.close()


	urls.pop(0)

	# DO NOT MESS WITH THIS FOR LOOP; IF YOU GET IT WRONG IT CAN ESCAPE YOUR URL AND
	# GO INTO THE WILD.  YOU ARE WARNED..
	for tag in soup.findAll('a', href=True):
		tag['href'] = urljoin(url, tag['href'])
		if url in tag['href'] and tag['href'] not in visited:
			urls.append(tag['href'])
			visited.append(tag['href'])

	output.append(htmlconv.makeHTML('h2', 'HTML Structure'))

	output.append(assignmentTests.testHead(soup))
	output.append(assignmentTests.testNav(soup))
	output.append(assignmentTests.testArticle(soup))
	output.append(assignmentTests.testSection(soup))
	output.append(assignmentTests.testFooter(soup))


	output.append(htmlconv.p(('Meta:' + str(len(soup.findAll('meta'))))))
	output.append(htmlconv.p(('Links:' + str(len(soup.findAll('link', href=True))))))


	numBR += len(soup.findAll('br'))
	numB += len(soup.findAll('b'))
	numI += len(soup.findAll('i'))


	output.append(htmlconv.makeHTML('h2', 'Images and Iframes'))

	output.append(assignmentTests.imageTitle(soup))
	output.append(assignmentTests.imageAlt(soup))
	output.append(assignmentTests.imageSource(soup))
	output.append(assignmentTests.imageHeight(soup))
	output.append(assignmentTests.imageWidth(soup))


	if len(soup.findAll('iframe', width=True))>0:
		images = soup.findAll('iframe', width=True)
		output.append(htmlconv.makeHTML('h3', 'IFRAME WIDTH SET ON THE FOLLOWING', 'text-danger'))
		printImages(images)

	if len(soup.findAll('iframe', height=True))>0:
		images = soup.findAll('iframe', height=True)
		output.append(htmlconv.makeHTML('h3', 'IFRAME HEIGHT SET ON THE FOLLOWING', 'text-danger'))
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

output.append(htmlconv.makeHTML('h1', 'Site Wide Results'))

output.append(htmlconv.makeHTML('h2', 'Amalgamated Results for other Items'))

output.append(htmlconv.siteCounts('br', numBR))
output.append(htmlconv.siteCounts('i', numI))
output.append(htmlconv.siteCounts('b', numB))
output.append(htmlconv.siteCounts('svg', numSVG))
output.append(htmlconv.siteCounts('canvas', numCanvas))
output.append(htmlconv.siteCounts('img', numIMG))
output.append(htmlconv.siteCounts('iframe', numIFRAME))
output.append(htmlconv.siteCounts('video', numVIDEO))
output.append(htmlconv.siteCounts('audio', numAUDIO))

output.append(htmlconv.makeHTML('h2', 'Listeners implemented in HTML (bad practice..)'))
output.append(htmlconv.siteEventCounts('onmouseover', numMouseOvers))
output.append(htmlconv.siteEventCounts('onmouseout', numMouseouts))
output.append(htmlconv.siteEventCounts('onclick', numOnclick))
output.append(htmlconv.siteEventCounts('onmousedown', numOnmouseDown))
output.append(htmlconv.siteEventCounts('onmouseup', numOnmouseUp))
output.append(htmlconv.siteEventCounts('onblur', numOnBlur))

output.append(htmlconv.makeHTML('h1', 'End of Report'))
output.writeout()
