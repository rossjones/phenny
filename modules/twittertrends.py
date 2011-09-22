"""
            Twittertrends.py - Phenny Twittertrends Module
            Copyright 2011, Nicola Hughes
            Licensed under the Eiffel Forum License 2.
            
"""

import urllib2
import re
import json

def trends(phenny, input):
	""".trends Returns the twitter trends for a given location"""
	LOCATION = input.group(2)
	woeidurl = "http://where.yahooapis.com/v1/places.q('%s')?appid=[Bcd2FJ_V34E7G0zR8K9pWDzSlmt.WU4KO0upkVygp8gT9aDe41DE1laBL6bt7YyJSaXoC8Vt65sMrI4VOIs246qOnnzzxC8-]" % (urllib2.quote(LOCATION))
	woeidxml = urllib2.urlopen(woeidurl).read()
	woeid = re.search("<woeid>(?P<woeid>[0-9]*)</woeid>", woeidxml).group("woeid")
	
		
	twitterurl = 'http://api.twitter.com/1/trends/%s.json' % woeid
	try:
		twitterjson = json.loads(urllib2.urlopen(twitterurl).read())
		trendingterms = ""
		for i in range(0,10):
			trendingterms = trendingterms + twitterjson[0]["trends"][i]["name"] + ", "
		phenny.say(trendingterms[:-2])
	except urllib2.HTTPError:
		phenny.say("This is not a trends region on twitter, please try another.")

trends.commands = ['trends']
trends.priority = 'medium'
trends.example = '.trends London'
    
if __name__ == _main_:
	print __doc__.strip()

	