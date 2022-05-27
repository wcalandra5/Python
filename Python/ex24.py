print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.' # the escapes let you put the single quote, the slash, the newlines and the tabs

# Write a block of text
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "-------------"
print poem
print "-------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

# Define a function with some variable assignments
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates # Interesting, can return multiple variable values

start_point = 10000
beans, jars, crates = secret_formula(start_point) # Store the return values in new variables for global scope

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10 # Notice start_point gets reassigned before next function call

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point) # Makes sense, because return statement has those values in that order (beans and jelly_beans are the same really)
# This case don't need the new variable declarations
