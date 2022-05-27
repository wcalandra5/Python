# Nothing new here other than printing variables where we stored the strings with formatters
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

# A little new
hilarious = False # MUST BE CAPITALIZED
joke_evaluation = "Isn't that joke so funny?! %r" # Can set the formatter as a placeholder in assignment

print joke_evaluation % hilarious # Now we set the hilarious variable in that formatter - works because raw data

w = "This is the left side of..."
e = "a string with a right side."

print w + e # Concatenate strings
