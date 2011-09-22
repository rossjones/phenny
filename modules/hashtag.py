"""
            hashtag.py - Phenny Hashtag Module
            Copyright 2011, Nicola Hughes
            Licensed under the Eiffel Forum License 2.
            
"""

import json
import urllib2

def tweets(phenny, input):
	""".tweets Returns the tweets and tweeter for the specified input for a given number of tweets"""
	QUERY = input.group(2).split(':')[0]
	Number = int(input.group(2).split(':')[1].strip(' '))
	RESULTS_PER_PAGE = '100'
	LANGUAGE = 'en'


	base_url = 'http://search.twitter.com/search.json?q=%s&rpp=%s&lang=%s&page=1' \
        	 % (urllib2.quote(QUERY), RESULTS_PER_PAGE, LANGUAGE)
    	try:
        	results_json = json.loads(urllib2.urlopen(base_url).read())
        	for i in range(0,Number):
        		phenny.say(results_json['results'][i]['from_user'] + ": " + results_json['results'][i]['text'])
            	 
    	except:
        	phenny.say('Oh dear, failed to get tweets about %s' % QUERY)

tweets.commands = ['tweets']
tweets.priority = 'medium'
tweets.example = '.tweets searchterm: number i.e. .tweets Mojo: 2'

if __name__ == '__main__':
	print __doc__.strip()