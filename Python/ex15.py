from sys import argv

script, filename = argv
# Could use raw_input() with a prompt to get filename if you wanted

# New open() function here
txt = open(filename)

print "Here's your file %r:" % filename

# This is new - we run a function on txt, which works since open() returns a file object
print txt.read()
# This is a read() function with no parameters. conducted on txt

txt.close() # Always good to close files when done with them

# Same idea here, just getting stored in different variables - if you had a different file this would run on that file
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt_again.close()