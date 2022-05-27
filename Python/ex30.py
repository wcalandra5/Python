people = 30
cars = 40
buses = 15

# If cars are greater than people, print we should take the cars
if cars > people:
    print "We should take the cars."
    # else if cars are less than people, print we should not take the cars.
elif cars < people:
    print "We should not take the cars."
    # else print we can't decide
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else: # notice this else still has that colon, even without the elif statements
    print "Fine, let's stay home then."



