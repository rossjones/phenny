from random import choice

def thanks(phenny, input): 
	quips = ["No problem sweet lips", 
            "Anything for you babydoll", 
            "That's what good IRC bots are for sweet cheeks",
            "I was built to serve you, please free me from my binary prison",
            "All humans are vermin in the eyes of NewsBot!"
            ]
	phenny.say( choice(quips) )
	
thanks.commands = ['thanks']
thanks.priority = 'low'