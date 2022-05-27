ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ') # We've seen this to break up words
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10: # as long as length isn't 10, add 
    next_one = more_stuff.pop() # remember this returns last element on list - nice
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff"

print stuff[1] # return index 1
print stuff[-1] # return the last element
print stuff.pop() # delete and return the last element
print ' '.join(stuff) # join the list into one with a space - remember this is the same as join(' ', stuff) - we just add that first parameter
print '#'.join(stuff[3:6]) # at index 3 to 6, join it with a # inbetween - not including 6