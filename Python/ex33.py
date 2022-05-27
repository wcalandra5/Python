i = 0 # intialize i to 0
numbers = []

while i < 6: # will stop at 6, not including it
    print "At the top i is %d" % i
    numbers.append(i) # append i to the end of numbers, building that list

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

# For loop based off of numbers list
print "The numbers: "
for num in numbers:
    print num

print '\n'

# Build function
def while_loop(start, stop, increment):
    i = start
    numbers = []
    while i < stop:
        print "At the top i in the functuion is %d" % i
        numbers.append(i) # append i to the end of numbers, building that list

        i = i + increment
        print "Numbers now in the function: ", numbers
        print "At the bottom i is %d" % i
    
    print "The numbers: "
    for num in numbers:
        print num

# Calling function
# while_loop(0,6,1)

# New numbers
while_loop(2,9,2)

# Build function with for loop
def for_loop(start, ranger):
    i = start
    ranger = range(start, ranger)
    numbers = []
    for i in ranger:
        print "Adding %d to the list:" % i
        numbers.append(i) # append i to the end of numbers, building that list

       # i = i + increment # This doesn't matter in the for loop
        print "Numbers now in the function: ", numbers
        print "At the bottom i is %d" % i
    
    print "The numbers: "
    for num in numbers:
        print num

for_loop(0,9)