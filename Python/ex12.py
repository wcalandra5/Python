# Improvement on prompting (the space is because the cursor is right after the string, so it gives you a space for the user reply)
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

# Remember the raw input here with %r
print "So you're %r old, %r tall and %r heavy." % (
    age, height, weight
)