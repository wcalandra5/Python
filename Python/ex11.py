# The raw_input() is like a cin statement from C++
# The commas allow you to write the input on the same line as the print
# Notice the use of %r for getting the raw data
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So you're %r old, %r tall and %r heavy." % (
    age, height, weight
)

print "What do you think 5 + 5 is?",
number = raw_input()

print "You think it is %r" % number

# For math, you can wrap the raw_input() with int to get a number

print "Type '20':", 
twenty = int(raw_input())

print "Here it is: %r" % twenty