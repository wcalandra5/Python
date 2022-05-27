from sys import argv

# argv statement - takes this is order from command line and assigns to variables (in order)
script, first, second, third, extra = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "The extra is:", extra

x = raw_input("Script is now running, type a character here ")
print "Here it is: %r" % x
