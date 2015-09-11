# New version, based on connectives_test
# should use English sentences

import random
import string

VALUES = [True, False]

DICT = {
          True: [
                 'Snow is white', 
                 'Grass is green', 
                 'The Earth is round',
                 'Cats are mammals', 
                 'Whales are mammals',
                 'Benjamin Franklin invented the lightning rod', 
                 'Chicago is in Illinois', 
                 'A BLT is a sandwich', 
                 'Peanut butter is made from peanuts'
                 'Apples are fruits'
                 'Some plants are edible'
                 'Squares have four sides'], 
          False: [
                  'Snow is black', 
                  'Grass is orange', 
                  'The Earth is flat',
                  'Lobsters are mammals', 
                  'Dolphins are fish',
                  'Michigan borders Idaho', 
                  'Every dog is a greyhound',
                  'Motor oil is edible', 
                  'Freddie Mercury was a U.S. president'
                  'Detroit is in Iowa'
                  'Cacti are animals'
                  'Triangles have four sides']
        }


def find_bool(sent):
    if sent in DICT.items()[0][1]:
        return False
    elif sent in DICT.items()[1][1]:
        return True

def produce_pair():
    global pair
    pair = [DICT[random.choice(VALUES)][random.randint(0, len(DICT[True]) - 1)], 
            DICT[random.choice(VALUES)][random.randint(0, len(DICT[True]) - 1)]
            ]

def test_conj():
    produce_pair()
    answer = str(find_bool(pair[0]) and find_bool(pair[1]))
    print """
    What is the truth-value of the conjunction:
    '{0} AND {1}'?\n""".format(pair[0], pair[1])
    response = raw_input('> ')
    if response == answer:
    	print "\n    Correct!"
    elif string.capitalize(response) == answer:
    	print "\n    Correct!"
    else:
    	print "\n    Sorry, the answer was '{0}'.".format(answer)

def test_disj():
	produce_pair()
	answer = str(find_bool(pair[0]) or find_bool(pair[1]))
	print """
    What is the truth-value of the disjunction:
    '{0} OR {1}'?\n""".format(pair[0], pair[1])
	response = raw_input('> ')
	if response == answer:
		print "\n    Correct!"
	elif string.capitalize(response) == answer:
	    print "\n    Correct!"
	else:
		print "\n    Sorry, the answer was '{0}'.".format(answer)

def test_cond():
	produce_pair()
	answer = str(not find_bool(pair[0]) or find_bool(pair[1]))
	print """
    What is the truth-value of the conditional:
    'IF {0} THEN {1}'?\n""".format(pair[0], pair[1])
	response = raw_input('> ')
	if response == answer:
		print "\n    Correct!"
	elif string.capitalize(response) == answer:
	    print "\n    Correct!"
	else:
		print "\n    Sorry, the answer was '{0}'.".format(answer)
		
def test_bicond():
	produce_pair()
	answer = str(
	             (not find_bool(pair[0]) or find_bool(pair[1])) and
	             (not find_bool(pair[1]) or find_bool(pair[0]))
	                                                           )
	print """
    What is the truth-value of the biconditional:
    '{0} IF AND ONLY IF {1}'?\n""".format(pair[0], pair[1])
	response = raw_input('> ')
	if response == answer:
		print "\n    Correct!"
	elif string.capitalize(response) == answer:
	    print "\n    Correct!"
	else:
		print "\n    Sorry, the answer was '{0}'.".format(answer)

def test_neg():
	unit = DICT[random.choice(VALUES)][random.randint(0, 2)]
	answer = str(not find_bool(unit))
	print """
    What is the truth-value of the negation:
    'It is NOT the case that {0}'?\n""".format(unit)
	response = raw_input('> ')
	if response == answer:
		print "\n    Correct!"
	elif string.capitalize(response) == answer:
	    print "\n    Correct!"
	else:
		print "\n    Sorry, the answer was '{0}'.".format(answer)



def splash():
	print"""

            T R U T H - F U N C T I O N A L
                 C O N N E C T I V E S             
    _______________________________________________
    |                                             |
    | Test your knowledge of the truth functions! |
    | Quit at any time with CTRL-D.               |
    |                                             |
    | - Adam                                      |
    |_____________________________________________|
    
	"""

splash()

try:
	while True:
		probe = random.randint(0, 4)
		if probe == 0:
			test_conj()
		elif probe == 1:
			test_disj()
		elif probe == 2:
			test_cond()
		elif probe == 3:
			test_bicond()
		elif probe == 4:
			test_neg()

except EOFError:
	print "\n\n    Thanks for playing!\n\n"