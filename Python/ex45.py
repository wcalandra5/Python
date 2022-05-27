# Baseball game
from sys import exit
from random import randint
import function # test at end - suceeded

# Create a default object to create the situation function to override by all child classes - put the exit(1) to get that error message and terminate
class Default(object):

    def situation(self):
        print "This is the default class to drive the program. Build more capability if you see this."
        exit(1)

# Create the engine
class Engine(object):
 
 # initialize the event map to be used by the play() function - naming the object by key to get a starting point
    def __init__(self, event_map):
        self.event_map = event_map

# set the current event to open to the starting point
    def play(self):
        current_event = self.event_map.open_event()

# situation will return the next event - fetch that and send it to the next event class
        while True:
            print "\n--------"
            next_event_name = current_event.situation()
            current_event = self.event_map.next_event(next_event_name)

# The menu - choose the pitch to receive
class Choice(Default):

    # display message to user
    def situation(self):
        print """
    Take me out to the ballgame! Congrats, you will play some baseball.
    Here is how the game works. You will pick the pitch you face, and then
    the program will determine how many bases you receive.

    Pick which pitch you want to face (type the number). Type 0 and hit enter to quit:
    1: Fastball
    2: Curveball
    3: Changeup
    """
        choice = raw_input("> ") # get user input, generate random number
        outcome = randint(1,15)

    # These blocks generate outcomes (based on return values) to send to corresponding classes to award bases
    # The probabilities are manually entered by ranges

    # Handle edge case of character input
        if not choice.isdigit():
            print "Man, learn how to type a number"
            return 'finish'

        elif int(choice) == 1: # convert choice to integer form for comparison
            if (12 <= outcome <= 15): 
                return 'swing and miss'
            elif 8 <= outcome <= 11:
                return 'single'
            elif 5 <= outcome <= 7:
                return 'double'
            elif 2 <= outcome <= 4:
                return 'triple'
            elif outcome == 1:
                return 'home run'

        elif int(choice) == 2:
            if 10 <= outcome <= 15:
                return 'swing and miss'
            elif 8 <= outcome <= 9:
                return 'single'
            elif 3 <= outcome <= 7:
                return 'double'
            elif outcome == 2:
                return 'triple'
            elif outcome == 1:
                return 'home run'

        elif int(choice) == 3:
            if 9 <= outcome <= 15:
                return 'swing and miss'
            elif 7 <= outcome <= 8:
                return 'single'
            elif 4 <= outcome <= 6:
                return 'double'
            elif 1 <= outcome <= 3:
                return 'home run'
        
    # Case of user wanting to exit the program
        elif int(choice) == 0:
            return 'finish'

    # Handle edge case where user doesn't put a number from 1-5
        else:
            print "Penalty, learn to follow directions. Swing and miss."
            return 'swing and miss'


# case of a swing and miss result from Choice
class Miss(Default):
    
    def situation(self):

        # Award no bases
        total_bases = 0

        # Output message with result
        message = "Swing and a miss! %d bases granted" % (
        total_bases
        )

        print message

        # Return to next pitch
        return 'choice'

# Case of single result from Choice
class Single(Default):

    def situation(self):
    
        # Award a base
        total_bases = 1

        # Print resulting message
        message = "Single! %d bases granted." % (
        total_bases
        )

        print message

        # Return to next pitch
        return 'choice'

# Case of double result from Choice
class Double(Default):
    
    def situation(self):
        
        # Award two bases
        total_bases = 2

        # Print result message
        message = "Double! %d bases granted." % (
        total_bases
        )

        print message

        # Return to next pitch
        return 'choice'

# Case of triple result from Choice
class Triple(Default):
    
    def situation(self):
        
        # Award three bases
        total_bases = 3

        # Print result message
        message = "Triple! %d bases granted." % (
        total_bases
        )

        print message

        # Return to next pitch
        return 'choice'

# Case of home run result from Choice
class Homer(Default):
    
    def situation(self):

        # Award four bases
        total_bases = 4

        # Print resulting message
        message = "HOME RUN! %d bases granted." % (
        total_bases
        )

        print message

        # Return for next pitcjh
        return 'choice'
    
# Case of user choosing to leave the game from Choice
class Finish(Default):

    def situation(self):
        
        print "Congrats, you are all finished! Thanks for playing." # Add this to prevent error upon completion of the game
        print "Here's a test of adder (imported file): should print 6 ", function.adder(1,5)
        exit(0) # prevents traceback error

# Create mappings for control of program
class Map(object):

    # Create a dict in which we will generate return values to call classes (set returns to keys)
    events = {
                'choice': Choice(),
                'swing and miss': Miss(),
                'single': Single(),
                'double': Double(),
                'triple': Triple(),
                'home run': Homer(),
                'finish': Finish()
            }

    def __init__(self, start_event):
        self.start_event = start_event # sets starting event (the menu)

    def next_event(self, event_name):
        return Map.events.get(event_name) # gets the value from the dicts to direct to the next class

    def open_event(self):
        return self.next_event(self.start_event) # puts the dict key inside the classes to start them


# Run the game now
a_map = Map('choice') # this is where the game starts - goes in the engine
a_game = Engine(a_map) # sets menu
a_game.play()  # run Engine