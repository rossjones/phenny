"""
            thankyou.py - Phenny Thankyou Module
            Copyright 2011, Nicola Hughes
            Licensed under the Eiffel Forum License 2.
            
"""

from random import randint

def thanks(phenny, input): 
	quips = ["No problem sweet lips", 
            "Anything for you babydoll", 
            "That's what good IRC bots are for sweet cheeks",
            "I was built to serve you, please free me from my binary prison",
            "All humans are vermin in the eyes of NewsBot!"
            ]
	phenny.reply(quips[randint(0, len(quips)-1)])
	
thanks.commands = ['thanks']
thanks.priority = 'low'

if __name__ == _main_:
	print __doc__.strip()