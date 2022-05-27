# Game
from sys import exit # allows for the termination capability

# The correct number (global variable)
correct = 6

def gold_room():
    print "You guessed the correct number - this room is full of gold. How many ounces do you want?"
    choice = raw_input("> ")
    if choice.isdigit(): # check if user input is a number
        how_much = int(choice) # converts the input to an integer
    else:
        dead("Man, learn how to type a number.")
    
    if how_much < 72:
        print "Wow, you should've taken more, but congrats, you won %d ounces of gold!" % how_much
        exit(0)
    else:
        dead("Congrats, you won %d ounces of gold!" % how_much) # display how much gold the user won - put it inside function to work

def low_room():
    print "That guess was too low, let's see if you can get it this time."
    print "Guess again."

    choice = raw_input("> ")
    if choice.isdigit(): # check if user input is a number
        number = int(choice) # converts the input to an integer
        if number < 1 or number > 10:
            dead("Man, type a number between 1 and 10 next time.")
    else:
        dead("Man, learn how to type a number.")

    if 1 <= number <= 5:
        low_room()
    elif 7 <= number <= 10:
        high_room()
    elif number == correct:
        gold_room()
    else:
        dead("Type a number within 1 and 10 next time please.")

def high_room():
    print "That guess was too high, let's see if you can get it this time."
    print "Guess again."

    choice = raw_input("> ")

    if choice.isdigit(): # check if user input is a number
        number = int(choice) # converts the input to an integer
        if number < 1 or number > 10:
            dead("Man, type a number between 1 and 10 next time.")
    else:
        dead("Man, learn how to type a number.")

    if 1 <= number <= 5:
        low_room()
    elif 7 <= number <= 10:
        high_room()
    elif number == correct:
        gold_room()
    else:
        dead("Type a number within 1 and 10 next time please.")

# This is clever, it prints out the result message and terminates the program with the exit(0)
def dead(why):
    print why
    exit(0)

# This is the hierarchy here. The first function that nests the others in it - depending on your choice, advance to next function
def start():
    print "I am thinking of an integer from 1 to 10. Which is it?"
    choice = raw_input("> ")

    if choice.isdigit(): # check if user input is a number
        number = int(choice) # converts the input to an integer
        if number < 1 or number > 10:
            dead("Man, type a number between 1 and 10.")
    else:
        dead("Man, learn how to type a number.")

    if 1 <= number <= 5:
        low_room()
    elif 7 <= number <= 10:
        high_room()
    elif number == correct:
        gold_room()
    else:
        dead("Type a number within 1 and 10 next time please.")

start() # Get the game on!
