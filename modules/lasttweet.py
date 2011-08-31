#!/usr/bin/env python
"""
twitter.py - Phenny Twitter Module
Copyright 2008, Ryan McCue
"""

import re, urllib
import web, time

timeline_url = 'http://twitter.com/statuses/user_timeline/%s.xml?count=1'
twitterers = ['rmccue', 'PatrickPatience', 'KevinPorter']
tweets = []
last_updated = time.time()
displaying_updates = False

r_status = re.compile(r'(?ims)<status>(.+?)<id>(.+?)<\/id>(.+?)<text>(.+?)<\/text>(.+?)<\/status>')

def twitter_get(user): 
   global timeline_url
   if not '%' in user:
      if isinstance(user, unicode): 
         t = user.encode('utf-8')
      else: t = user
      q = urllib.quote(t)
      u = timeline_url % q
      bytes = web.get(u)
   else: bytes = web.get(timeline_url % user)
   status = r_status.search(bytes)

   if not status or not status.group(4):
      return None

   return '%s: %s' % (user, status.group(4))

def lasttweet(phenny, input): 
   origuser = input.groups()[1]
   if not origuser: 
      return phenny.say('Perhaps you meant ".twitter rmccue"?')
   origuser = origuser.encode('utf-8')

   user = urllib.unquote(origuser)
   user = user.replace(' ', '_')

   try: result = twitter_get(user)
   except IOError: 
      error = "Can't connect to Twitter (%s)" % (timeline_url % user)
      return phenny.say(error)

   if result is not None: 
      phenny.say(result)
   else: phenny.say('%s has not yet updated or doesn\'t exist.' % origuser)

lasttweet.commands = ['lasttweet']

def twitter_background(phenny, input):
	global twitterers, tweets, last_updated, displaying_updates
	seconds_left = time.time() - last_updated
	if not twitterers or not input.sender == '#rmccue' or seconds_left < 300 or displaying_updates:
		return
	displaying_updates = True
	for origuser in twitterers:
		user = urllib.unquote(origuser)
		user = user.replace(' ', '_')

		try: result = twitter_get(user)
		except IOError: 
			error = "Can't connect to Twitter (%s)" % (timeline_url % user)
			return phenny.say(error)

		if result is None:
			continue
		else:
			if not result in tweets:
				phenny.say('Twitter update from ' + result)
				tweets.append(result)
	last_updated = time.time()
	displaying_updates = False

#twitter_background.rule = '.*'
#twitter_background.priority = 'low'

if __name__ == '__main__': 
   print __doc__.strip()