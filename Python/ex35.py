from sys import exit # allows for the termination capability

def gold_room():
    print "This room is full of gold. How much do you take?"
    next = raw_input("> ")
    if next.isdigit(): # check if user input is a number
        how_much = int(next) # converts the input to an integer
    else:
        dead("Man, learn how to type a number.")
    
    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False # initialize bear_moved to false

    while True: # This loop will keep going until you open the door - I think this is bad form for infinite loops, but we haven't learned exception handling
        next = raw_input("> ")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."

def cthulu_room():
    print "Here you see the great evil Cthulu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next = raw_input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulu_room() # recursive, nice

# This is clever, it prints out the result message and terminates the program with the exit(0)
def dead(why):
    print why, "Good job!"
    exit(0)

# This is the hierarchy here. The first function that nests the others in it - depending on your choice, advance to next function
def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve.")

start() # Get the game on!

# Exception handling for digits
#user_input = raw_input("> ")
#try:
 #   val = int(user_input)
#except ValueError:
#    print "That's not an int!"
