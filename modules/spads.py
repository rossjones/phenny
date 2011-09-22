"""
            spads.py - Phenny Spads Module
            Copyright 2011, Nicola Hughes
            Licensed under the Eiffel Forum License 2.
            
"""
import urllib2
import urllib
import urlparse
import json

def spads(phenny, input):
	""".spads Returns the lastest meeting by a given Special Adviser in Number 10 for a given number
	Cueerent Spads are: Robert Riddell, Flora Coleman, Naweed Khan, Laura Trott, James McGory, Chris Saunders, Richard Reeves, Jonny Oates, Alan Sendorek, Michael Salter, Lena Pietsch, James O'Shaugnessy, Craig Oliver, Polly Mackenzie, Ed Llewellyn, Sean Kemp, Steve Hilton, Tim Colbourne, Tim Chatwin, Gabby Bertin, Martha Varney, Alison Suttie, Rohan Silva, Henry Macrory, Catherine Fall, Andy Coulson, Sean Worth, and Chris White"""
	person = input.group(2).split(':')[0]
	try:
		Number = int(input.group(2).split(':')[1].strip(' '))
	except:
		Number = 1
		
	spadapi = 'https://api.scraperwiki.com/api/1.0/datastore/sqlite?format=jsondict&name=special_advisers_gifts_and_hospitality&query=SELECT%20%60Name%20of%20Special%20Adviser%60%20FROM%20swdata%20GROUP%20BY%20%60Name%20of%20Special%20Adviser%60'
	jsonspadapi = json.loads(urllib2.urlopen(spadapi).read())
	listspad = []
	for name in jsonspadapi:
		listspad.append(name["Name of Special Adviser"])
		
	if person in listspad:
		
		type = 'jsondict'
		scraper = 'special_advisers_gifts_and_hospitality'
		query = 'SELECT `Name of Special Adviser`, `Type of hospitality received`, `Name of Organisation`, `Date of Hospitality` FROM swdata WHERE `Name of Special Adviser` = "%s" ORDER BY `Date of Hospitality` desc' % person
	
		params = { 'format': type, 'name': scraper, 'query': query}	
	
		site = 'https://api.scraperwiki.com/api/1.0/datastore/sqlite?'
		url = site + urllib.urlencode(params)
	
		jsonurl = urllib2.urlopen(url).read()
		swjson = json.loads(jsonurl)
	
		for entry in swjson[:Number]:
			ans = ('On ' + entry["Date of Hospitality"] + ' %s' % person + ' got ' + 
				   entry["Type of hospitality received"] + ' from ' + entry["Name of Organisation"])
			phenny.say(ans)
	else:
		phenny.say("%s is not in list of Special Advisers, please try another" % person)
		
spads.commands = ["spads"]
spads.priority = 'medium'
spads.example = '.spads name of special adviser: number i.e. .spads Andy Coulson: 4'

if __name__ == '__main__':
	print __doc__.strip()
		
	
	