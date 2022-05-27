name = 'Zed A. Shaw'
age = 35 # Not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)

# So these %d and %s are python formatters.
# %d will format integers, decimals, or numbers - put the %d where you want the number, and specify the corresponding variable with the %
# %s will concatenate strings - put the %s where you want the string, and then specify with the corresponding %
# %r is a mix of both, where it will return an object decomposed a bit - the raw data that you put in, so use it for debugging

inches_to_cm = 2.54
lbs_to_kilos = .4536

height_in_cm = height * inches_to_cm
weight_in_kg = weight * lbs_to_kilos

print "His height in cm is %r." % height_in_cm
print "His weight in kg is %r." % weight_in_kg