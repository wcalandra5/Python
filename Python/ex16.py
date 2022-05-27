# List of useful functions for files
# close - closes the file - like file/save in your editor
# read - reads the contents of the file. Can assign result to a variable
# readline - reads just one line of a text file
# truncate - empties the file. Watch out if you care about the file
# write(stuff) - writes stuff to the file

from sys import argv

script, filename = argv

print "We are going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?") # This just forces the action on the terminal by the user

print "Opening the file..."
target = open(filename, 'w') # w means open for write mode

print "Truncating the file. Goodbye!"
target.truncate() # This isn't necessary, since write mode will overwrite the file

print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

content = "%s \n%s \n%s \n" % (line1, line2, line3) # Little ugly with the escapes
target.write(content)

target = open(filename, 'r') # Open to read it - this is the default for open, so not really necessary
# When this was target1, it failed - necessary to open the same file multiple times, and remember, we wrote this to target, so makes sense

print "Here is what you wrote."
print target.read()

print "And finally, we close it."
target.close()
