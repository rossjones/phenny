"""
            headlines.py - Phenny Headlines Module
            Copyright 2011, Nicola Hughes
            Licensed under the Eiffel Forum License 2.
            
"""

import urlparse
import urllib2
import re

def hl(phenny, input):
	""".hl Returns the headlines from a news source for a given number of headlines """
	QUERY = input.group(2).split(':')[0]
	Number = int(input.group(2).split(':')[1].strip(' '))
	news = QUERY.strip(' ').lower()

	if news == 'bbc':
		site = 'http://www.bbc.co.uk/news/'
		html = urllib2.urlopen(site).read()
		everyheadline = re.findall('<h2[^>]*?>[\s]*?<a class="story".*?>.*?</h2>', html, re.DOTALL)
		for headline in everyheadline[:Number]:
			headlines = re.search('<a[^>]*?href="(?P<link>[^"]*?)".*>(?P<story>.+?)(<img.*/>.*?)?</a>', headline, re.DOTALL)
			link = urlparse.urljoin(site, headlines.group('link'))
			story = headlines.group('story').replace("&#039;", "'")
			topstories = story.strip() + ' -> ' + link
			phenny.say(topstories)

	elif news == 'guardian':
		site = 'http://www.guardian.co.uk/'
		html = urllib2.urlopen(site).read()
		indiv = re.search("""<div\s*class="\s*component b5 nf-main\s*">.*?<div\s*id="keycontent"\s*class="\s*component nf-main\s*">""", html, re.DOTALL).group(0)
		everyheadline = re.findall('<h[13]>.*?</h[13]>', indiv, re.DOTALL)
		for headline in everyheadline[:Number]:
			headlines = re.search('<a[^>]*?href="(?P<link>[^"]*?)".*>(?P<story>.+?)</a>', headline, re.DOTALL)
			link = urlparse.urljoin(site, headlines.group('link'))
			story = headlines.group('story')
			topstories = story.strip() + ' -> ' + link
			phenny.say(topstories)

	elif news == 'aljazeera':
		site = 'http://english.aljazeera.net/'
		html = urllib2.urlopen(site).read()
		everyheadline = re.findall('<div id="divNewsInfo"*?>.*?</div>', html, re.DOTALL)
		for headline in everyheadline[:Number]:
			headlines = re.search('<a[^>]*?href="(?P<link>[^"]+?)"[^>]*>(?P<story>.+?)(?:<img.*?>\s)?</a>', headline, re.DOTALL)
			link = urlparse.urljoin(site, headlines.group('link'))
			story = headlines.group('story')
			topstories = story.strip() + ' -> ' + link
			phenny.say(topstories)

	elif news == 'thetimes':
		site = 'http://www.thetimes.co.uk/tto/news/'
		html = urllib2.urlopen(site).read()
		everyheadline = re.findall('<h2 class="f.*?>.*?</h2>', html, re.DOTALL)
		for headline in everyheadline[:Number]:
			headlines = re.search('<a[^>]*?href="(?P<link>[^"]*?)".*>(?P<story>.+?)</a>', headline, re.DOTALL)
			link = urlparse.urljoin(site, headlines.group('link'))
			story = headlines.group('story').replace("&#8216;", "'").replace("&#8217;", "'")
			topstories = story.strip() + ' -> ' + link
			phenny.say(topstories)
			
	#this checks Reuters homepage
	elif news == 'reuters':
		site = 'http://uk.reuters.com/'
		html = urllib2.urlopen(site).read()
		indiv = re.search("""<div class="column1 gridPanel grid8">.*?<div class="column2 gridPanel grid4">""", html, re.DOTALL).group(0)
		everyheadline = re.findall('<h2>.*?</h2>', indiv, re.DOTALL)
		for headline in everyheadline[:Number]:
			headlines = re.search('<a[^>]*?href="(?P<link>[^"]*?)".*>(?P<story>.+?)</a>', headline, re.DOTALL)
			link = urlparse.urljoin(site, headlines.group('link'))
			story = headlines.group('story')
			topstories = story.strip() + ' -> ' + link
			phenny.say(topstories)

	else:
		phenny.say("Sorry, don't have this news source :(")
		
hl.commands = ['hl']
hl.priority = 'high'
hl.example = '.hl newssource: number i.e. .story guardian: 3'

if __name__ == _main_:
	print __doc__.strip()