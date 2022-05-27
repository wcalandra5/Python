print "You enter a dark room with two doors. Do you go through door #1, door #2, or door #3?"

door = raw_input("> ")

if door == "1": # String because user input is a string
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    # Notice the whitespace. This is still in the if block of door == 1. Because we didn't dedent out.
    bear = raw_input("> ")

    # Nested if statements add more capability. Nice
    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

# Notice the indent matches the first if statement indent (or lack thereof) from the door. Nice that Python keeps you organized like this.
elif door == "2":
    print "You stare into the endless abyss at Cthulu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2": # Nice use of an or expression here - can also do like 1 < x < 10 as a statement
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "Your insanity rots your eues into a pool of muck. Good job!"

elif door == "3":
    print "You have two cards to pick from. Do you pick 1 or 2?"
    
    card = int(raw_input("> ")) # This helps with the if statement not being a string

    if card == 1:
        print "Congrats! You won a car."
    else:
        print "You lost. Sorry."


else:
    print "You stumble around and fall on a knife and die. Good job!"

# Now we are outside, this will show regardless of cases
print "Finished. That game was weird."