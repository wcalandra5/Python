def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# Hard code
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# Using variables - usually how I do it
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# I guess to prove a point here with the last two - variables just store values, and parameters are values
print "We can even do math inside too!"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# Custom function
def adder(x, y): # doesn't let you put in defaults for parameters in the def
    # x = 4 # if you wanted x to always be 4
    print x + y # MUST BE INDENTED

adder(5, 10)