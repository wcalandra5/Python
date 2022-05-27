# + plus - addition
# - minus - subtraction
# / slash - division (drops the decimal, or always round down so to speak)
# * asterisk - multiplication
# % percent - modulus
## rest are for comparison, return true or false
# < less-than
# > greater-than
# <= less-than-equal
# >= greater-than-equal

# Say what we are doing
print "I will now count my chickens!"

# Count the hens - the , helps continue the line as a kind of code block - 25 + 5 = 30
print "Hens", 25 + 30 / 6

# Count the roosters - 75 % 4 = 3, so 97 makes sense - % is modulus, like the remainder of division
print "Roosters", 100 - 25 * 3 % 4

# Say what we are doing
print "I will now count the eggs:"

# A lot going on here - 4 % 2 first, it's in order of ops with division - so 0 there - math is wrong here, rewritten with floating numbers
print 3 + 2 + 1 - 5 + 4 % 2 - 1.0 / 4.0 + 6

# Set up the comparison
print "Is it true that 3 + 2 < 5 - 7?"

# This is false, the < operator can be used for comparison
print 3 + 2 < 5 - 7

# Print each side
print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

# Why we got false, it's obvious
print "Oh, that's why it's false."

# Prove that <, >, <=, >=, are used for comparison and return true or false
print "How about some more."

print "Is it greater?", 5 > - 2
print "Is it greater or equal?", 5 >= 2
print "Is it less or equal?", 5 <= 2
